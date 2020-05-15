#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Typically you can use this class like this:

    >>> from waste_flow.spreading import spread
    >>> print(spread.by_nace)
"""

# Built-in modules #

# Internal modules #
from waste_flow.common import spread_coefs, nace_selected

# First party modules #
from plumbing.cache import property_cached

# Third party modules #

###############################################################################
class WasteSpreading:

    # ----------------------------- Properties ------------------------------ #
    @property_cached
    def by_nace(self):
        """
        Returns a dictionary where every key is a nace sector name
        and every value is a dataframe looking like this:

                  W072  W073  W075  W076  W091  W092  W093    W101
        waste
        W072_hh    1.0  0.00   0.0   0.0   0.0   0.0   0.0  0.1505
        W075_hh    0.0  0.00   1.0   0.0   0.0   0.0   0.0  0.0075
        W091_hh    0.0  0.00   0.0   0.0   1.0   0.0   0.0  0.2500
        W092_hh    0.0  0.00   0.0   0.0   0.0   1.0   0.0  0.0400
        W7376_hh   0.0  0.54   0.0   0.4   0.0   0.0   0.0  0.0024
        W9999_hh   0.0  0.00   0.0   0.0   0.0   0.0   0.0  0.0335
        """
        # Make a dataframe for every sheet in the original xls #
        result = {k: df for k, df in spread_coefs.groupby('nace')}
        # Remove the default spreading from the dict #
        default_spread = result.pop('default')
        # Apply the default to all non-mentioned nace #
        result = {k: result[k]
                     if   k in result
                     else default_spread.copy()
                     for  k in nace_selected}
        # Format each dataframe #
        result = {k: self.format_spread(df) for k, df in result.items()}
        # Return #
        return result

    # ------------------------------ Methods -------------------------------- #
    def format_spread(self, df):
        """Format a given dataframe."""
        # Drop columns #
        df = df.drop(columns=['nace'])
        # Set index #
        df = df.set_index('waste')
        # Assume zero everywhere #
        df = df.fillna(0)
        # Return #
        return df

###############################################################################
# Create singleton #
spread = WasteSpreading()
