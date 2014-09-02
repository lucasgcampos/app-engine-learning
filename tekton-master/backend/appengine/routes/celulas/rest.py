# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from celula_app import facade


def index():
    cmd = facade.list_celulas_cmd()
    celula_list = cmd()
    short_form=facade.celula_short_form()
    celula_short = [short_form.fill_with_model(m) for m in celula_list]
    return JsonResponse(celula_short)


def save(**celula_properties):
    cmd = facade.save_celula_cmd(**celula_properties)
    return _save_or_update_json_response(cmd)


def update(celula_id, **celula_properties):
    cmd = facade.update_celula_cmd(celula_id, **celula_properties)
    return _save_or_update_json_response(cmd)


def delete(celula_id):
    facade.delete_celula_cmd(celula_id)()


def _save_or_update_json_response(cmd):
    try:
        celula = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.celula_short_form()
    return JsonResponse(short_form.fill_with_model(celula))

