# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from relatorio_app import facade


def index():
    cmd = facade.list_relatorios_cmd()
    relatorio_list = cmd()
    short_form=facade.relatorio_short_form()
    relatorio_short = [short_form.fill_with_model(m) for m in relatorio_list]
    return JsonResponse(relatorio_short)


def save(**relatorio_properties):
    cmd = facade.save_relatorio_cmd(**relatorio_properties)
    return _save_or_update_json_response(cmd)


def update(relatorio_id, **relatorio_properties):
    cmd = facade.update_relatorio_cmd(relatorio_id, **relatorio_properties)
    return _save_or_update_json_response(cmd)


def delete(relatorio_id):
    facade.delete_relatorio_cmd(relatorio_id)()


def _save_or_update_json_response(cmd):
    try:
        relatorio = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.relatorio_short_form()
    return JsonResponse(short_form.fill_with_model(relatorio))

