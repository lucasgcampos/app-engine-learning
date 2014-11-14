# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from celula_app import facade


@login_not_required
@no_csrf
def index():
    cmd = facade.list_celulas_cmd()
    celula_list = cmd()
    short_form=facade.celula_short_form()
    celula_short = [short_form.fill_with_model(m) for m in celula_list]
    return JsonResponse(celula_short)

@login_not_required
@no_csrf
def save(**celula_properties):
    cmd = facade.save_celula_cmd(**celula_properties)
    return _save_or_update_json_response(cmd)

@login_not_required
@no_csrf
def save(_resp, **celula_properties):
    cmd = facade.save_celula_cmd(**celula_properties)
    return _save_or_update_json_response(_resp, cmd)

@login_not_required
@no_csrf
def update(_resp, celula_id, **celula_properties):
    cmd = facade.update_celula_cmd(celula_id, **celula_properties)
    return _save_or_update_json_response(_resp, cmd)

@login_not_required
@no_csrf
def delete(celula_id):
    facade.delete_celula_cmd(celula_id)()

@login_not_required
@no_csrf
def _save_or_update_json_response(_resp, cmd):
    try:
        celula = cmd()
    except CommandExecutionException:
        _resp.status_code = 500;
        return JsonUnsecureResponse(cmd.errors)
    short_form = facade.celula_short_form()
    return JsonResponse(short_form.fill_with_model(celula))

