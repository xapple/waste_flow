#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Typically you can use this class this like:

    >>> from waste_flow.generation import waste_gen
"""

# Built-in modules #

# Internal modules #
from waste_flow           import module_dir
from waste_flow.zip_files import waste_gen as orig_gen

# First party modules #
from plumbing.cache import property_cached

# Third party modules #
import pandas

###############################################################################
class WasteGeneration:

    @property
    def filtered(self):
        """Filter the dataframe some more."""
        # Load #
        df = orig_gen.df
        # Filter for only the waste categories we are interested in #
        from waste_flow.mappings import wastes_selected
        df = df.query("waste in @wastes_selected")
        # Filter for only the nace categories we are interested in #
        from waste_flow.mappings import nace_selected
        df = df.query("nace_r2 in @nace_selected")
        # Return #
        return df

    @property
    def pivoted(self):
        """
        Transform the dataframe into the long format
        (and not the wide format).
        """
        # Load #
        df = orig_gen.df
        # Pivot #
        pass
        # Return #
        return df

    @property_cached
    def df(self):
        """
        Remove the municipal waste category and spread it
        in other categories according to specifc breakdown proportions.
        The municipal waste should be called as such because otherwise
        it can be confused with the "household" nace sector.
        """
        # Load #
        df = orig_gen.df
        # Load municipal breakdown #
        muni_break = module_dir + 'extra_data/municipal_breakdown.csv'
        muni_break = pandas.read_csv(str(muni_break))
        muni_break = muni_break.fraction
        # Remove the municipal waste and spread it in other categories #
        muni_total = df
        broken_down = df.multiply(muni_break)
        # Return #
        return df

###############################################################################
# Create singleton #
waste_gen = WasteGeneration()
