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
nace_names  = module_dir + 'extra_data/nace_to_full_name.csv'
nace_names  = pandas.read_csv(str(nace_names))
waste_names = module_dir + 'extra_data/waste_to_full_name.csv'
waste_names = pandas.read_csv(str(waste_names))
