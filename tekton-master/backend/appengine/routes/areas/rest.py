# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from area_app import facade


def index():
    cmd = facade.list_areas_cmd()
    area_list = cmd()
    short_form=facade.area_short_form()
    area_short = [short_form.fill_with_model(m) for m in area_list]
    return JsonResponse(area_short)


def save(**area_properties):
    cmd = facade.save_area_cmd(**area_properties)
    return _save_or_update_json_response(cmd)


def update(area_id, **area_properties):
    cmd = facade.update_area_cmd(area_id, **area_properties)
    return _save_or_update_json_response(cmd)


def delete(area_id):
    facade.delete_area_cmd(area_id)()


def _save_or_update_json_response(cmd):
    try:
        area = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.area_short_form()
    return JsonResponse(short_form.fill_with_model(area))

