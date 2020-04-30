#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Typically you can use this class this like:

    >>> from waste_flow.outputs import outputs
    >>> print(outputs.make_excel())
"""

# Built-in modules #

# Internal modules #

# First party modules #
from autopaths import Path

# Third party modules #
import pandas

###############################################################################
class Outputs:
    """Takes care of creating some files that contain outputs."""

    def make_excel(self, path='~/test/dry_mass.xlsx'):
        """
        Create an excel file with one sheet per country.
        And containing the dry mass tables for each year.
        """
        # Parse path #
        path = Path(path)
        # Load #
        from waste_flow.generation import waste_gen
        df = waste_gen.dry_mass
        # Remove index #
        df = df.reset_index()
        # Create a writer #
        self.writer = pandas.ExcelWriter(str(path), engine='xlsxwriter')
        # Create a sheet per country #
        for country_code in df.country.unique():
            worksheet = self.writer.book.add_worksheet(country_code)
            self.writer.sheets[country_code] = worksheet
        # Write each country #
        groups = df.groupby(['country'])
        for code, subdf in groups: self.write_one_country(code, subdf)
        # Save #
        self.writer.save()
        # Return #
        return path

    def write_one_country(self, code, df):
        """
        Create an excel sheet with every year that a
        given country has.
        """
        # Drop #
        df = df.drop(columns='country')
        # Group by year #
        groups = df.groupby('year')
        # Initialize #
        all_dfs = []
        # Loop #
        for year, table in groups:
            table = table.drop(columns='year')
            table = table.set_index('nace_r2')
            # Names #
            table.index.name = "kilograms"
            # Append #
            all_dfs.append(("YEAR %s -- dry mass" % year, table))
        # Write all tables #
        self.one_sheet_several_df(code, all_dfs)

    def one_sheet_several_df(self, sheet_name, all_dfs):
        """
        Write several dataframes, all to the same excel sheet.
        It will append a custom title before hand for each
        dataframe.
        """
        # Get sheet #
        sheet = self.writer.sheets[sheet_name]
        # Initialize #
        row = 0
        # Loop #
        for title, df in all_dfs:
            # Write custom title #
            sheet.write_string(row, 0, title)
            row += 2
            # Write dataframe #
            df.to_excel(self.writer,
                        sheet_name = sheet_name,
                        startrow   = row,
                        startcol   = 0)
            # Increment #
            row += len(df.index) + 4
        # Return #
        return row

###############################################################################
# Create singleton #
outputs = Outputs()
