#!env python
import falcon
import yaml
from views import main,tables,table,row,help
from falcon_cors import CORS
from jinja2 import Environment, PackageLoader, select_autoescape

cors = CORS(allow_all_origins=True)
api = falcon.API(middleware=[cors.middleware])

env = Environment(
  loader=PackageLoader('templates','help'),
  autoescape=select_autoescape(['html', 'xml']),
)

with open("config.yml", 'r') as stream:
  try:
    config = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    config = False

if config:
  api.add_route('/', tables.Tables(config))
  api.add_route('/tables', tables.Tables(config))
  api.add_route('/{table}', table.Table(config))
  api.add_route('/{table}/{row}', row.Row(config))
  api.add_route('/help', help.Help(config,env))




