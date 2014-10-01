# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb
from celula_app.model import Celula

from gaegraph.model import Node, origins_cache_key, Arc


class Membro(Node):
    nome = ndb.StringProperty(required=True)
    celular = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    celula = ndb.KeyProperty(Celula, required=True)
    celulaNome = ndb.StringProperty()

