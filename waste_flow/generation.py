#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Typically you can use this class this like:

    >>> from waste_flow.generation import waste_gen
    >>> print(waste_gen.dry_mass)
"""

# Built-in modules #

# Internal modules #
from waste_flow           import module_dir, cache_dir
from waste_flow.spreading import spread
from waste_flow.zip_files import waste_gen as orig_gen

# First party modules #
from plumbing.cache import property_pickled_at
from plumbing.cache import property_cached

# Third party modules #
import pandas

###############################################################################
class WasteGeneration:

    # ----------------------------- Formatting ------------------------------ #
    @property
    def filtered(self):
        """Filter the dataframe some more."""
        # Load #
        df = orig_gen.df
        # Filter for only the waste categories we are interested in #
        from waste_flow.common import wastes_selected
        df = df.query("waste in @wastes_selected")
        # Filter for only the nace categories we are interested in #
        from waste_flow.common import nace_selected
        df = df.query("nace_r2 in @nace_selected")
        # Return #
        return df

    @property
    def long_format(self):
        """
        Transform the dataframe into the long format
        (and not the wide format).
        """
        # Load #
        df = self.filtered
        # Get categorical columns #
        id_vars = [name for name, kind in df.dtypes.items() if kind == object]
        # Unpivot #
        df = df.melt(id_vars=id_vars, value_name='tonnes', var_name='year')
        # Sort by country then by year etc. #
        columns_order = ['country', 'year', 'nace_r2', 'waste']
        df = df[columns_order + ['tonnes']]
        df = df.sort_values(columns_order)
        # Return #
        return df

    @property
    def wide_format(self):
        """
        Transform the dataframe into the wide format
        (and not the long format).
        With waste categories as column names.
        """
        # Load #
        df = self.long_format
        # Pivot #
        df = df.pipe(pandas.pivot_table,
                     index   = ['country', 'year', 'nace_r2'],
                     columns = ['waste'],
                     values  = ['tonnes'])
        # Return #
        return df

    # ----------------------------- Processing ------------------------------ #
    @property_pickled_at('cache_path')
    def spread_waste(self):
        """
        The eurostat original waste categories are spread into new custom
        waste categories. These categories have modified names and are divided
        into "household" categories and "industrial" categories.

        In particular, we remove the municipal waste category and distribute it
        in other categories according to specific breakdown proportions.
        All these proportions are described in "waste_spreading.csv".

        The municipal waste (W101) should be called as such because otherwise
        it can be confused with the "household" nace sector.
        """
        # Load dataframe #
        df = self.long_format
        # Group #
        groups = df.groupby(['country', 'year', 'nace_r2'])
        # Function #
        def spreader(country, year, nace, group):
            coeffs = spread.by_nace[nace]
            group  = group.set_index('waste')
            wastes = group['tonnes'] * coeffs
            summed = wastes.sum(axis=1)
            1/0
            return summed
        # Apply function #
        df = groups.apply(lambda x: spreader(*x.name, x))
        # Return #
        return df

    @property_cached
    def dry_mass(self):
        """
        Convert all the 'wet tonnes' values to their dry weight
        equivalent in kilograms.
        """
        # Load dry wet coefficients #
        dry_coef = module_dir + 'extra_data/dry_weight_coef.csv'
        dry_coef = pandas.read_csv(str(dry_coef), index_col=0)
        dry_coef = 1 - dry_coef.fraction
        # Load dataframe #
        df = self.spread_muni.copy()
        # Multiply for dry mass #
        df *= dry_coef
        # Multiply for tonnes to kg #
        df *= 1000
        # Return #
        return df

    @property
    def dry_long(self):
        """Same as above but in the long format."""
        # Load #
        df = self.dry_mass
        df = df.reset_index()
        df = df.melt(id_vars=['country', 'year', 'nace_r2'], value_name='tonnes', var_name='waste')
        # Return #
        return df

    #--------------------------------- Cache ---------------------------------#
    @property
    def cache_path(self):
        """Specify where on the file system we will pickle the property."""
        return cache_dir + 'dataframes/' + 'waste_spread.pickle'

###############################################################################
# Create singleton #
waste_gen = WasteGeneration()
