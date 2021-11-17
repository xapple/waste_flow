#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Typically you can use this class like this:

    >>> from waste_flow.country import countries
    >>> for country in countries.values():
    >>>     print('**' + country.long_name + '**')
    >>>     print(country.summary_recovered)
"""

# Built-in modules #
import importlib

# Internal modules #
from waste_flow.common    import country_codes
from waste_flow.zip_files import waste_gen as gen_orig
from waste_flow.zip_files import waste_trt as trt_orig

# First party modules #
from plumbing.cache import property_cached

# Third party modules #

###############################################################################
class Country:
    """Represents one country's dataset."""

    def __init__(self, code):
        # The reference country code #
        self.code = code

    def __repr__(self):
        return '%s object code "%s"' % (self.__class__, self.code)

    # ----------------------------- Properties ------------------------------ #
    @property_cached
    def long_name(self):
        """The long name of this country."""
        row = country_codes.query('nuts_zero_2010 == @self.code')
        return row.iloc[0]['country']

    @property
    def wide_format(self):
        return self.get_a_df('waste_flow.analysis.waste_ana',
                             'wide_format')

    @property
    def summary_recovered(self):
        return self.get_a_df('waste_flow.analysis.waste_ana',
                             'summary_recovered')

    @property
    def waste_gen(self):
        return self.get_a_df('waste_flow.generation.waste_gen',
                             'wide_format',
                             False)

    # ------------------------------ Methods -------------------------------- #
    def get_a_df(self, location, df_name, by_index=True):
        """
        Return rows that concern this country only for any
        given dataframe passed in the location argument.
        """
        # Split #
        module_path = '.'.join(location.split('.')[:-1])
        object_name = location.split('.')[-1]
        # Import #
        mdl = importlib.import_module(module_path)
        obj = getattr(mdl, object_name)
        # Load #
        df = getattr(obj, df_name)
        # Select rows for current country #
        if by_index: df = df.loc[[self.code]].copy()
        else:        df = df.query("country == '%s'" % self.code)
        # We don't need the country column anymore #
        if by_index: df = df.droplevel(0)
        else:        df = df.reset_index().drop(columns=['country'])
        # Return #
        return df

###############################################################################
# Get all possible countries #
gen_codes = set(gen_orig.df.country.unique())
trt_codes = set(trt_orig.df.country.unique())
all_codes = list(gen_codes & trt_codes)
all_codes.sort()

# Create every country object #
all_countries = [Country(code) for code in all_codes]
countries     = {c.code: c for c in all_countries}
