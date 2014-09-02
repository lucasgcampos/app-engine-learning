# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from area_app import facade
from routes.areas import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'areas/admin/form.html')


def save(_handler, area_id=None, **area_properties):
    cmd = facade.save_area_cmd(**area_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'area': cmd.form}

        return TemplateResponse(context, 'areas/admin/form.html')
    _handler.redirect(router.to_path(admin))

