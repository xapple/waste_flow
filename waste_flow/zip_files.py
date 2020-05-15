#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Typically you can use this class like this:

    >>> from waste_flow.zip_files import waste_gen, waste_trt
    >>> print(waste_gen.cache_is_valid)
    >>> print(waste_trt.cache_is_valid)

To download the zips:

    >>> from waste_flow.zip_files import waste_gen, waste_trt
    >>> print(waste_gen.refresh_cache())
    >>> print(waste_trt.refresh_cache())

To look at the raw contents as dataframes:

    >>> from waste_flow.zip_files import waste_gen, waste_trt
    >>> print(waste_gen.raw_csv)
    >>> print(waste_trt.raw_csv)

To look at the processed contents as dataframes:

    >>> from waste_flow.zip_files import waste_gen, waste_trt
    >>> print(waste_gen.processed_csv)
    >>> print(waste_trt.processed_csv)

To look at the filtered contents as dataframes:

    >>> from waste_flow.zip_files import waste_gen, waste_trt
    >>> print(waste_gen.df)
    >>> print(waste_trt.df)
"""

# Built-in modules #
import gzip, io

# Internal modules #
from waste_flow import cache_dir

# First party modules #
from plumbing.cache    import property_pickled_at
from plumbing.scraping import download_from_url
from autopaths         import Path

# Third party modules #
import pandas

###############################################################################
class ZipFile:
    """
    Download a zipped CSV file containing all countries and all categories
    from the EUROSTAT webserver.

    The original strategy to convert colons to NaN was the following:

        # If there is a colon in a cell, it's not a number #
        def colon_to_nan(cell): return numpy.NaN if ':' in cell else cell
        df = df.applymap(colon_to_nan)
    """

    base_url   = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/" \
                 "BulkDownloadListing"

    def __init__(self, zip_cache_dir):
        # Record where the cache will be located on disk #
        self.cache_dir = zip_cache_dir
        # Where the file should be downloaded to #
        self.zip_path = Path(self.cache_dir + self.zip_name)

    def refresh_cache(self):
        """Will download the required zip files to the cache directory."""
        return download_from_url(self.base_url + self.url_param,
                                 self.zip_path,
                                 stream     = False,
                                 progress   = False,
                                 uncompress = False)

    # ---------------------------- Properties --------------------------------#
    @property
    def cache_is_valid(self, check_md5=True):
        """Checks if the file needed has been correctly downloaded."""
        # Simple case #
        if not self.zip_path.exists: return False
        if not check_md5:            return True
        # Check the MD5 #
        return self.zip_path.md5 == self.md5

    @property
    def raw_csv(self):
        """
        Loads the big CSV that's inside the ZIP into memory.
        We don't specify na_values = [':', ': '] here because it's done later.
        """
        # Check the cache #
        if not self.cache_is_valid:
            self.refresh_cache()
            if not self.cache_is_valid:
                raise Exception("Error refreshing cache")
        # Load the CSV #
        with gzip.open(self.zip_path) as csv_handle:
            text_mode = io.TextIOWrapper(csv_handle, encoding=self.encoding)
            return pandas.read_csv(text_mode, sep = ',|\t', engine = 'python')

    @property_pickled_at('csv_cache_path')
    def processed_csv(self):
        """Format the data frame and store it in cache."""
        # Load #
        df = self.raw_csv
        # Strange name due to wrong column parsing and tabs #
        df = df.rename(columns={'geo\\time': 'country'})
        # Also many column names have trailing whitespace #
        df.columns = df.columns.str.strip().str.replace(' ','_')
        # Some cells have a number and a character or just a character #
        for col in map(str, (2016, 2014, 2012, 2010, 2008, 2006, 2004)):
            df[col] = df[col].apply(pandas.to_numeric, errors = 'coerce')
        # Return #
        return df

    @property
    def df(self):
        """Filter the dataframe."""
        # Load #
        df = self.processed_csv
        # Filter for those that we want - UNIT #
        df = df.query("unit == 'T'")
        df = df.drop(columns=['unit'])
        # Filter for those that we want - HAZARD #
        df = df.query("hazard == 'HAZ_NHAZ'")
        df = df.drop(columns=['hazard'])
        # Albania, Kosovo and Turkey are missing entries, drop them #
        df = df.query("country != 'AL'")
        df = df.query("country != 'XK'")
        df = df.query("country != 'TR'")
        # Return #
        return df

    # -------------------------------- Cache -------------------------------- #
    @property
    def csv_cache_path(self):
        """Specify where on the file system we will pickle the property."""
        return self.cache_dir + self.short_name + '.pickle'

###############################################################################
class WasteGen(ZipFile):

    short_name = "env_wasgen"
    long_name  = "Generation of waste by waste category, hazardousness and" \
                 " NACE Rev. 2 activity."
    url_param  = "?file=data/env_wasgen.tsv.gz"
    zip_name   = "env_wasgen.tsv.gz"
    csv_name   = "env_wasgen.tsv"
    encoding   = "ISO-8859-1"
    md5        = "df2ab56bb48bb2bf0e3266d08fa4d408"

#-----------------------------------------------------------------------------#
class WasteTrt(ZipFile):

    short_name = "env_wastrt"
    long_name  = "Treatment of waste by waste category, hazardousness and" \
                 " waste management operations."
    url_param  = "?file=data/env_wastrt.tsv.gz"
    zip_name   = "env_wastrt.tsv.gz"
    csv_name   = "env_wastrt.tsv"
    encoding   = "ISO-8859-1"
    md5        = "bfbfc036921b22698e52eab168f3f891"

###############################################################################
# Create singletons #
waste_gen = WasteGen(cache_dir + 'eurostat/')
waste_trt = WasteTrt(cache_dir + 'eurostat/')