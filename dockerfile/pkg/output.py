# -*- coding: utf-8 -*-
"""Output to stdout in docker image."""

from sys import stdout
from time import ctime

__DEBUG_PREFIX = "DEBUG"
__LOG_PREFIX = "LOG"
__WARN_PREFIX = "WARNING"
__ERROR_PREFIX = "ERROR"

LOG_LEVEL = "info"

def debug(string):
    """Debug specified data."""
    # if LOG_LEVEL == "debug":
    __write(__DEBUG_PREFIX, string)

def log(string):
    """Log specified data."""
    __write(__LOG_PREFIX, string)        

def __write( prefix, line = '' ):
  stdout.flush()
  stdout.write( ctime() + " " + prefix + ": " + line + '\n' )
  stdout.flush()