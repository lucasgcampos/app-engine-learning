# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb

from gaegraph.model import Node, origins_cache_key, Arc


class Membro(Node):
    nome = ndb.StringProperty(required=True)
    celular = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)

class MembroLider(Arc):
    origin = ndb.KeyProperty()
    destination = ndb.KeyProperty(Membro, required=True)

