# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from usuario_app import facade


def index():
    cmd = facade.list_usuarios_cmd()
    usuario_list = cmd()
    short_form=facade.usuario_short_form()
    usuario_short = [short_form.fill_with_model(m) for m in usuario_list]
    return JsonResponse(usuario_short)


def save(**usuario_properties):
    cmd = facade.save_usuario_cmd(**usuario_properties)
    return _save_or_update_json_response(cmd)


def update(usuario_id, **usuario_properties):
    cmd = facade.update_usuario_cmd(usuario_id, **usuario_properties)
    return _save_or_update_json_response(cmd)


def delete(usuario_id):
    facade.delete_usuario_cmd(usuario_id)()


def _save_or_update_json_response(cmd):
    try:
        usuario = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.usuario_short_form()
    return JsonResponse(short_form.fill_with_model(usuario))

