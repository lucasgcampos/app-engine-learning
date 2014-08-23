# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from area_app import facade
from routes.areas.admin import new, edit


def delete(_handler, area_id):
    facade.delete_area_cmd(area_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_areas_cmd()
    areas = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.area_short_form()

    def short_area_dict(area):
        area_dct = short_form.fill_with_model(area)
        area_dct['edit_path'] = router.to_path(edit_path, area_dct['id'])
        area_dct['delete_path'] = router.to_path(delete_path, area_dct['id'])
        return area_dct

    short_areas = [short_area_dict(area) for area in areas]
    context = {'areas': short_areas,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

