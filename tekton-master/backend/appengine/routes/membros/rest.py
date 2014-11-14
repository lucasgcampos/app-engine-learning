# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from membro_app import facade


def index():
    cmd = facade.list_membros_cmd()
    membro_list = cmd()
    short_form=facade.membro_short_form()
    membro_short = [short_form.fill_with_model(m) for m in membro_list]
    return JsonResponse(membro_short)


def save(**membro_properties):
    cmd = facade.save_membro_cmd(**membro_properties)
    return _save_or_update_json_response(cmd)


def update(membro_id, **membro_properties):
    cmd = facade.update_membro_cmd(membro_id, **membro_properties)
    return _save_or_update_json_response(cmd)


def delete(membro_id):
    facade.delete_membro_cmd(membro_id)()


def _save_or_update_json_response(cmd):
    try:
        membro = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.membro_short_form()
    return JsonResponse(short_form.fill_with_model(membro))

