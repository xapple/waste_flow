#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Script to convert the extra data excel files into their CSV equivalents.

Typically you would run this file from a command line like this:

     ipython3 -i -- ~/deploy/waste_flow/scripts/extra_data/xls_to_csv.py
"""

# Built-in modules #

# First party modules #
from autopaths import Path
from plumbing.cache import property_cached

# Third party modules #
import pandas, xlrd

# Internal modules #
from waste_flow import module_dir

# Constants #
convert_pairs = (('extra_data_xls/nace_to_full_name.xlsx',      'extra_data_csv/'),
                 ('extra_data_xls/waste_to_full_name.xlsx',     'extra_data_csv/'),
                 ('extra_data_xls/treatment_to_full_name.xlsx', 'extra_data_csv/'),
                 ('extra_data_xls/waste_spreading.xlsx',        'extra_data_csv/'))

###############################################################################
class ConvertExcelToCSV:
    """
    Will convert an excel file into its CSV equivalent.
    """

    def __init__(self, source_path, dest_path, **kwargs):
        # Record attributes #
        self.source = Path(source_path)
        self.dest   = Path(dest_path)
        # Keep the kwargs too #
        self.kwargs = kwargs
        # Check directory case #
        if self.dest.endswith('/'):
            self.dest = self.dest + self.source.filename
            self.dest = self.dest.replace_extension('csv')

    def __call__(self):
        """Are we mono or multi sheet?"""
        if len(self.handle.sheet_names) > 1: self.multi_sheet()
        else:                                self.mono_sheet()

    @property_cached
    def handle(self):
        """Pandas handle to the excel file."""
        return pandas.ExcelFile(str(self.source))

    def mono_sheet(self):
        """Supports only one work sheet per file."""
        xls = pandas.read_excel(str(self.source))
        xls.to_csv(str(self.dest), **self.kwargs)

    def multi_sheet(self):
        """
        Supports multiple work sheets per file.
        Will concatenate sheets together by adding an extra column
        containing the original sheet name.
        """
        # Initialize #
        all_sheets = []
        # Loop #
        for name in self.handle.sheet_names:
            sheet = self.handle.parse(name)
            sheet.insert(0, "nace", name)
            all_sheets.append(sheet)
        # Write #
        df = pandas.concat(all_sheets)
        df.to_csv(str(self.dest), **self.kwargs)

###############################################################################
if __name__ == '__main__':
    for pair in convert_pairs:
        source, dest = module_dir + pair[0], module_dir + pair[1]
        converter = ConvertExcelToCSV(source, dest, index=False)
        converter()
