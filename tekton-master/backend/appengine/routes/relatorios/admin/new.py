# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from relatorio_app import facade
from routes.relatorios import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'relatorios/admin/form.html')


def save(_handler, relatorio_id=None, **relatorio_properties):
    cmd = facade.save_relatorio_cmd(**relatorio_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'relatorio': cmd.form}

        return TemplateResponse(context, 'relatorios/admin/form.html')
    _handler.redirect(router.to_path(admin))

