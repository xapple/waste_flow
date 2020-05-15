#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.
"""

# Built-in modules #
import importlib

# Internal modules #
from waste_flow.common    import country_codes
from waste_flow.zip_files import waste_gen as gen_orig

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

    # ------------------------------ Methods -------------------------------- #
    def get_a_df(self, location, df_name):
        """
        Return rows that concern this country only for any
        given dataframe passed in the location argument.
        """
        # Split #
        module_path = '.'.join(location.split('.')[:-1])
        object_name = location.split('.')[-1]
        # Import #
        mod = importlib.import_module(module_path)
        obj = getattr(mod, object_name)
        # Load #
        df = getattr(obj, df_name)
        # Select rows for current country #
        df = df.loc[[self.code]].copy()
        # We don't need the country column anymore #
        df = df.droplevel(0)
        # Return #
        return df

###############################################################################
# Get all possible countries #
all_codes = list(gen_orig.df.country.unique())

# Create every country object #
all_countries = [Country(code) for code in all_codes]
countries     = {c.code: c for c in all_countries}
