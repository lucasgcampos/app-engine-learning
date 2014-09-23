# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from celula_app.model import Celula
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from membro_app.model import Membro
from tekton import router
from gaecookie.decorator import no_csrf
from membro_app import facade
from routes.membros import admin


@no_csrf
def index():


    contexto = {'save_path': router.to_path(save), 'celulas' : Celula.query().fetch()}
    return TemplateResponse(contexto,'membros/admin/form.html')


def save(_handler, celula, **membro_properties):
    form = facade.membro_short_form(**membro_properties)
    erros=form.validate()
    if not erros:
        dct=form.normalize()
        celula_key=ndb.Key(Celula,int(celula))
        membro=Membro(celula=celula_key,**dct)
        membro.put()
    else:
        context = {'errors': erros,
                   'membro': membro_properties}

        return TemplateResponse(context, 'membros/admin/form.html')
    _handler.redirect(router.to_path(admin))

