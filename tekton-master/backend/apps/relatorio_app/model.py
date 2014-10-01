# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb
from celula_app.model import Celula

from gaegraph.model import Node


class Relatorio(Node):
    tema = ndb.StringProperty(required=True)
    geral = ndb.IntegerProperty(required=True)
    cincoes = ndb.IntegerProperty(required=True)
    participacao = ndb.IntegerProperty(required=True)
    horario = ndb.IntegerProperty(required=True)
    conteudo = ndb.IntegerProperty(required=True)
    observacao = ndb.StringProperty(required=True)
    data = ndb.DateProperty(required=True)
    celula = ndb.KeyProperty(Celula, required=True)
    celulaNome = ndb.StringProperty()
