# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celula_app.model import Celula
from config.template_middleware import TemplateResponse
from google.appengine.ext import ndb
from relatorio_app.model import Relatorio
from tekton import router
from gaecookie.decorator import no_csrf
from relatorio_app import facade
from routes.relatorios import admin


@no_csrf
def index():
    contexto = {'save_path': router.to_path(save), 'celulas' : Celula.query().fetch()}
    return TemplateResponse(contexto,'relatorios/admin/form.html')


def save(_handler, celula, **relatorio_properties):
    form = facade.relatorio_short_form(**relatorio_properties)
    erros=form.validate()
    if not erros:
        dct=form.normalize()
        celula_key=ndb.Key(Celula,int(celula))
        relatorio=Relatorio(celula=celula_key,**dct)
        relatorio.put()
    else:
        context = {'errors': erros,
                   'relatorio': relatorio_properties}

        return TemplateResponse(context, 'relatorios/admin/form.html')
    _handler.redirect(router.to_path(admin))

