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

###############################################################################
class ConvertExcelToCSV:
    """
    Lorem ipsum
    """

    def __init__(self, path):
        self.path = Path(path)

    def __call__(self):
        pass

###############################################################################
if __name__ == '__main__':
    converter = ConvertExcelToCSV('~/test/waste_spreading.xlsx')
    converter()