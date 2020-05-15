#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Script to generate the output PDF comparison report.

Typically you would run this file from a command line like this:

     ipython3 -i -- ~/deploy/waste_flow/scripts/outputs/make_outputs.py
"""

###############################################################################
from waste_flow.viz.gen_by_country import legend
print(legend.plot(rerun=True))

#from waste_flow.viz.gen_by_country import countries
#for gen_viz in countries.values():
#    print(gen_viz.plot(rerun=True))
#
#from waste_flow.viz.gen_by_sector import sectors
#for gen_viz in sectors.values():
#    print(gen_viz.plot(rerun=True))

from waste_flow.reports.comparison import ComparisonReport
report = ComparisonReport()
print(report())
