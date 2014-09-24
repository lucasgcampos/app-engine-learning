# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from relatorio_app.model import Relatorio

class RelatorioPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Relatorio
    _include = [Relatorio.participacao, 
                Relatorio.geral, 
                Relatorio.observacao, 
                Relatorio.horario, 
                Relatorio.tema, 
                Relatorio.conteudo, 
                Relatorio.data, 
                Relatorio.cincoes]


class RelatorioForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Relatorio
    _include = [Relatorio.participacao, 
                Relatorio.geral, 
                Relatorio.observacao, 
                Relatorio.horario, 
                Relatorio.tema, 
                Relatorio.conteudo, 
                Relatorio.data, 
                Relatorio.cincoes]


class RelatorioDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Relatorio
    _include = [Relatorio.participacao, 
                Relatorio.data, 
                Relatorio.creation, 
                Relatorio.observacao, 
                Relatorio.horario, 
                Relatorio.tema, 
                Relatorio.conteudo, 
                Relatorio.geral, 
                Relatorio.cincoes]


class RelatorioShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Relatorio
    _include = [Relatorio.participacao, 
                Relatorio.data, 
                Relatorio.creation, 
                Relatorio.observacao, 
                Relatorio.horario, 
                Relatorio.tema, 
                Relatorio.conteudo, 
                Relatorio.geral, 
                Relatorio.cincoes]


class SaveRelatorioCommand(SaveCommand):
    _model_form_class = RelatorioForm


class UpdateRelatorioCommand(UpdateNode):
    _model_form_class = RelatorioForm


class ListRelatorioCommand(ModelSearchCommand):
    def __init__(self):
        super(ListRelatorioCommand, self).__init__(Relatorio.query_by_creation())

