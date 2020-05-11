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
# Load names #
nace_names  = module_dir + 'extra_data_csv/nace_to_full_name.csv'
nace_names  = pandas.read_csv(str(nace_names))
waste_names = module_dir + 'extra_data_csv/waste_to_full_name.csv'
waste_names = pandas.read_csv(str(waste_names))

# Load waste spreading #
spreading = module_dir + 'extra_data_csv/waste_spreading.csv'
spreading = pandas.read_csv(str(spreading))

# Will be used to filter later #
wastes_selected = list(waste_names.query("category == 'eurostat'")['waste'])
nace_selected   = list(nace_names['nace'])

###############################################################################
# Load spread coefficients #
spread_coefs = module_dir + 'extra_data_csv/waste_spreading.csv'
spread_coefs = pandas.read_csv(str(spread_coefs))

# Make a dataframe for every sheet in the original xls #
spread_by_nace = {k: df for k, df in spread_coefs.groupby('nace')}

# Apply the default to all non-mentioned nace #
default_spread = spread_by_nace.pop('default')
spread_by_nace = {k: spread_by_nace[k] if k in spread_by_nace
                  else default_spread.copy()
                  for k in nace_selected}

# Format each dataframe #
for k, df in spread_by_nace.items():
    df = df.drop(columns=['nace'])
    df = df.set_index('waste')
    df = df.fillna(0)
    spread_by_nace[k] = df
