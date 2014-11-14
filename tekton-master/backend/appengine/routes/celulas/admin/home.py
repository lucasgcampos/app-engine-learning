# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celula_app.facade import celula_public_form
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required
from tekton import router
from gaecookie.decorator import no_csrf
from celula_app import facade
from routes.celulas.admin import new, edit


def delete(_handler, celula_id):
    facade.delete_celula_cmd(celula_id)()
    _handler.redirect(router.to_path(index))


# @no_csrf
# def index():
#     context = {'new_path' : router.to_path(new)}
#     return TemplateResponse(context)


@no_csrf
@login_not_required
def index():
    cmd = facade.list_celulas_cmd()
    celulas = cmd()
    public_form = facade.celula_public_form()

    celula_public_dcts = [public_form.fill_with_model(celula) for celula in celulas]
    context = {
        'celulas' : celula_public_dcts,
        'new_path' : router.to_path(new)
    }
    return TemplateResponse(context)