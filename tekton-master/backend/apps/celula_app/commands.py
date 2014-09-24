# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from celula_app.model import Celula

class CelulaPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Celula
    _include = [Celula.nome, 
                Celula.data, 
                Celula.area,
                Celula.endereco]



class CelulaForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Celula
    _include = [Celula.nome, 
                Celula.data, 
                Celula.area,
                Celula.endereco]


class CelulaDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Celula
    _include = [Celula.area, 
                Celula.creation, 
                Celula.data, 
                Celula.nome,
                Celula.endereco]


class CelulaShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Celula
    _include = [Celula.area, 
                Celula.creation, 
                Celula.data, 
                Celula.nome,
                Celula.endereco]


class SaveCelulaCommand(SaveCommand):
    _model_form_class = CelulaForm


class UpdateCelulaCommand(UpdateNode):
    _model_form_class = CelulaForm


class ListCelulaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListCelulaCommand, self).__init__(Celula.query_by_creation())

