#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Script to generate the output XLS files.

Typically you would run this file from a command line like this:

     ipython3 -i -- ~/deploy/waste_flow/scripts/outputs/make_xls_outputs.py
"""

###############################################################################
from waste_flow.analysis import waste_ana
del waste_ana.spread_waste

from waste_flow.outputs import waste_breakdown, summary_recovered
waste_breakdown()
summary_recovered()
