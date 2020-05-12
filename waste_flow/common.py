#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.
"""

# Built-in modules #

# Internal modules #
from waste_flow import module_dir

# First party modules #

# Third party modules #
import pandas

###############################################################################
# Load nace names #
nace_names = module_dir + 'extra_data_csv/nace_to_full_name.csv'
nace_names = pandas.read_csv(str(nace_names))

# Load waste names #
waste_names = module_dir + 'extra_data_csv/waste_to_full_name.csv'
waste_names = pandas.read_csv(str(waste_names))

# Will be used to filter later #
wastes_selected = list(waste_names.query("category == 'eurostat'")['waste'])
nace_selected   = list(nace_names['nace'])

# Load spread coefficients #
spread_coefs = module_dir + 'extra_data_csv/waste_spreading.csv'
spread_coefs = pandas.read_csv(str(spread_coefs))

