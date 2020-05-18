#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.

Typically you can use this class like this:

    >>> from waste_flow.analysis import waste_ana
    >>> print(waste_ana.summary_recovered)
"""

# Built-in modules #

# Internal modules #
from waste_flow            import cache_dir
from waste_flow.treatment  import waste_trt
from waste_flow.generation import waste_gen
from waste_flow.common     import trt_names, wastes_created, wet_coefs
from waste_flow.spreading  import spread

# First party modules #
from plumbing.cache import property_cached, property_pickled_at

# Third party modules #
import pandas

###############################################################################
class WasteAnalysis:
    """
    Here we combine the waste generation and waste treatment datasets and
    perform a custom analysis by breaking down the waste categories into
    new categories and calculating which proportion of waste ends up in which
    treatment category per activity sector.
    """

    # ----------------------------- Preparing ------------------------------- #
    @property
    def combined(self):
        """
        Starting from the waste generation dataframe, add the waste
        treatment data by performing a join on country, year and
        waste category.
        Now we have both the activity sector and the waste destinations
        combined.
        """
        # Load #
        gen = waste_gen.long_format
        trt = waste_trt.normalized
        # Join #
        df = gen.left_join(trt, on = ['country', 'year', 'waste'])
        # Return #
        return df

    @property
    def kilograms(self):
        """
        Multiply the waste total by the fraction that goes to each
        treatment destination. Also convert to kilograms which is
        the SI unit.
        """
        # Load #
        df = self.combined
        # Process #
        df['kg'] = df['tonnes'] * df['frac'] * 1000
        # Drop #
        df = df.drop(columns=['tonnes', 'frac'])
        # Return #
        return df

    # ----------------------------- Processing ------------------------------ #
    @property_pickled_at('cache_path')
    def spread_waste(self):
        """
        The eurostat original waste categories are spread into new custom
        waste categories. These categories have modified names and are divided
        into "household" categories and "industrial" categories.

        In particular, we remove the municipal waste (W101) category and
        distribute it in other categories according to specific breakdown
        proportions.
        All these proportions are described in "waste_spreading.csv".

        The municipal waste (W101) should be called as such because otherwise
        it can be confused with the "household" nace sector.
        """
        # Load dataframe #
        df = self.kilograms
        # Group #
        groups = df.groupby(['country', 'year', 'wst_oper', 'nace_r2'])
        # Apply function #
        df = groups.apply(lambda x: self.spreader(*x.name, x))
        # Return #
        return df

    @staticmethod
    def spreader(country, year, treatment, nace, subdf):
        # Load the coeffs #
        coeffs  = spread.by_nace[nace]
        # Multiply #
        wastes  = subdf.set_index('waste')['kg']
        product = coeffs * wastes
        # Replace some NaNs with zeros #
        product[coeffs == 0.0] = 0.0
        # But otherwise keep NaNs #
        summed  = product.sum(axis=1, skipna=False)
        # Return #
        return summed

    @property_cached
    def dry_mass(self):
        """
        Convert all the 'wet tonnes' values to their dry weight
        equivalent.
        """
        # Compute dry coefficients #
        dry_coef = 1 - wet_coefs
        # Multiply for dry mass #
        result = self.spread_waste * dry_coef
        # Return #
        return result

    @property
    def dry_long(self):
        """Same as above but in the long format."""
        # Load #
        df = self.dry_mass
        # Unpivot #
        df = df.reset_index()
        df = df.melt(id_vars    = ['country', 'year', 'nace_r2', 'wst_oper'],
                     value_name = 'kg_dry',
                     var_name   = 'waste')
        # Return #
        return df

    @property
    def collapse_ind(self):
        """
        Sum all nace sectors together, keeping only the <EP_HH>
        one as separate (and thus not summed).
        """
        # Load #
        df = self.dry_long
        # Split the dataset in two #
        selector = df['nace_r2'] == 'EP_HH'
        house = df[selector]
        indus = df[~selector]
        # Reset index #
        indus = indus.reset_index(drop=True)
        house = house.reset_index(drop=True)
        # Sum the industrial #
        groups = indus.groupby(['country', 'year', 'wst_oper', 'waste'])
        summed = groups.aggregate({'kg_dry': 'sum'})
        summed = summed.reset_index()
        # Create a new artificial nace that is the sum of the others #
        summed.insert(2, "nace_r2", "all_indus")
        # Put them back together #
        df = pandas.concat([summed, house])
        # Return #
        return df

    @property_cached
    def wide_format(self):
        """
        Transform the dataframe into the wide format
        With waste categories as column names.
        """
        # Load #
        df = self.collapse_ind
        # Pivot #
        df = df.pipe(pandas.pivot_table,
                     index   = ['country', 'year', 'nace_r2', 'wst_oper'],
                     columns = ['waste'],
                     values  = ['kg_dry'])
        # Only one level on the column index #
        df.columns = df.columns.droplevel()
        # Order the waste categories #
        df = df.reindex(columns=wastes_created)
        # Order the nace activities #
        df = df.sort_index(level=2, ascending=False)
        # Return #
        return df

    # ----------------------------- Reporting ------------------------------- #
    @property_cached
    def summary_recovered(self):
        """
        Produce a dataframe that summarizes the quantities of waste disposed
        and recovered, for every waste category, in the household and
        industrial categories.
        """
        # Load #
        df = self.collapse_ind
        # Pivot #
        df = df.pipe(pandas.pivot_table,
                     index   = ['country', 'year', 'nace_r2', 'waste'],
                     columns = ['wst_oper'],
                     values  = ['kg_dry'])
        # Only one level on the column index #
        df.columns = df.columns.droplevel()
        # Split into recovered and disposed #
        recovery = trt_names[trt_names['category'] == 'recovery']['treatment']
        disposal = trt_names[trt_names['category'] == 'disposal']['treatment']
        # Sum the treatment categories that belong #
        df['recovery'] = sum(df[trt] for trt in list(recovery))
        df['disposal'] = sum(df[trt] for trt in list(disposal))
        # Remove other columns #
        df = df.drop(columns=[trt for trt in trt_names['treatment']])
        # Add total #
        df['dry_mass'] = df.sum(axis=1)
        # Add wet mass #
        df['wet_mass'] = df['dry_mass'] / (1 - wet_coefs)
        # Remove lines that are all zeros #
        #df = df.query('dry_mass != 0.0')
        # Reorder columns #
        index = ['wet_mass', 'dry_mass', 'disposal', 'recovery']
        df = df.reindex(columns=index)
        # Return #
        return df

    # -------------------------------- Cache -------------------------------- #
    @property
    def cache_path(self):
        """Specify where on the file system we will pickle the property."""
        return cache_dir + 'dataframes/' + 'waste_spread.pickle'

###############################################################################
# Create singleton #
waste_ana = WasteAnalysis()
