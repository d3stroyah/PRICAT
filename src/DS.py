#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Classe DepartmentStore.

Descrive il comportamento di ogni classe di DS. Ogni tipologia e' descritta in
una sottoclasse a parte, contenente tutti i metodi necessari alla formattazione
dei file dei cataloghi
"""


import lib_data
import lib_parametri
import lib_utility
import lib_ws

class DSObject(object):

    def __init__(self, nome, annos):
        self._nome = nome
        # check su formato anno+stagione
        assert((len(str(annos).strip()) == 5) and (int(annos))), \
               "Parametro 'annos' invalido"
        self._annos = annos
        self._anno = str(annos[:-1])
        self._stagione = str(annos[-1])
        self._lclienti = []
        self._lsocieta = []
        self._lfiles = []

    ############# FUNZIONI BASE
    def format_CABPRI(self, content):
        """Formattazione generale di CABPRI"""
        pass

    def format_GRUPRI(self, content):
        """Formattazione generale di GRUPRI"""
        pass

    def format_LINPRI(self, content):
        """Formattazione generale di LINPRI"""
        pass

    ############# GETITEM e RAPPRESENTAZIONI
    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self):
        l_str = []
        l_str.append('DS: ')
        l_str.append('(tipo_DS => %(whatami)s)' % self)
        l_str.append('(nome => %(_nome)s)' % self)
        l_str.append('(anno => %(_anno)s)' % self)
        l_str.append('(stagione => %(_stagione)s)' % self)
        l_str.append('(lclienti => %(_lclienti)s)' % self)
        l_str.append('(lsocieta => %(_lsocieta)s)' % self)
        return '\n\t'.join(l_str)

    def __repr__(self):
        return "%s" % self.__class__

    ############# SETTER, GETTER e PROPERTIES
    def get_whatami(self):
        return self.__class__.__name__.replace("DepartmentStore", "")

    def get_nome(self):
        return self._nome
    def set_nome(self, value):
        # check se value in lista DS completa
        self._nome = value

    def get_annos(self):
        return self._annos
    def set_annos(self, value):
        assert((len(str(value).strip()) == 5) and (int(value))), \
            "Parametro 'annos' invalido"
        self._annos = value

    def get_anno(self):
        return self._anno

    def get_stagione(self):
        return self._stagione

    def get_lclienti(self):
        return self._lclienti
    def set_lclienti(self, value):
        self._lclienti = value

    def get_lsocieta(self):
        return self._lsocieta
    def set_lsocieta(self, value):
        self._lsocieta = value

    def get_lfiles(self):
        return self._lfiles
    def set_lfiles(self, value):
        self._lfiles = value

    whatami = property(get_whatami)
    nome = property(get_nome, set_nome)
    annos = property(get_annos, set_annos)
    anno = property(get_anno)
    stagione = property(get_stagione)
    lclienti = property(get_lclienti, set_lclienti)
    lsocieta = property(get_lsocieta, set_lsocieta)
    lfiles = property(get_lfiles, set_lfiles)

    ############# CLASSI DERIVATE


# =========================================================================== #
class GeneraleDepartmentStore(DSObject):
    """
    Classe di gestione pubblicazioni per DS generale (in assenza di
    casi particolari)
    """

    def __init__(self, nome, annos):
        super(GeneraleDepartmentStore, self).__init__(nome, annos)

# =========================================================================== #


# =========================================================================== #
class ECIDepartmentStore(DSObject):
    """Classe di gestione pubblicazioni per DS ECI_PORTOGALLO"""

    def __init__(self, nome, annos):
        super(ECIDepartmentStore, self).__init__(nome, annos)

# =========================================================================== #


# =========================================================================== #
class ECIPortoDepartmentStore(DSObject):
    """Classe di gestione pubblicazioni per DS ECI_PORTOGALLO"""

    def __init__(self, nome, annos):
        super(ECIPortoDepartmentStore, self).__init__(nome, annos)

# =========================================================================== #


# =========================================================================== #
class USADepartmentStore(DSObject):
    """Classe di gestione pubblicazioni per DS USA"""

    def __init__(self, nome, annos, completo=True):
        super(USADepartmentStore, self).__init__(nome, annos)

# =========================================================================== #


# =========================================================================== #
class OEDepartmentStore(DSObject):
    """Classe di gestione pubblicazioni per DS PEEK, RINA e COIN"""

    def __init__(self, nome, annos):
        super(OEDepartmentStore, self).__init__(nome, annos)

# =========================================================================== #


################ TEST FUNCTION
def test():
    eci_ds = ECIDepartmentStore("eci", "20142")
    eci_porto_ds = ECIPortoDepartmentStore("eci_porto", "20142")

    print(eci_ds)
    print(eci_porto_ds)


# =========================================================================== #
# =========================================================================== #
# =========================================================================== #
if __name__ == '__main__':
    test()