#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Development script to test the usage examples included in the README.

Typically you would run this file from a command line like this:

     ipython3 -i -- ~/deploy/waste_flow/scripts/docs/run_readme_examples.py
"""

###############################################################################
from waste_flow.analysis import waste_ana
print(waste_ana.dry_mass)

###############################################################################
from waste_flow.generation import waste_gen
params = ("waste   == 'W073' & "
          "country == 'UK' & "
          "year    == '2008'")
result = waste_gen.long_format.query(params)
print(result)

###############################################################################
from waste_flow.viz.gen_by_country import legend
print(legend.plot(rerun=True))
from waste_flow.viz.gen_by_country import countries
for gen_viz in countries.values():
    print(gen_viz.plot(rerun=True))
