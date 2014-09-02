# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from usuario_app import facade
from routes.usuarios import admin


@no_csrf
def index(usuario_id):
    usuario = facade.get_usuario_cmd(usuario_id)()
    detail_form = facade.usuario_detail_form()
    context = {'save_path': router.to_path(save, usuario_id), 'usuario': detail_form.fill_with_model(usuario)}
    return TemplateResponse(context, 'usuarios/admin/form.html')


def save(_handler, usuario_id, **usuario_properties):
    cmd = facade.update_usuario_cmd(usuario_id, **usuario_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'usuario': cmd.form}

        return TemplateResponse(context, 'usuarios/admin/form.html')
    _handler.redirect(router.to_path(admin))

