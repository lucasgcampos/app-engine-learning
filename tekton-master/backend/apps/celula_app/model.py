# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Celula(Node):
    nome = ndb.StringProperty(required=True)
    data = ndb.DateProperty(required=True)
    area = ndb.IntegerProperty(required=True)

