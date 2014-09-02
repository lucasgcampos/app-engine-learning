# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from usuario_app.model import Usuario

class UsuarioPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Usuario
    _include = [Usuario.celula, 
                Usuario.nome, 
                Usuario.idade, 
                Usuario.celular, 
                Usuario.endereco]


class UsuarioForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Usuario
    _include = [Usuario.celula, 
                Usuario.nome, 
                Usuario.idade, 
                Usuario.celular, 
                Usuario.endereco]


class UsuarioDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Usuario
    _include = [Usuario.celula, 
                Usuario.nome, 
                Usuario.creation, 
                Usuario.idade, 
                Usuario.celular, 
                Usuario.endereco]


class UsuarioShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Usuario
    _include = [Usuario.celula, 
                Usuario.nome, 
                Usuario.creation, 
                Usuario.idade, 
                Usuario.celular, 
                Usuario.endereco]


class SaveUsuarioCommand(SaveCommand):
    _model_form_class = UsuarioForm


class UpdateUsuarioCommand(UpdateNode):
    _model_form_class = UsuarioForm


class ListUsuarioCommand(ModelSearchCommand):
    def __init__(self):
        super(ListUsuarioCommand, self).__init__(Usuario.query_by_creation())

