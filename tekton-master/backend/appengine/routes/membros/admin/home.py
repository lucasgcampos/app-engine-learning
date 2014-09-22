# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from membro_app import facade
from routes.membros.admin import new, edit


def delete(_handler, membro_id):
    facade.delete_membro_cmd(membro_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_membros_cmd()
    membros = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.membro_short_form()

    def short_membro_dict(membro):
        membro_dct = short_form.fill_with_model(membro)
        membro_dct['edit_path'] = router.to_path(edit_path, membro_dct['id'])
        membro_dct['delete_path'] = router.to_path(delete_path, membro_dct['id'])
        return membro_dct

    short_membros = [short_membro_dict(membro) for membro in membros]
    context = {'membros': short_membros,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

