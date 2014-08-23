# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from area_app import facade
from routes.areas import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_areas_cmd()
    areas = cmd()
    public_form = facade.area_public_form()
    area_public_dcts = [public_form.fill_with_model(area) for area in areas]
    context = {'areas': area_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

