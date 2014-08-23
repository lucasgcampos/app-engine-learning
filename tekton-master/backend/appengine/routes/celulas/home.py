# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from celula_app import facade
from routes.celulas import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_celulas_cmd()
    celulas = cmd()
    public_form = facade.celula_public_form()
    celula_public_dcts = [public_form.fill_with_model(celula) for celula in celulas]
    context = {'celulas': celula_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

