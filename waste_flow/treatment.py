#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Typically you can use this class like this:

    >>> from waste_flow.treatment import waste_trt
    >>> print(waste_trt.normalized)
"""

# Built-in modules #

# Internal modules #
from waste_flow.zip_files import waste_trt as orig_trt

# First party modules #
from plumbing.cache import property_cached

# Third party modules #
import pandas

###############################################################################
class WasteTreatment:

    # ----------------------------- Formatting ------------------------------ #
    @property
    def filtered(self):
        """Filter the dataframe some more."""
        # Load #
        df = orig_trt.df
        # Filter for only the waste categories we are interested in #
        from waste_flow.common import wastes_selected
        df = df.query("waste in @wastes_selected")
        # Filter for only the trt operations we are interested in #
        from waste_flow.common import trt_selected
        df = df.query("wst_oper in @trt_selected")
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
        df = df.melt(id_vars    = ['wst_oper', 'waste', 'country'],
                     value_name = 'tonnes',
                     var_name   = 'year')
        # Sort by country then by year etc. #
        columns_order = ['country', 'year', 'waste', 'wst_oper']
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
                     index   = ['country', 'year', 'wst_oper'],
                     columns = ['waste'],
                     values  = ['tonnes'])
        # Return #
        return df

    # ----------------------------- Processing ------------------------------ #
    @property_cached
    def normalized(self):
        """
        Here we divide each group of year, country and waste category by its
        total in order to obtain the fraction that ends up in each different
        treatment destination.

        NB: NaNs do not affect the normalization here as sum is called
            without skip_na=True and we then fill the remaining ones.
        """
        # Load dataframe #
        df = self.long_format
        # Group #
        groups = df.groupby(['country', 'year', 'waste'])
        # Add the frac column #
        df['frac'] = groups.transform(lambda x: (x / x.sum()))
        # Fill remaining NaNs #
        df = df.fillna(0.0)
        # Drop the tonnes column #
        df = df.drop(columns=['tonnes'])
        # Return #
        return df

###############################################################################
# Create singleton #
waste_trt = WasteTreatment()
