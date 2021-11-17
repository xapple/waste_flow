#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Script to convert the extra data excel files into their CSV equivalents.

Typically you would run this file from a command line like this:

     ipython3 -i -- ~/deploy/waste_flow/scripts/extra_data/convert_all_xls_to_csv.py
"""

# Built-in modules #

# First party modules #
from plumbing.xls_tables import ConvertExcelToCSV

# Third party modules #

# Internal modules #
from waste_flow import module_dir

###############################################################################
# Constants #
convert_pairs = (
    ('extra_data_xls/nace_to_full_name.xlsx',      'extra_data_csv/'),
    ('extra_data_xls/waste_to_full_name.xlsx',     'extra_data_csv/'),
    ('extra_data_xls/treatment_to_full_name.xlsx', 'extra_data_csv/'),
    ('extra_data_xls/waste_spreading.xlsx',        'extra_data_csv/')
)

if __name__ == '__main__':
    for pair in convert_pairs:
        source, dest = module_dir + pair[0], module_dir + pair[1]
        converter = ConvertExcelToCSV(source, dest, index=False)
        converter()
