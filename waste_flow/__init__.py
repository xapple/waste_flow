#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.

JRC Biomass Project.
Unit D1 Bioeconomy.
"""

# Special variables #
__version__ = '1.1.9'

# Built-in modules #
import os, sys

# First party modules #
from autopaths    import Path
from plumbing.git import GitRepo

# Constants #
project_name  = 'waste_flow'
project_url   = 'https://github.com/xapple/waste_flow'

# Get paths to module #
self       = sys.modules[__name__]
module_dir = Path(os.path.dirname(self.__file__))

# The repository directory #
repos_dir = module_dir.directory

# The module is maybe in a git repository #
git_repo = GitRepo(repos_dir, empty=True)

# Determine where to cache things #
env_var_name = "WASTE_FLOW_CACHE"

# If it is specified by user #
if env_var_name in os.environ:
    cache_dir = os.environ[env_var_name]
    if not cache_dir.endswith('/'): cache_dir += '/'

# If it is not specified by user #
else:
    import tempfile
    cache_dir = tempfile.gettempdir() + '/waste_flow/'
    import warnings
    message = ("\n\n The cache location for waste_flow's data is not defined in"
               " the '%s' environment variable.\n In this case it will default"
               " to:\n\n '%s',\n which might lead to re-caching after every reboot.\n")
    message = message % (env_var_name, cache_dir)
    warnings.warn(message)

# Monkey patch pandas library #
import plumbing.pandas_patching