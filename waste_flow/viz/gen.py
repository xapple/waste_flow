#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.
"""

# Built-in modules #

# Internal modules #
from waste_flow import cache_dir, module_dir
from waste_flow.country import all_countries

# First party modules #
from plumbing.graphs.multiplot import Multiplot
from plumbing.cache import property_cached
from plumbing.graphs.solo_legend import SoloLegend

# Third party modules #
from matplotlib import pyplot
import pandas

# Load names #
nace_names  = module_dir + 'extra_data/nace_to_full_name.csv'
nace_names  = pandas.read_csv(str(nace_names))
waste_names = module_dir + 'extra_data/waste_to_full_name.csv'
waste_names = pandas.read_csv(str(waste_names))

# Where to store the graphs #
base_dir = cache_dir + 'graphs/gen_viz/'

###############################################################################
class GenerationViz:
    """
    Every country has one GenerationViz object containing
    several graphs.
    Each graph contains a fixed number of subplots.
    Each subplot corresponds to one sector (nace).
    """

    def __init__(self, country):
        self.country = country

    def plot(self, *ag, **kw):
        return [graph.plot(*ag, **kw) for graph in self.all_graphs]

    @property_cached
    def df(self):
        # Load #
        df = self.country.dry_mass
        # Swap index levels #
        df = df.reset_index()
        df = df.sort_values(['nace_r2', 'year'])
        df = df.set_index(['nace_r2', 'year'])
        # Return #
        return df

    @property_cached
    def all_graphs(self):
        # Get all sectors #
        sectors = self.df.index.levels[0]
        # Sort sectors into batches of a given size #
        size    = GenPlot.n_cols
        count   = len(sectors)
        batches = [sectors[i:i + size] for i in range(0, count, size)]
        # One graph per sector #
        result = [GenPlot(self, batch) for batch in batches]
        # Return #
        return result

###############################################################################
class GenPlot(Multiplot):

    # Basic params #
    formats    = ('pdf',)
    share_y    = False
    share_x    = False
    height     = 7
    width      = 30

    # Labels for axes #
    label_x = 'Year'
    label_y = 'Dry mass in kilograms'

    # Size of grid #
    n_rows = 1
    n_cols = 4

    def __init__(self, parent, batch):
        # Save batch #
        self.batch = batch
        # Call parent class #
        super(GenPlot, self).__init__(parent, base_dir)

    @property_cached
    def short_name(self):
        return self.parent.country.code + '|' + '+'.join(c for c in self.batch)

    def lines_plot(self, sector, axes, **kw):
        # Load #
        df = self.parent.df
        # Filter for the current sector #
        df = df.loc[[sector]]
        # We don't need the sector column anymore #
        df = df.droplevel(0)
        # Get all waste types #
        wastes = df.columns
        # Plot every line #
        for waste in wastes:
            axes.plot(df[waste],
                      marker     = ".",
                      markersize = 20.0,
                      linewidth  = 5.0,
                      color      = legend.name_to_color[waste],
                      **kw)

    def plot(self, **kwargs):
        # Plot every country #
        for sector, axes in zip(self.batch, self.axes):
            self.lines_plot(sector, axes)

        # Change the X labels #
        self.set_x_labels(self.label_x)

        # Change the Y labels only for the left most graph #
        self.axes[0].set_ylabel(self.label_y, fontsize=12)

        # Remove ugly box around figures #
        self.remove_frame()

        # Adjust details on the subplots #
        self.y_grid_on()

        # Add the sector name as a title #
        for batch, axes in zip(self.batch, self.axes):
            row  = nace_names.query('nace_r2 == @batch')
            text = row.iloc[0]['description']
            if len(text) > 30: text = text[:30] + ' [...]'
            axes.text(0.05, 1.05, text, transform=axes.transAxes, ha="left", size=22)

        # Prune graphs if we are shorter than n_cols #
        if len(self.batch) < self.n_cols:
            for axes in self.axes[len(self.batch):]:
                self.hide_full_axes(axes)

        # Leave some space around the graph #
        pyplot.subplots_adjust(wspace=0.2, top=0.9, left=0.04, right=0.95, bottom=0.1)
        # Save #
        self.save_plot(**kwargs)
        # Convenience: return for display in notebooks for instance #
        return self.fig

###############################################################################
class GenLegend(SoloLegend):

    # Params #
    capitalize = False

    @property_cached
    def label_to_color(self):
        """Mapping of each waste to type to colors."""
        return {
            "Paper and cardboard wastes":     'gray',
            "Rubber wastes":                  'blue',
            "Wood wastes":                    'brown',
            "Textile wastes":                 'purple',
            "Animal and mixed food waste":    'pink',
            "Vegetal wastes":                 'green',
            "Animal feces urine and manure":  'yellow',
        }

    @property_cached
    def name_to_color(self):
        return {
            'W072': 'gray',
            'W073': 'blue',
            'W075': 'brown',
            'W076': 'purple',
            'W091': 'pink',
            'W092': 'green',
            'W093': 'yellow',
        }

###############################################################################
# Every country has a several graphs (each graph has several subplots) #
countries = {c.code: GenerationViz(c) for c in all_countries}

# Create a separate standalone legend #
legend = GenLegend(base_dir = base_dir)