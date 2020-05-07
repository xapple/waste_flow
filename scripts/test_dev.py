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
#print(waste_gen.dry_long)

###############################################################################
#from waste_flow.outputs import outputs
#print(outputs.make_dry_mass('~/test/dry_mass.xlsx'))

###############################################################################
from waste_flow.viz.gen_by_country import legend
print(legend.plot(rerun=True))

from waste_flow.viz.gen_by_sector import sectors as all_gen_viz

i = 0
for gen_viz in all_gen_viz.values():
    print(gen_viz.plot(rerun=True))
    i += 1
    if i > 1: break

###############################################################################
from waste_flow.reports.comparison import ComparisonReport
report = ComparisonReport('~/test/report.pdf')
print(report())

###############################################################################
#from waste_flow.common import nace_names, waste_names
#print(waste_names)

###############################################################################
#from waste_flow.viz.gen_by_sector import sectors as all_gen_viz
#print(all_gen_viz)
#print(list(all_gen_viz.values())[0].df.index.levels[0])