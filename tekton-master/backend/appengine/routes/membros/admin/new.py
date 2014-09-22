# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from membro_app import facade
from routes.membros import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'membros/admin/form.html')


def save(_handler, membro_id=None, **membro_properties):
    cmd = facade.save_membro_cmd(**membro_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'membro': cmd.form}

        return TemplateResponse(context, 'membros/admin/form.html')
    _handler.redirect(router.to_path(admin))

    #membro = membro_detail_form().fill_model()
    #chave_do_membro  = membro.put()
    #chave_do_usuario = _logged_user.key
    #membro_lider = MembroLider(origin=chave_do_usuario, destination=chave_do_membro)
    #membro_lider.put()
