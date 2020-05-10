#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Development script to generate an empty version of the
"waste_spreading.xlsx" excel file.

Typically you would run this file from a command line like this:

     ipython3 -i -- ~/deploy/waste_flow/scripts/make_spread_xls.py
"""

# Built-in modules #

# First party modules #
from autopaths import Path

# Third party modules #
import pandas

# Internal modules #

###############################################################################
class SpreadExcelMaker:
    """
    Takes several dataframes and writes them to an XLS file.
    The dataframes are spread through different work sheets.
    """

    def __init__(self, path):
        self.path = Path(path)

    def __call__(self):
        """
        Write several dataframes, to several excel sheets.
        """
        # Create a writer #
        self.writer = pandas.ExcelWriter(str(self.path), engine='xlsxwriter')
        # Create a sheet per every key #
        for key in self.sheet_to_dfs:
            worksheet = self.writer.book.add_worksheet(key)
            self.writer.sheets[key] = worksheet
        # Write each sheet #
        for key in self.sheet_to_dfs: self.write_one_sheet(key)
        # Save #
        self.writer.save()
        # Return #
        return self.path

    def write_one_sheet(self, key):
        """
        Write several dataframes, all to the same excel sheet.
        It will append a custom title before hand for each
        dataframe.
        """
        # Get sheet #
        sheet = self.writer.sheets[key]
        # Get dataframes #
        all_dfs = self.sheet_to_dfs[key]
        # Initialize #
        row = 0
        # Loop #
        for info in all_dfs:
            # Get dataframe #
            df = info['dataframe']
            # Write custom title #
            sheet.write_string(row, 0, info.get('title', ''))
            row += 2
            # Add extras #
            df.index.name   = info.get('y_extra', '')
            df.columns.name = info.get('x_extra', '')
            # Add Y labels #
            title, label = info.get('y_title', ''), info.get('y_label', '')
            df = pandas.concat({title: df}, names=[label])
            # Add X labels #
            title, label = info.get('x_title', ''), info.get('x_label', '')
            df = pandas.concat({title: df}, names=[label], axis=1)
            # Write dataframe #
            df.to_excel(self.writer,
                        sheet_name = key,
                        startrow   = row,
                        startcol   = self.indentation)
            # Increment #
            row += len(df.index) + self.spacing

###############################################################################
if __name__ == '__main__':
    maker = SpreadExcelMaker('~/test/waste_spreading.xlsx')
    maker()