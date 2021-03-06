# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, DestinationsSearch
from membro_app.model import Membro

#here
class ListMembroDeCelula(DestinationsSearch):
    def __init__(self, celula):
        super(ListMembroDeCelula, self).__init__(celula)

    def do_business(self):
        super(ListMembroDeCelula, self).do_business()
        self.result = [e for e in self.result if e != None]


class MembroPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Membro
    _include = [Membro.celular, 
                Membro.email, 
                Membro.nome,
                Membro.celulaNome]


class MembroForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Membro
    _include = [Membro.celular, 
                Membro.email, 
                Membro.nome,
                Membro.celulaNome]


class MembroDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Membro
    _include = [Membro.nome, 
                Membro.creation, 
                Membro.email, 
                Membro.celular,
                Membro.celulaNome]


class MembroShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Membro
    _include = [Membro.nome, 
                Membro.creation, 
                Membro.email, 
                Membro.celular,
                Membro.celulaNome]


class SaveMembroCommand(SaveCommand):
    _model_form_class = MembroForm


class UpdateMembroCommand(UpdateNode):
    _model_form_class = MembroForm


class ListMembroCommand(ModelSearchCommand):
    def __init__(self):
        super(ListMembroCommand, self).__init__(Membro.query_by_creation())

