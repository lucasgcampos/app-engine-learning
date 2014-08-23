# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from area_app import facade
from routes.areas import admin


@no_csrf
def index(area_id):
    area = facade.get_area_cmd(area_id)()
    detail_form = facade.area_detail_form()
    context = {'save_path': router.to_path(save, area_id), 'area': detail_form.fill_with_model(area)}
    return TemplateResponse(context, 'areas/admin/form.html')


def save(_handler, area_id, **area_properties):
    cmd = facade.update_area_cmd(area_id, **area_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'area': cmd.form}

        return TemplateResponse(context, 'areas/admin/form.html')
    _handler.redirect(router.to_path(admin))

