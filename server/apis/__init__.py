from flask_restx import Api

from .endpoints import api as ep

#DOC_PATH determines path for swagger API documentation for our endpoints
DOC_PATH = '/api/doc/'
api = Api(title='Endpoints', doc=DOC_PATH)

api.add_namespace(ep)
