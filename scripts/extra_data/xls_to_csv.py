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

# Third party modules #
import pandas

# Internal modules #
from waste_flow import module_dir

# Constants #
convert_pairs = (('extra_data_xls/nace_to_full_name.xlsx',  'extra_data_csv/'),
                 ('extra_data_xls/waste_to_full_name.xlsx', 'extra_data_csv/'))

###############################################################################
class ConvertExcelToCSV:
    """
    Will convert an excel file into its CSV equivalent.
    """

    def __init__(self, source, dest, **kwargs):
        # Record attributes #
        self.source = Path(source)
        self.dest   = Path(dest)
        self.kwargs = kwargs
        # Check directory case #
        if self.dest.endswith('/'):
            self.dest = self.dest + self.source.filename
            self.dest = self.dest.replace_extension('csv')

    def __call__(self):
        data_xls = pandas.read_excel(str(self.source))
        data_xls.to_csv(str(self.dest), **self.kwargs)

###############################################################################
if __name__ == '__main__':
    for pair in convert_pairs:
        source, dest = module_dir + pair[0], module_dir + pair[1]
        converter = ConvertExcelToCSV(source, dest, index=False)
        converter()