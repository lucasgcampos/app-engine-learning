# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from celula_app import facade
from routes.celulas.admin import new, edit


def delete(_handler, celula_id):
    facade.delete_celula_cmd(celula_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_celulas_cmd()
    celulas = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.celula_short_form()

    def short_celula_dict(celula):
        celula_dct = short_form.fill_with_model(celula)
        celula_dct['edit_path'] = router.to_path(edit_path, celula_dct['id'])
        celula_dct['delete_path'] = router.to_path(delete_path, celula_dct['id'])
        return celula_dct

    short_celulas = [short_celula_dict(celula) for celula in celulas]
    context = {'celulas': short_celulas,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

