#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.
"""

# Built-in modules #

# Internal modules #

# First party modules #

# Third party modules #

###############################################################################
class Country:
    """Represents one country's dataset."""

    def __init__(self, code):
        # The reference country code #
        self.code = code

    def __repr__(self):
        return '%s object code "%s"' % (self.__class__, self.code)

    @property
    def gen(self):
        """
        Return rows that concern this country only for the
        waste generation table.
        """
        # Load #
        df = zip_file.df
        # Select rows for country #
        selector = df['country'] == self.code
        df       = df[selector]
        # We don't need the country column anymore #
        df = df.drop(columns=['country'])
        # We don't need the old index anymore #
        df = df.reset_index(drop=True)
        # Return #
        return df

###############################################################################
# Get all possible countries #
all_codes = 0

# Create every country object #
all_countries = [Country(code) for code in all_codes]
countries     = {c.code: c for c in all_countries}
