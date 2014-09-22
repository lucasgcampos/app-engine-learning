# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from relatorio_app import facade
from routes.relatorios.admin import new, edit


def delete(_handler, relatorio_id):
    facade.delete_relatorio_cmd(relatorio_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_relatorios_cmd()
    relatorios = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.relatorio_short_form()

    def short_relatorio_dict(relatorio):
        relatorio_dct = short_form.fill_with_model(relatorio)
        relatorio_dct['edit_path'] = router.to_path(edit_path, relatorio_dct['id'])
        relatorio_dct['delete_path'] = router.to_path(delete_path, relatorio_dct['id'])
        return relatorio_dct

    short_relatorios = [short_relatorio_dict(relatorio) for relatorio in relatorios]
    context = {'relatorios': short_relatorios,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

