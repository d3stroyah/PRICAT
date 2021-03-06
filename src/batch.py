#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Batch di gestione della stesura e dell'esportazione dei cataloghi via FTP a
EDICOM.

Utilizzo:
    $ ./batch.py [-h] [-DS Department Store] [-action Azione]
                 [-societa Societa Gruppo] [-anno Anno capo]
                 [-stagione Stagione capo]

In caso di mancanza di comandi necessari all'esecuzione, il batch solleva
un'eccezione e termina l'esecuzione.
"""


import sys
import os
import time
import datetime
import argparse
import logging
import collections
import logging.handlers

import lib_data
import lib_parametri
import lib_utility
import lib_ws
from lib_utility import timeit

parser = argparse.ArgumentParser()
parser.add_argument("-DS", "-DepartmentStore", 
                    help="Specifica il Department Store")
parser.add_argument("-action", help="Azione da effettuare")
parser.add_argument("-societa", help="Societa di provenienza capo")
parser.add_argument("-anno", help="Anno di riferimento")
parser.add_argument("-stagione", help="Stagione di riferimento")
args = parser.parse_args()

# considero tutte le variabili in minuscolo (scelta arbitraria per avere 
# consistenza in seguito)
SOCIETA = str(args.societa).upper()  # per consistenza con quanto esistente
ACTION = str(args.action).lower()
DS = str(args.DS).lower()
ANNO = str(args.anno).lower()
STAGIONE = str(args.stagione).lower()
# ============================================================================ #


# ============================================================================ #
@timeit
def main():
    """
    Programma di generazione ed esportazione cataloghi,
    chiamato da riga di comando.

    In caso di mancanza di comandi necessari all'esecuzione, 
    il batch solleva un'eccezione e termina l'esecuzione.
    """
    start_time = datetime.datetime.now()
    logger = lib_utility.get_logger()
    logger.info("=" * 80)
    logger.info(
        "Starting execution at: " + start_time.strftime(lib_parametri.DATE_FMT))

    # Gestione macro casi di azione:
    if DS:
        pass
        # gestione societa
    else:
        if ACTION == 'pubblica':
            pass
        elif ACTION == 'pubblica_usa':
            pass
        elif ACTION == 'pubblica_ordrsp':
            pass
        elif ACTION == 'schedulato':
            pass
        elif ACTION == 'usa_completo':
            pass
        elif ACTION == 'delete_inovis':
            pass
        elif ACTION == 'sconti_eci':
            pass
        else:
            pass  # raise # se i parametri non vanno bene: raise

    final_time = datetime.datetime.now()
    logger.info(
        "Execution ended at: " + final_time.strftime(lib_parametri.DATE_FMT))
    logger.info("Elapsed time: " + str(final_time - start_time))
    logger.info("=" * 80 + "\n")

if __name__ == '__main__':
    main()
