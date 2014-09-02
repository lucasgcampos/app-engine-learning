# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from usuario_app import facade
from routes.usuarios.admin import new, edit


def delete(_handler, usuario_id):
    facade.delete_usuario_cmd(usuario_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_usuarios_cmd()
    usuarios = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.usuario_short_form()

    def short_usuario_dict(usuario):
        usuario_dct = short_form.fill_with_model(usuario)
        usuario_dct['edit_path'] = router.to_path(edit_path, usuario_dct['id'])
        usuario_dct['delete_path'] = router.to_path(delete_path, usuario_dct['id'])
        return usuario_dct

    short_usuarios = [short_usuario_dict(usuario) for usuario in usuarios]
    context = {'usuarios': short_usuarios,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

