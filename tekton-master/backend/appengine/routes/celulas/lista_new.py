from __future__ import absolute_import, unicode_literals
from celula_app.model import Celula
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions
from permission_app.model import ADMIN


@permissions(ADMIN)
@no_csrf
def index():
    query = Celula.query().order(Celula.nome)
    celulas = query.fetch()
    contexto = {'celulas': celulas}
    return TemplateResponse(contexto)

