#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.
"""

# Built-in modules #
import socket

# Internal modules #
import waste_flow

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
    def hostname(self):          return socket.gethostname()

    def git(self):
        if not waste_flow.git_repo: return False
        return {'git_hash'  : waste_flow.git_repo.hash}
