# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from relatorio_app.commands import ListRelatorioCommand, SaveRelatorioCommand, UpdateRelatorioCommand, \
    RelatorioPublicForm, RelatorioDetailForm, RelatorioShortForm


def save_relatorio_cmd(**relatorio_properties):
    """
    Command to save Relatorio entity
    :param relatorio_properties: a dict of properties to save on model
    :return: a Command that save Relatorio, validating and localizing properties received as strings
    """
    return SaveRelatorioCommand(**relatorio_properties)


def update_relatorio_cmd(relatorio_id, **relatorio_properties):
    """
    Command to update Relatorio entity with id equals 'relatorio_id'
    :param relatorio_properties: a dict of properties to update model
    :return: a Command that update Relatorio, validating and localizing properties received as strings
    """
    return UpdateRelatorioCommand(relatorio_id, **relatorio_properties)


def list_relatorios_cmd():
    """
    Command to list Relatorio entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListRelatorioCommand()


def relatorio_detail_form(**kwargs):
    """
    Function to get Relatorio's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return RelatorioDetailForm(**kwargs)


def relatorio_short_form(**kwargs):
    """
    Function to get Relatorio's short form. just a subset of relatorio's properties
    :param kwargs: form properties
    :return: Form
    """
    return RelatorioShortForm(**kwargs)

def relatorio_public_form(**kwargs):
    """
    Function to get Relatorio'spublic form. just a subset of relatorio's properties
    :param kwargs: form properties
    :return: Form
    """
    return RelatorioPublicForm(**kwargs)


def get_relatorio_cmd(relatorio_id):
    """
    Find relatorio by her id
    :param relatorio_id: the relatorio id
    :return: Command
    """
    return NodeSearch(relatorio_id)


def delete_relatorio_cmd(relatorio_id):
    """
    Construct a command to delete a Relatorio
    :param relatorio_id: relatorio's id
    :return: Command
    """
    return DeleteNode(relatorio_id)

