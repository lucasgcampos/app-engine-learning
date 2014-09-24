# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celula_app.model import Celula
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from membro_app import facade
from routes.membros import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_membros_cmd()
    membros = cmd()
    public_form = facade.membro_public_form()
    membro_public_dcts = [public_form.fill_with_model(membro) for membro in membros]

    context = {'membros': membro_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

