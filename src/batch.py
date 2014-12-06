import sys
import os
import argparse
import logging
import collections
import logging.handlers

#================================================================================#
# genera un parser dei parametri nominali da riga di comando
# il comando puo essere passato in forma:
# $ ./batch -DS [DS] -action [action] -societa[societa] -anno[anno] 
#           -stagione [stagione]
#
# i parametri non sono posizionali e sono facoltativi
# si deve gestire la presenza di tutti i segnali necessari
#================================================================================#
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
#================================================================================#


#================================================================================#
# CREAZIONE DEL LOGGER
def getLogger(name='main', loglevel='INFO'):
    """Genera un logger globale per il batch"""  
    logger = logging.getLogger(name)

    # if logger 'name' already exists, return it to avoid logging duplicate
    # messages by attaching multiple handlers of the same type
    if logger.handlers:
        return logger
    # if logger 'name' does not already exist, create it and attach handlers
    else:
    # set logLevel to loglevel or to INFO if requested level is incorrect
        loglevel = getattr(logging, loglevel.upper(), logging.INFO)
        logger.setLevel(loglevel)
        fmt = '%(asctime)s - %(filename)-8s - %(funcName)-10s - %(levelname)-10s: %(message)s'
        fmt_date = '%Y-%m-%d %T %Z'
        formatter = logging.Formatter(fmt, fmt_date)
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    if logger.name == 'main':
        logger.warning('Running: %s %s',
                       os.path.basename(sys.argv[0]),
                       ' '.join(sys.argv[1:]))
    return logger



#================================================================================#
def main():
    """Batch di gestione invio cataloghi 
    Utilizzo: 
    $ ./batch.py [-h] [-DS Department Store] [-action Azione] 
                 [-societa Societa Gruppo] [-anno Anno capo] 
                 [-stagione Stagione capo]
    
    In caso di mancanza di comandi necessari all'esecuzione, 
    il batch solleva un'eccezione e termina l'esecuzione.
    """

    logger = getLogger()
    #logger.info("ciao")
    #logger.debug("asd")
    #logger.critical("asdasd")

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
            pass#raise # se i parametri non vanno bene solleviamo un'eccezione


if __name__ == '__main__':
    main()
