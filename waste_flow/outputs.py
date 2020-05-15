#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Typically you can use this class this like:

    >>> from waste_flow.outputs import outputs
    >>> print(outputs.make_dry_mass())
"""

# Built-in modules #

# Internal modules #
from waste_flow import cache_dir
from waste_flow.country import all_countries

# First party modules #
from plumbing.xls_tables import MultiDataFrameXLS

# Third party modules #

###############################################################################
class Outputs:
    """Takes care of creating some files that contain outputs."""

    # ----------------------------- Properties ------------------------------ #
    @property
    def path(self):
        """Specify where on the file system we will pickle the property."""
        return cache_dir + 'outputs/' + self.short_name + '.xlsx'

    # ------------------------------ Methods -------------------------------- #
    def __call__(self):
        """
        Create an excel file with one sheet per country.
        """
        # Write each country #
        sheet_to_dfs = {c.code: self.one_country(c) for c in all_countries}
        # Save #
        multi_xls = MultiDataFrameXLS(sheet_to_dfs, self.path)
        # Do it #
        return multi_xls()

    def one_country(self, country):
        """
        Create an excel sheet with every year that a
        given country has.
        """
        # Get the dataframe #
        df = getattr(country, self.df_name)
        df = df.reset_index()
        # Group by year #
        groups = df.groupby('year')
        # Initialize #
        all_dfs = []
        # Loop #
        for year, table in groups:
            # Drop the year column #
            table = table.drop('year', axis=1)
            table = table.set_index('nace_r2')
            # Main title #
            title = "YEAR %s" % year
            # Other optional labels #
            sheet = {
                'dataframe': table,
                'title':     title,
                'x_title':   getattr(self, 'x_title', None),
                'y_title':   getattr(self, 'y_title', None),
                'x_label':   getattr(self, 'x_label', None),
                'y_label':   getattr(self, 'y_label', None),
                'x_extra':   getattr(self, 'x_extra', None),
                'y_extra':   getattr(self, 'y_extra', None),
            }
            # Append #
            all_dfs.append(sheet)
        # Return #
        return all_dfs

###############################################################################
class WasteBreakdown(Outputs):
    short_name = "waste_breakdown"
    df_name    = "wide_format"
    x_title    = "Custom Waste Categories (values are kilograms)"
    y_title    = "Nace"

class SummaryRecovered(Outputs):
    short_name = "summary_recovered"
    df_name    = "summary_recovered"
    x_title    = "Summary (values are kilograms)"
    y_title    = "Nace"

###############################################################################
# Create singletons #
waste_breakdown   = WasteBreakdown()
summary_recovered = SummaryRecovered()
