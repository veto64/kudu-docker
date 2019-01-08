#!/usr/bin/env python
import time
import falcon
import json
import kudu
import uuid
from kudu.client import Partitioning
from datetime import datetime

class Row:
  def __init__(self,config):
   self.config = config

  def on_get(self, req, res,table,row):
    api = {
     'table'   : table,
     'row'     : row,
     'errors'  : []
     }
    client = kudu.connect(host='queen', port=7051)

    if client.table_exists(table):
      row_id  = row
      table   = client.table(table)
      scanner = table.scanner()
      #api['scanner'] = dir(scanner)
      scanner.add_predicate(table['_id'] == row_id )
      ret = scanner.open().read_all_tuples()
      api['ret'] = ret
    else:
      api['errors'].append('Table does not exist')
    res.body = json.dumps(api)
    res.status = falcon.HTTP_200

  def on_put(self, req, res,table,row):
    api = {
     'table'  : table,
     'errors' : [],
     'data' : {} 
     }
    client = kudu.connect(host='queen', port=7051)
    session = client.new_session()
    if client.table_exists(table): 
      tb = client.table(table)
      sm = tb.schema
      data   = json.loads(req.bounded_stream.read().decode("utf-8"))
      table  = client.table(table)
      schema = {}      
      for i in sm:
        schema[i.name] = i.type.name
      scanner = table.scanner()
      scanner.set_limit(1) 
      op = table.new_insert()   
      if not '_id' in data:
       data['_id'] = str(uuid.uuid4()).split('-')[4]
      for i in data:
        if i in schema:
          op[i] = data[i]
          api['data'][i] = data[i]
      session.apply(op)
      session.flush()

    else:
      api['errors'].append('Table does not exist')
    res.body = json.dumps(api)
    res.status = falcon.HTTP_200

