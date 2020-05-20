#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Typically you can use this file like this:

    >>> from waste_flow.common import waste_names
    >>> print(waste_names)
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

# Load treatment names #
trt_names = module_dir + 'extra_data_csv/treatment_to_full_name.csv'
trt_names = pandas.read_csv(str(trt_names))

# Will be used to filter later #
nace_selected   = list(nace_names['nace'])
trt_selected    = list(trt_names['treatment'])
wastes_selected = list(waste_names.query("category == 'eurostat'")['waste'])
wastes_created  = list(waste_names.query("category != 'eurostat'")['waste'])

# Load spread coefficients #
spread_coefs = module_dir + 'extra_data_csv/waste_spreading.csv'
spread_coefs = pandas.read_csv(str(spread_coefs))

# Load dry to wet coefficients #
wet_coefs = waste_names.query("category != 'eurostat'")
wet_coefs = wet_coefs.reset_index(drop=True)
wet_coefs = wet_coefs.set_index('waste')['wet_fraction']

# Load country codes #
country_codes = module_dir + 'extra_data_csv/foastat_countries.csv'
country_codes = pandas.read_csv(str(country_codes))

###############################################################################
# Load names that appear in the other dataframe #
orig_w_names = set(spread_coefs['waste'])
new_w_names  = set(spread_coefs.columns) - {'waste', 'nace'}

# Check that waste names match #
assert orig_w_names == set(wastes_created)
assert new_w_names  == set(wastes_selected)

###############################################################################
# Split in two #
waste_names_ind = [w for w in waste_names['waste'] if w.endswith('_ind')]
waste_names_hh  = [w for w in waste_names['waste'] if w.endswith('_hh')]
waste_names_ind = waste_names.query("waste in @waste_names_ind")
waste_names_hh  = waste_names.query("waste in @waste_names_hh")