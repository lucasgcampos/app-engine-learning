# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from membro_app.commands import ListMembroCommand, SaveMembroCommand, UpdateMembroCommand, \
    MembroPublicForm, MembroDetailForm, MembroShortForm, ListMembroDeCelula

#here
def list_membros_de_celula(celula):
    """
    Método que retornar comando que lista escravos de um dono ordenados
    por data criação
    :param dono: Dono (Usuário) ou um comando que retorne um usuário como resultado
    :return: Comando que retorna lista de escravos como resultado

    """
    return ListMembroDeCelula(celula)

def save_membro_cmd(**membro_properties):
    """
    Command to save Membro entity
    :param membro_properties: a dict of properties to save on model
    :return: a Command that save Membro, validating and localizing properties received as strings
    """
    return SaveMembroCommand(**membro_properties)


def update_membro_cmd(membro_id, **membro_properties):
    """
    Command to update Membro entity with id equals 'membro_id'
    :param membro_properties: a dict of properties to update model
    :return: a Command that update Membro, validating and localizing properties received as strings
    """
    return UpdateMembroCommand(membro_id, **membro_properties)


def list_membros_cmd():
    """
    Command to list Membro entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListMembroCommand()


def membro_detail_form(**kwargs):
    """
    Function to get Membro's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return MembroDetailForm(**kwargs)


def membro_short_form(**kwargs):
    """
    Function to get Membro's short form. just a subset of membro's properties
    :param kwargs: form properties
    :return: Form
    """
    return MembroShortForm(**kwargs)

def membro_public_form(**kwargs):
    """
    Function to get Membro'spublic form. just a subset of membro's properties
    :param kwargs: form properties
    :return: Form
    """
    return MembroPublicForm(**kwargs)


def get_membro_cmd(membro_id):
    """
    Find membro by her id
    :param membro_id: the membro id
    :return: Command
    """
    return NodeSearch(membro_id)


def delete_membro_cmd(membro_id):
    """
    Construct a command to delete a Membro
    :param membro_id: membro's id
    :return: Command
    """
    return DeleteNode(membro_id)

