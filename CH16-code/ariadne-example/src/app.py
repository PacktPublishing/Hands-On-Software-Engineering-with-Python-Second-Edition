from fastapi import FastAPI
from ariadne.asgi import GraphQL
from ariadne import make_executable_schema, load_schema_from_path

from resolvers import query, mutation

type_defs = load_schema_from_path("src/schema.graphql")
schema = make_executable_schema(type_defs, query, mutation)

app = FastAPI()
app.mount("/graphql", GraphQL(schema, debug=True))
