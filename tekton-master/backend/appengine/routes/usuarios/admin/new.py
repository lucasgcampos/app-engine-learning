# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from usuario_app import facade
from routes.usuarios import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'usuarios/admin/form.html')


def save(_handler, usuario_id=None, **usuario_properties):
    cmd = facade.save_usuario_cmd(**usuario_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'usuario': cmd.form}

        return TemplateResponse(context, 'usuarios/admin/form.html')
    _handler.redirect(router.to_path(admin))

