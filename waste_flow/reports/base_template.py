#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.
"""

# Built-in modules #
import os, socket

# Internal modules #
import waste_flow
from waste_flow.country import all_codes

# First party modules #
from pymarktex.templates import Template
from plumbing.common     import pretty_now

###############################################################################
class ReportTemplate(Template):
    """Things that are common to most reports in waste_flow."""

    def project_name(self):      return waste_flow.project_name
    def project_url(self):       return waste_flow.project_url
    def project_version(self):   return waste_flow.__version__
    def now(self):               return pretty_now()

    def hostname(self):
        host = os.environ.get('WASTE_FLOW_HOSTNAME')
        if host is not None: return host
        return socket.gethostname()

    def git(self):
        if not waste_flow.git_repo: return False
        return {'git_hash'  : waste_flow.git_repo.hash}

    def country_list(self):
        aggregates = ['EU27_2020', 'EU28']
        countries  = [c for c in all_codes if c not in aggregates]
        msg = "%s as well as %s which represent aggregates."
        return msg % (', '.join(countries), ', '.join(aggregates))