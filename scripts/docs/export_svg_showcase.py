#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

A script to export some graphs in SVG format for inclusion in the README
and showcasing.

Typically you would run this file from a command line like this:

     ipython3 -i -- ~/deploy/waste_flow/scripts/docs/export_showcase_svg.py
"""

# Built-in modules #

# Internal modules #
from waste_flow import repos_dir

# First party modules #

# Third party modules #
from tqdm import tqdm

###############################################################################
# Legend #
from waste_flow.viz.gen_by_country import legend

# Set it to SVG #
legend.formats = ('svg',)

# Change output path #
legend.base_dir = repos_dir + 'docs/showcase_graphs/'

# Plot #
legend.plot(rerun=True)

###############################################################################
# Sectors #
from waste_flow.viz.gen_by_sector import sectors

# Select a given nace category #
viz = sectors['C20-C22']

# Set them all to SVG #
for g in viz.all_graphs: g.formats = ('svg',)

# Change output paths #
for g in viz.all_graphs: g.base_dir = repos_dir + 'docs/showcase_graphs/'

# Change names #
for g in viz.all_graphs: g.short_name = '_'.join(c for c in g.batch)

# Plot all graphs #
for g in tqdm(viz.all_graphs): g.plot(rerun=True)
