# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Libreria dei parametri generali e di classi di parametri suddivisi per area.
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

import time
from datetime import datetime

DEBUG = True

LISTA_AZIONI_POSSIBILI = ()
LISTA_STAGIONI = (1, 2)

START_TIME = time.time()
START_DATETIME = datetime.today()
DATE_FMT = '%Y-%m-%d %H:%M:%S'
DAY_FMT = '%Y-%m-%d'

LOG_FMT = '%(asctime)s - %(filename)-8s - %(funcName)-10s - %(levelname)-10s: %(message)s'
LOGFILE_FMT = ".log"
LOGFILE_MODE = {
                "write": "w",
                "append": "a"
                }

# per ottenere il tempo intercorso dall'inizio dell'esecuzione
def get_elapsed_time(final_time):
    return str(final_time - START_TIME)


# ============================================================================ #
#### Parametri suddivisi per categorie
class BaseParameter(object):

    def __init__(self):
        pass


class ParametriWS(BaseParameter):

    def __init__(self):
        # super(ParametriWS, self).__init__(self)
        self.ws_dict = {}


class ParametriDS(BaseParameter):

    def __init__(self):
        # super(ParametriDS, self).__init__(self)

        self.lista_completa_DS = ()
        self.lista_ECI = ()
        self.lista_USA = ()
        self.lista_USA_completa = ()
        self.lista_europa = ()


class ParametriLogger(BaseParameter):

    def __init__(self):
        # super(ParametriLogger, self).__init__(self)

        self.LOGFILE_PATH = '../log/'
        self.LOGFILE_NAME = str((datetime.today().date().strftime(DAY_FMT))) + \
                            LOGFILE_FMT
        self.STREAM_PATH = ''
        self.INFO = 'INFO'
        self.DEBUG = 'DEBUG'
        self.WARNING = 'WARNING'
        self.MODE = LOGFILE_MODE["append"]
        self.fmt = LOG_FMT
        self.fmt_date = DATE_FMT

