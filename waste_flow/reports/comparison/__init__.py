#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.
"""

# Built-in modules #

# Internal modules #
from waste_flow.reports.base_template import ReportTemplate
from waste_flow                       import cache_dir
from waste_flow.reports.template      import Header, Footer

# First party modules #
from plumbing.cache    import property_cached
from pymarktex         import Document
from pymarktex.figures import ScaledFigure, BareFigure
from autopaths         import Path

# Third party modules #

###############################################################################
class ComparisonReport(Document):
    """
    A report generated in PDF describing several countries.
    """

    header_template = Header
    footer_template = Footer

    def __init__(self, output_path=None):
        # Paths #
        if output_path is None:
            self.output_path = Path(cache_dir + 'reports/comparison.pdf')
        else:
            self.output_path = Path(output_path)

    @property_cached
    def template(self): return ComparisonTemplate(self)

    def load_markdown(self): self.markdown = str(self.template)

###############################################################################
class ComparisonTemplate(ReportTemplate):
    """All the parameters to be rendered in the markdown template."""

    delimiters = (u'{{', u'}}')

    def __repr__(self):
        return '<%s object on %s>' % (self.__class__.__name__, self.parent)

    def __init__(self, parent):
        self.parent = parent
        self.report = parent

    #-------------------------------- XXXX -----------------------------------#
    def comp_total_area(self):
        # Caption #
        caption = "XXXX"
        # Import #
        from waste_flow.viz.area_comp import all_graphs, legend
        # Initialize #
        result = ""
        # Loop every country batch #
        for graph in all_graphs: result += str(BareFigure(graph=graph)) + '\n\n'
        # Add the legend #
        result += str(ScaledFigure(graph   = legend,
                                   caption = caption,
                                   label   = 'xxxx',
                                   width   = '9em'))
        # Return #
        return result

###############################################################################
# Create singleton #
report = ComparisonReport()
