# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from celula_app import facade
from routes.celulas import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'celulas/admin/form.html')


def save(_handler, celula_id=None, **celula_properties):
    cmd = facade.save_celula_cmd(**celula_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'celula': cmd.form}

        return TemplateResponse(context, 'celulas/admin/form.html')
    _handler.redirect(router.to_path(admin))

