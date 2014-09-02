# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from area_app.model import Area

class AreaPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Area
    _include = [Area.responsavel, 
                Area.area]


class AreaForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Area
    _include = [Area.responsavel, 
                Area.area]


class AreaDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Area
    _include = [Area.responsavel, 
                Area.creation, 
                Area.area]


class AreaShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Area
    _include = [Area.responsavel, 
                Area.creation, 
                Area.area]


class SaveAreaCommand(SaveCommand):
    _model_form_class = AreaForm


class UpdateAreaCommand(UpdateNode):
    _model_form_class = AreaForm


class ListAreaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListAreaCommand, self).__init__(Area.query_by_creation())

