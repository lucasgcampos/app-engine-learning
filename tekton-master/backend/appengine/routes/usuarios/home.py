# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from usuario_app import facade
from routes.usuarios import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_usuarios_cmd()
    usuarios = cmd()
    public_form = facade.usuario_public_form()
    usuario_public_dcts = [public_form.fill_with_model(usuario) for usuario in usuarios]
    context = {'usuarios': usuario_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

