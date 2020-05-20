#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.
"""

# Built-in modules #

# Internal modules #
from waste_flow         import cache_dir
from waste_flow.country import all_countries
from waste_flow.common  import waste_names_ind, waste_names_hh

# First party modules #
from plumbing.graphs             import Graph
from plumbing.cache              import property_cached
from plumbing.graphs.solo_legend import SoloLegend

# Third party modules #
from matplotlib import pyplot
import pandas

# Where to store the graphs #
base_dir = cache_dir + 'graphs/summary/'

###############################################################################
class SummaryGraph(Graph):
    """
    Every country has two SummaryGraph objects.
    One for industrial activities, one for household activities.
    The values indicate dry mass in kilograms.
    """

    # Basic params #
    formats    = ('pdf',)
    height     = 5
    width      = 13
    y_grid     = True

    # Labels for axes #
    x_label = 'Year'
    y_label = 'Dry mass in kilograms'

    def __init__(self, country, category):
        # Basic attributes #
        self.country    = country
        self.category   = category
        self.short_name = country.code + '_' + category
        # Nace filter #
        if self.category == 'industrial': self.nace_r2 = 'all_indus'
        if self.category == 'household':  self.nace_r2 = 'EP_HH'
        # Waste suffix #
        if self.category == 'industrial': self.waste_names = waste_names_ind
        if self.category == 'household':  self.waste_names = waste_names_hh
        # Waste filter #
        self.wastes = self.waste_names['waste']
        # Colors #
        self.colors = dict(self.waste_names.set_index('waste')['plot_color'])
        # Call parent #
        super().__init__(country, base_dir)

    @property_cached
    def df(self):
        # Load #
        df = self.country.summary_recovered
        # Filter for the current nace activity group #
        df = df.query("nace_r2 == @self.nace_r2")
        # Filter for the current waste group #
        df = df.query("waste in @self.wastes")
        # Take only the dry_mass column #
        df = df[['dry_mass']]
        # Swap index levels #
        df = df.reset_index()
        df = df.drop(columns=['nace_r2'])
        # Pivot #
        df = df.pipe(pandas.pivot_table,
                     index   = ['year'],
                     columns = ['waste'],
                     values  = ['dry_mass'])
        # Only one level on the column index #
        df.columns = df.columns.droplevel()
        # Return #
        return df

    def plot(self, **kwargs):
        # Make figure #
        fig  = pyplot.figure()
        axes = fig.add_subplot(111)
        # Plot every line #
        for waste in self.wastes:
            if waste not in self.df.columns: continue
            axes.plot(self.df[waste],
                      marker     = ".",
                      markersize = 20.0,
                      linewidth  = 5.0,
                      color      = self.colors[waste])
        # Leave some space around the graph #
        #pyplot.subplots_adjust(wspace=0.2, top=0.9, left=0.04, right=0.95, bottom=0.1)
        # Save #
        self.save_plot(**kwargs)
        # Convenience: return for display in notebooks for instance #
        return fig

###############################################################################
class SummaryLegend(SoloLegend):

    def __init__(self, category):
        # Basic attributes #
        self.category = category
        # Name #
        self.short_name = 'legend_' + category
        # Waste suffix #
        if self.category == 'industrial': self.waste_names = waste_names_ind
        if self.category == 'household':  self.waste_names = waste_names_hh
        # Index #
        self.waste_names = self.waste_names.set_index('waste')
        # Colors #
        self.name_to_color = dict(self.waste_names['plot_color'])
        # Call parent #
        super().__init__(base_dir=base_dir)

    @property_cached
    def label_to_color(self):
        """Mapping of each waste to type to colors."""
        df = self.waste_names.reset_index()
        df = df.set_index('full_name')
        return dict(df['plot_color'])

###############################################################################
# Every country has a several graphs (each graph has several subplots) #
countries_ind = {c.code: SummaryGraph(c, 'industrial') for c in all_countries}
countries_hh  = {c.code: SummaryGraph(c, 'household')  for c in all_countries}

# Create separate standalone legends #
legend_ind = SummaryLegend('industrial')
legend_hh  = SummaryLegend('household')