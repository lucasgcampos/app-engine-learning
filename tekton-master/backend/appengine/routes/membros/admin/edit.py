# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from membro_app import facade
from routes.membros import admin


@no_csrf
def index(membro_id):
    membro = facade.get_membro_cmd(membro_id)()
    detail_form = facade.membro_detail_form()
    context = {'save_path': router.to_path(save, membro_id), 'membro': detail_form.fill_with_model(membro)}
    return TemplateResponse(context, 'membros/admin/form.html')


def save(_handler, membro_id, **membro_properties):
    cmd = facade.update_membro_cmd(membro_id, **membro_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'membro': cmd.form}

        return TemplateResponse(context, 'membros/admin/form.html')
    _handler.redirect(router.to_path(admin))

