#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Typically you can use this class like this:

    >>> from waste_flow.generation import waste_gen
    >>> print(waste_gen.wide_format)
"""

# Built-in modules #

# Internal modules #
from waste_flow.zip_files import waste_gen as orig_gen

# First party modules #
from plumbing.cache import property_cached

# Third party modules #
import pandas

###############################################################################
class WasteGeneration:

    # ----------------------------- Formatting ------------------------------ #
    @property
    def filtered(self):
        """Filter the dataframe some more."""
        # Load #
        df = orig_gen.df
        # Filter for only the waste categories we are interested in #
        from waste_flow.common import wastes_selected
        df = df.query("waste in @wastes_selected")
        # Filter for only the nace categories we are interested in #
        from waste_flow.common import nace_selected
        df = df.query("nace_r2 in @nace_selected")
        # Return #
        return df

    @property_cached
    def long_format(self):
        """
        Transform the dataframe into the long format
        (and not the wide format).
        """
        # Load #
        df = self.filtered
        # Unpivot #
        df = df.melt(id_vars    = ['nace_r2', 'waste', 'country'],
                     value_name = 'tonnes',
                     var_name   = 'year')
        # Sort by country then by year etc. #
        columns_order = ['country', 'year', 'waste', 'nace_r2']
        df = df[columns_order + ['tonnes']]
        df = df.sort_values(columns_order)
        # Return #
        return df

    @property_cached
    def wide_format(self):
        """
        Transform the dataframe into the wide format
        (and not the long format).
        With waste categories as column names.
        """
        # Load #
        df = self.long_format
        # Pivot #
        df = df.pipe(pandas.pivot_table,
                     index   = ['country', 'year', 'nace_r2'],
                     columns = ['waste'],
                     values  = ['tonnes'])
        # Only one level on the column index #
        df.columns = df.columns.droplevel()
        # Return #
        return df

###############################################################################
# Create singleton #
waste_gen = WasteGeneration()
