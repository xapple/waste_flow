#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Typically you can use this class this like:

    >>> from waste_flow.treatment import waste_trt
"""

# Built-in modules #

# Internal modules #
from waste_flow.zip_files import waste_trt as orig_trt

# First party modules #

# Third party modules #

###############################################################################
class WasteTreatment:

    @property
    def df(self):
        """Format and filter the dataframe."""
        # Load #
        df = orig_trt.df.copy()
        # Return #
        return df

###############################################################################
# Create singleton #
waste_trt = WasteTreatment()
