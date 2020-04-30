#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Development script to test some of the methods in `waste_flow`

Typically you would run this file from a command line like this:

     ipython3 -i -- ~/deploy/waste_flow/scripts/test_dev.py
"""

# Built-in modules #

# Third party modules #

###############################################################################
#from waste_flow.zip_files import waste_gen, waste_trt

#print(waste_gen.cache_is_valid)
#print(waste_trt.cache_is_valid)

#print(waste_gen.refresh_cache())
#print(waste_trt.refresh_cache())

#print(waste_gen.raw_csv)
#print(waste_trt.raw_csv)

#del waste_gen.processed_csv
#del waste_trt.processed_csv

#print(waste_gen.processed_csv.shape)
#print(waste_trt.processed_csv.shape)

#print(waste_gen.df)
#print(waste_trt.df)

###############################################################################
#from waste_flow.generation import waste_gen
#print(waste_gen.dry_mass)

###############################################################################
from waste_flow.outputs import outputs
print(outputs.make_excel())
