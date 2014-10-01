# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celula_app.model import Celula
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from relatorio_app import facade
from routes.relatorios import admin


@no_csrf
def index(relatorio_id):
    relatorio = facade.get_relatorio_cmd(relatorio_id)()
    detail_form = facade.relatorio_detail_form()
    context = {'save_path': router.to_path(save, relatorio_id), 'relatorio': detail_form.fill_with_model(relatorio), 'celulas' : Celula.query().fetch()}
    return TemplateResponse(context, 'relatorios/admin/form.html')


def save(_handler, relatorio_id, **relatorio_properties):
    cmd = facade.update_relatorio_cmd(relatorio_id, **relatorio_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'relatorio': cmd.form,
                   'celulas' : Celula.query().fetch()}

        return TemplateResponse(context, 'relatorios/admin/form.html')
    _handler.redirect(router.to_path(admin))

