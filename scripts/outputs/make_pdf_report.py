#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Script to generate the output PDF comparison report.

Typically you would run this file from a command line like this:

     ipython3 -i -- ~/deploy/waste_flow/scripts/outputs/make_pdf_report.py
"""

###############################################################################
from waste_flow.viz.gen_by_country import legend
print(legend.plot(rerun=True))

from waste_flow.viz.gen_by_country import countries
for gen_viz in countries.values():
    print(gen_viz.plot(rerun=True))

from waste_flow.viz.gen_by_sector import sectors
for gen_viz in sectors.values():
    print(gen_viz.plot(rerun=True))

#-----------------------------------------------------------------------------#
from waste_flow.viz.summary import legend_ind, legend_hh
print(legend_ind.plot(rerun=True))
print(legend_hh.plot(rerun=True))

from waste_flow.viz.summary import countries_ind, countries_hh
for gen_viz in countries_ind.values():
    print(gen_viz.plot(rerun=True))
for gen_viz in countries_hh.values():
    print(gen_viz.plot(rerun=True))

#-----------------------------------------------------------------------------#
from waste_flow.reports.comparison import report
print(report())
