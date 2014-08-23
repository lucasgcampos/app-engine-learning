# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Usuario(Node):
    nome = ndb.StringProperty(required=True)
    idade = ndb.IntegerProperty(required=True)
    celula = ndb.StringProperty(required=True)
    endereco = ndb.StringProperty(required=True)
    celular = ndb.StringProperty(required=True)

