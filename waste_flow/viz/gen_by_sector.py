#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.
"""

# Built-in modules #

# Internal modules #
from waste_flow                    import cache_dir
from waste_flow.common             import nace_names
from waste_flow.country            import countries
from waste_flow.viz.gen_by_country import legend
from waste_flow.generation         import waste_gen

# First party modules #
from plumbing.graphs.multiplot import Multiplot
from plumbing.cache import property_cached

# Third party modules #
from matplotlib import pyplot

# Where to store the graphs #
base_dir = cache_dir + 'graphs/gen_by_sector/'

###############################################################################
class GenBySectorViz:
    """
    Every sector has one GenBySectorViz object containing several graphs.
    Each graph contains a fixed number of subplots.
    Each subplot corresponds to one country.
    """

    def __init__(self, sector):
        self.sector = sector

    def plot(self, *ag, **kw):
        return [graph.plot(*ag, **kw) for graph in self.all_graphs]

    @property_cached
    def df(self):
        # Load #
        df = waste_gen.wide_format
        # Reset index #
        df = df.reset_index()
        # Filter #
        df = df.query('nace_r2 == @self.sector')
        df = df.drop(columns={'nace_r2'})
        # Swap index levels #
        df = df.sort_values(['country', 'year'])
        df = df.set_index(['country', 'year'])
        # Return #
        return df

    @property_cached
    def all_graphs(self):
        # Get all countries #
        country_names = self.df.index.levels[0]
        # Sort sectors into batches of a given size #
        size    = GenSectorPlot.n_cols
        count   = len(country_names)
        batches = [country_names[i:i + size] for i in range(0, count, size)]
        # One graph per sector #
        result = [GenSectorPlot(self, batch) for batch in batches]
        # Return #
        return result

###############################################################################
class GenSectorPlot(Multiplot):

    # Basic params #
    formats    = ('pdf',)
    share_y    = False
    share_x    = False
    height     = 7
    width      = 30

    # Labels for axes #
    label_x = 'Year'
    label_y = 'Wet mass in tonnes'

    # Size of grid #
    n_rows = 1
    n_cols = 4

    def __init__(self, parent, batch):
        # Save batch #
        self.batch = batch
        # Call parent class #
        super(GenSectorPlot, self).__init__(parent, base_dir)

    @property_cached
    def short_name(self):
        return self.parent.sector + '|' + '+'.join(s for s in self.batch)

    def lines_plot(self, country, axes, **kw):
        # Load #
        df = self.parent.df
        # Filter for the current country #
        df = df.loc[[country]]
        # We don't need the country column anymore #
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
        for country, axes in zip(self.batch, self.axes):
            self.lines_plot(country, axes)

        # Change the X labels #
        self.set_x_labels(self.label_x)

        # Change the Y labels only for the left most graph #
        self.axes[0].set_ylabel(self.label_y, fontsize=12)

        # Remove ugly box around figures #
        self.remove_frame()

        # Adjust details on the subplots #
        self.y_grid_on()

        # Add the country name as a title #
        for country, axes in zip(self.batch, self.axes):
            text = countries[country].long_name
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
# Every sector has a several graphs (each graph has several subplots) #
sectors = {s: GenBySectorViz(s) for s in nace_names['nace']}