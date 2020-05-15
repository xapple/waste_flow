#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

These contains the tests to be run automatically with the pytest
executable. To run all the tests just type the following on your
terminal:

    $ python3 -m pip install --upgrade --user pytest
    $ pytest
"""

# Built-in modules #

# Internal modules #

# First party modules #

# Third party modules #
import pytest

###############################################################################
# --------------------------------- Import ---------------------------------- #
def test_package_import():
    import waste_flow
    return waste_flow

###############################################################################
# -------------------------------- Download --------------------------------- #
@pytest.mark.skip(reason="Takes too long to download."
                         "Don't want to spam eurostat.")
def test_gen_download():
    from waste_flow.zip_files import waste_gen
    return waste_gen.refresh_cache()

@pytest.mark.skip(reason="Takes too long to download."
                         "Don't want to spam eurostat.")
def test_trt_download():
    from waste_flow.zip_files import waste_trt
    return waste_trt.refresh_cache()

###############################################################################
# ------------------------------- Zip files --------------------------------- #
def test_gen_parsing():
    from waste_flow.zip_files import waste_gen
    del waste_gen.processed_csv
    return waste_gen.processed_csv

def test_trt_parsing():
    from waste_flow.zip_files import waste_trt
    del waste_trt.processed_csv
    return waste_trt.processed_csv

###############################################################################
# -------------------------------- Datasets --------------------------------- #
def test_gen_dataset():
    from waste_flow.generation import waste_gen
    return waste_gen.wide_format

def test_trt_dataset():
    from waste_flow.treatment import waste_trt
    return waste_trt.normalized

###############################################################################
# -------------------------------- Analysis --------------------------------- #
def test_spread():
    from waste_flow.analysis import waste_ana
    del waste_ana.spread_waste
    return waste_ana.spread_waste

def test_summary():
    from waste_flow.analysis import waste_ana
    return waste_ana.summary_recovered