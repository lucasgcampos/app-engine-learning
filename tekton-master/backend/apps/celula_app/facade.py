# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from celula_app.commands import ListCelulaCommand, SaveCelulaCommand, UpdateCelulaCommand, \
    CelulaPublicForm, CelulaDetailForm, CelulaShortForm


def save_celula_cmd(**celula_properties):
    """
    Command to save Celula entity
    :param celula_properties: a dict of properties to save on model
    :return: a Command that save Celula, validating and localizing properties received as strings
    """
    return SaveCelulaCommand(**celula_properties)


def update_celula_cmd(celula_id, **celula_properties):
    """
    Command to update Celula entity with id equals 'celula_id'
    :param celula_properties: a dict of properties to update model
    :return: a Command that update Celula, validating and localizing properties received as strings
    """
    return UpdateCelulaCommand(celula_id, **celula_properties)


def list_celulas_cmd():
    """
    Command to list Celula entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListCelulaCommand()


def celula_detail_form(**kwargs):
    """
    Function to get Celula's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return CelulaDetailForm(**kwargs)


def celula_short_form(**kwargs):
    """
    Function to get Celula's short form. just a subset of celula's properties
    :param kwargs: form properties
    :return: Form
    """
    return CelulaShortForm(**kwargs)

def celula_public_form(**kwargs):
    """
    Function to get Celula'spublic form. just a subset of celula's properties
    :param kwargs: form properties
    :return: Form
    """
    return CelulaPublicForm(**kwargs)


def get_celula_cmd(celula_id):
    """
    Find celula by her id
    :param celula_id: the celula id
    :return: Command
    """
    return NodeSearch(celula_id)


def delete_celula_cmd(celula_id):
    """
    Construct a command to delete a Celula
    :param celula_id: celula's id
    :return: Command
    """
    return DeleteNode(celula_id)

