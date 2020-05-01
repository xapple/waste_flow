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

# First party modules #
from plumbing.xls_tables import MultiDataFrameXLS

# Third party modules #

###############################################################################
class Outputs:
    """Takes care of creating some files that contain outputs."""

    def make_dry_mass(self, path):
        """
        Create an excel file with one sheet per country.
        And containing the dry mass tables for each year.
        """
        # Load #
        from waste_flow.generation import waste_gen
        df = waste_gen.dry_mass
        # Remove index #
        df = df.reset_index()
        # Group per country #
        groups = df.groupby(['country'])
        # Write each country #
        sheet_to_dfs = {k: self.one_country(k,v) for k,v in groups}
        # Save #
        multi_xls = MultiDataFrameXLS(sheet_to_dfs, path)
        # Do it #
        return multi_xls()

    def one_country(self, code, df):
        """
        Create an excel sheet with every year that a
        given country has.
        """
        # Drop the country column #
        df = df.drop('country', axis=1)
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
            title = "YEAR %s -- dry mass in kg -- W101 is spread out" % year
            # Other labels #
            sheet = {
                'dataframe': table,
                'title':     title,
                'x_title':   "Waste",
                'y_title':   "Activity",
                'x_label':   None,
                'y_label':   None,
                'x_extra':   None,
                'y_extra':   None,
            }
            # Append #
            all_dfs.append(sheet)
        # Return #
        return all_dfs

###############################################################################
# Create singleton #
outputs = Outputs()
