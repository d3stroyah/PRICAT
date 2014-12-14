#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Libreria di utility utilizzate nel programma.
"""


import os
import sys
import logging
import logging.handlers

import lib_parametri
import lib_data
import lib_ws


# CREAZIONE DEL LOGGER
def get_logger(name='main'):
    """Genera un logger globale per il batch
    :param name: nome del logger
    :type name: str
    :returns: logger with double handler (stream + file)
    :rtype: logging.Logger
    """
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
        logger.addHandler(file_handler)  # per ora uso solo lo stream

    if logger.name == 'main':
        logger.warning('Running: %s %s',
                       os.path.basename(sys.argv[0]),
                       ' '.join(sys.argv[1:]))
    return logger

import time


def timeit(method):
    """Wrapper per misurare il tempo di esecuzione di una funzione/metodo
     :param method: function
     :returns decorated function
    """
    def timed(*args, **kw):
        """
        Funzione interna di cui misurare il tempo di esecuzione
        :param args: list
        :param kw: dict
        :return: result
        """
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        logger = get_logger()
        logger.info(
            ' %r executed, args: (%r, %r). Execution time: %2.2f sec' %
            (method.__name__, args, kw, te - ts))
        #print '%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te-ts)
        return result

    return timed
