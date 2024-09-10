import os

from mongoengine import connect
from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp
from starlette_graphene3 import make_graphiql_handler

from my_graphql.schema import schema

client = connect(host=os.environ["DATABASE_URL"])
db = client[os.environ["DATABASE_NAME"]]

app = Starlette()

app.mount("/", GraphQLApp(schema, on_get=make_graphiql_handler()))
