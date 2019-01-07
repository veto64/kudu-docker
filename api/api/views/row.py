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
      if row.isdigit():
        row_id  = int(row)
        table   = client.table(table)
        scanner = table.scanner()
        #api['scanner'] = dir(scanner)
        scanner.add_predicate(table['_id'] == row_id )
        ret = scanner.open().read_all_tuples()
        api['ret'] =ret
      else:
        api['errors'].append('Row is not an integer/number')
    else:
      api['errors'].append('Table does not exist')
    res.body = json.dumps(api)
    res.status = falcon.HTTP_200



  def on_put(self, req, res,table,row):
    api = {
     'table'  : table,
     'success': False,
     'errors' : [] 
     }
    client = kudu.connect(host='queen', port=7051)
    session = client.new_session()
    if client.table_exists(table): 
      tb = client.table(table)
      sm = tb.schema
      data = json.loads(req.bounded_stream.read().decode("utf-8"))
      table   = client.table(table)
      schema = {}      
      for i in sm:
        schema[i.name] = i.type.name
      scanner = table.scanner()
      scanner.set_limit(1) 
      #scanner.add_predicate(table['_id'] == row_id )
      op = table.new_insert()   
      if not '_id' in data:
        op['_id'] = 'xxxx'
      for i in data:
        if i in schema:
          print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')
          print(data[i])
          print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')
          print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')

      op['_id'] = 1
      op['style'] = 'xxxx'

      #session.apply(op)
      #session.flush()

      api['success'] = True
      api['insert'] = True

    else:
      api['errors'].append('Table does not exist')

    res.body = json.dumps(api)
    res.status = falcon.HTTP_200

