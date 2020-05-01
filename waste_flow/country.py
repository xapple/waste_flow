#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.
"""

# Built-in modules #

# Internal modules #
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

    @property_cached
    def dry_mass(self):
        """
        Return rows that concern this country only for the
        waste generation dry mass table.
        """
        # Import #
        from waste_flow.generation import waste_gen
        # Load #
        df = waste_gen.dry_mass
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
