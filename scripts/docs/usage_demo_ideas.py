#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Development script to test some of the methods in `waste_flow`.
This is mostly just scrap code. Some of these snippets could be used
as extra examples in the main `README.md` file.
"""

###############################################################################
from waste_flow.zip_files import waste_gen, waste_trt

print(waste_gen.cache_is_valid)
print(waste_trt.cache_is_valid)

print(waste_gen.refresh_cache())
print(waste_trt.refresh_cache())

print(waste_gen.raw_csv)
print(waste_trt.raw_csv)

del waste_gen.processed_csv
del waste_trt.processed_csv

print(waste_gen.processed_csv.shape)
print(waste_trt.processed_csv.shape)

print(waste_gen.df)
print(waste_trt.df)

###############################################################################
from waste_flow.viz.gen_by_country import legend
print(legend.plot(rerun=True))

from waste_flow.viz.gen_by_sector import sectors as all_gen_viz

i = 0
for gen_viz in all_gen_viz.values():
    print(gen_viz.plot(rerun=True))
    i += 1
    if i > 3: break

###############################################################################
from waste_flow.reports.comparison import ComparisonReport
report = ComparisonReport('~/test/report.pdf')
print(report())

###############################################################################
from waste_flow.viz.gen_by_sector import sectors as all_gen_viz
print(all_gen_viz)
print(list(all_gen_viz.values())[0].df.index.levels[0])

###############################################################################
from waste_flow.common import wastes_selected
from waste_flow.common import nace_selected
print(wastes_selected)
print(nace_selected)

###############################################################################
from waste_flow.spreading import spread
print(spread.by_nace['A'])
print(spread.by_nace['EP_HH'])

###############################################################################
from waste_flow.generation import waste_gen
del waste_gen.spread_waste
print(waste_gen.dry_mass)

###############################################################################
from waste_flow.analysis import waste_ana
del waste_ana.spread_waste
print(waste_ana.spread_waste)

###############################################################################
from waste_flow.analysis import waste_ana
print(waste_ana.summary_recovered)

###############################################################################
from waste_flow.country import countries
eu = countries['EU28']
df = eu.wide_format

###############################################################################
from waste_flow.viz.summary import countries_ind
for gen_viz in countries_ind.values(): print(gen_viz.plot(rerun=True))

###############################################################################
from waste_flow.generation import waste_gen
params = "country == 'BA'"
result = waste_gen.long_format.query(params)
print(result)