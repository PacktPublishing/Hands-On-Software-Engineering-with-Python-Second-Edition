# app.py

# To run this, execute pipenv run uvicorn app:app --reload

# Test with curl:
CURL_COMMAND="""
curl -X POST http://localhost:8000/graphql/ \
    -H "Content-Type: application/json"\
    -d '{"query": "{ getArtisans { oid givenName familyName } }"}'
"""

from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from schema import schema

app = FastAPI()
app.mount(
    "/graphql",
    GraphQLApp(schema=schema, on_get=make_graphiql_handler())
)
