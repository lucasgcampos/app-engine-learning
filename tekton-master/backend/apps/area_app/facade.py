# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from area_app.commands import ListAreaCommand, SaveAreaCommand, UpdateAreaCommand, \
    AreaPublicForm, AreaDetailForm, AreaShortForm


def save_area_cmd(**area_properties):
    """
    Command to save Area entity
    :param area_properties: a dict of properties to save on model
    :return: a Command that save Area, validating and localizing properties received as strings
    """
    return SaveAreaCommand(**area_properties)


def update_area_cmd(area_id, **area_properties):
    """
    Command to update Area entity with id equals 'area_id'
    :param area_properties: a dict of properties to update model
    :return: a Command that update Area, validating and localizing properties received as strings
    """
    return UpdateAreaCommand(area_id, **area_properties)


def list_areas_cmd():
    """
    Command to list Area entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListAreaCommand()


def area_detail_form(**kwargs):
    """
    Function to get Area's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return AreaDetailForm(**kwargs)


def area_short_form(**kwargs):
    """
    Function to get Area's short form. just a subset of area's properties
    :param kwargs: form properties
    :return: Form
    """
    return AreaShortForm(**kwargs)

def area_public_form(**kwargs):
    """
    Function to get Area'spublic form. just a subset of area's properties
    :param kwargs: form properties
    :return: Form
    """
    return AreaPublicForm(**kwargs)


def get_area_cmd(area_id):
    """
    Find area by her id
    :param area_id: the area id
    :return: Command
    """
    return NodeSearch(area_id)


def delete_area_cmd(area_id):
    """
    Construct a command to delete a Area
    :param area_id: area's id
    :return: Command
    """
    return DeleteNode(area_id)

