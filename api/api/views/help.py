#!/usr/bin/env python
import time
import falcon
import json
import kudu
from kudu.client import Partitioning
from datetime import datetime
import sortedcontainers

class Help:

  def __init__(self,config, env):
   self.env = env
   self.config = config
   self.api = {
      '_API' : 'help',
      'method' : '',
      'status': 'http://127.0.0.1:8051',
      'tables': {}
    }

  def on_get(self, req, res):
    self.api['method'] = 'GET'
    template = self.env.get_template('index.html')

    res.content_type = 'falcon.MEDIA_HTML'
    res.body  = template.render(data=self.api)


  def on_delete(self, req, res):
    self.api['method'] = 'DELETE'
