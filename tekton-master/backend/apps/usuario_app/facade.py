# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from usuario_app.commands import ListUsuarioCommand, SaveUsuarioCommand, UpdateUsuarioCommand, \
    UsuarioPublicForm, UsuarioDetailForm, UsuarioShortForm


def save_usuario_cmd(**usuario_properties):
    """
    Command to save Usuario entity
    :param usuario_properties: a dict of properties to save on model
    :return: a Command that save Usuario, validating and localizing properties received as strings
    """
    return SaveUsuarioCommand(**usuario_properties)


def update_usuario_cmd(usuario_id, **usuario_properties):
    """
    Command to update Usuario entity with id equals 'usuario_id'
    :param usuario_properties: a dict of properties to update model
    :return: a Command that update Usuario, validating and localizing properties received as strings
    """
    return UpdateUsuarioCommand(usuario_id, **usuario_properties)


def list_usuarios_cmd():
    """
    Command to list Usuario entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListUsuarioCommand()


def usuario_detail_form(**kwargs):
    """
    Function to get Usuario's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return UsuarioDetailForm(**kwargs)


def usuario_short_form(**kwargs):
    """
    Function to get Usuario's short form. just a subset of usuario's properties
    :param kwargs: form properties
    :return: Form
    """
    return UsuarioShortForm(**kwargs)

def usuario_public_form(**kwargs):
    """
    Function to get Usuario'spublic form. just a subset of usuario's properties
    :param kwargs: form properties
    :return: Form
    """
    return UsuarioPublicForm(**kwargs)


def get_usuario_cmd(usuario_id):
    """
    Find usuario by her id
    :param usuario_id: the usuario id
    :return: Command
    """
    return NodeSearch(usuario_id)


def delete_usuario_cmd(usuario_id):
    """
    Construct a command to delete a Usuario
    :param usuario_id: usuario's id
    :return: Command
    """
    return DeleteNode(usuario_id)

