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
# Wastes #
wastes_selected = ['W072', 'W073', 'W075', 'W076', 'W091', 'W092', 'W093', 'W101']

municipal = 'W101'

# Sectors #
industrial = ['A', 'B', 'C', 'D',
              'E36_E37_E39', 'E38',
              'F', 'G-U_X_G4677', 'G4677']

household  = ['EP_HH']

nace_selected = industrial + household