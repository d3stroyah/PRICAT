##Costanti globali
import time
from datetime import datetime

DEBUG = True

LISTA_AZIONI_POSSIBILI = ()
LISTA_STAGIONI = (1, 2)

START_TIME = time.time()
START_DATETIME = datetime.today()


# per ottenere il tempo intercorso dall'inizio dell'esecuzione
def get_elapsed_time(final_time):
    return str(final_time - START_TIME)



#### Parametri suddivisi per categorie
class BaseParameter(object):

    def __init__(self):
        pass


class ParametriWS(BaseParameter):

    def __init__(self):
        super(ParametriWS, self).__init__(self)
        self.ws_dict = {}


class ParametriDS(BaseParameter):

    def __init__(self):
        super(ParametriDS, self).__init__(self)

        self.lista_completa_DS = ()
        self.lista_ECI = ()
        self.lista_USA = ()
        self.lista_USA_completa = ()
        self.lista_europa = ()


class ParametriLogger(BaseParameter):
    def __init__(self):
        super(ParametriLogger, self).__init__(self)

        self.LOGFILE_PATH = ''
        self.STREAM_PATH = ''
        self.LEVEL = ''

