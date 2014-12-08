#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Libreria di utility utilizzate nel programma.
"""

# ============================================================================ #
__author__ = "Pietro Mascolo"
__copyright__ = "Copyright 2014, Energee3"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pietro Mascolo"
__email__ = "pietro@mascolo.eu"
__status__ = "Development"
# ============================================================================ #

import os
import sys
import logging
import logging.handlers

import lib_parametri
import lib_data
import lib_ws


# CREAZIONE DEL LOGGER
def getLogger(name='main'):
    """Genera un logger globale per il batch"""
    logger = logging.getLogger(name)

    log_param = lib_parametri.ParametriLogger()
    # if logger 'name' already exists, return it to avoid logging duplicate
    # messages by attaching multiple handlers of the same type
    if logger.handlers:
        return logger
    # if logger 'name' does not already exist, create it and attach handlers
    else:
        logger.setLevel(log_param.INFO)
        fmt = log_param.fmt
        fmt_date = log_param.fmt_date
        formatter = logging.Formatter(fmt, fmt_date)

        # stream handler visualizzazione console
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        # file handler: file di log
        file_handler = logging.FileHandler(log_param.LOGFILE_PATH +
                                           log_param.LOGFILE_NAME,
                                           mode=log_param.MODE)
        file_handler.setFormatter(formatter)

        logger.addHandler(handler)
        # logger.addHandler(file_handler)  # per ora uso solo lo stream

    if logger.name == 'main':
        logger.warning('Running: %s %s',
                       os.path.basename(sys.argv[0]),
                       ' '.join(sys.argv[1:]))
    return logger