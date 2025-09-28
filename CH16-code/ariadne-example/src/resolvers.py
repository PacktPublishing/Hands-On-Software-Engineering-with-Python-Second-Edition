from ariadne import QueryType, MutationType
from hms.core.business_objects import Artisan
from uuid import UUID
from converters import artisan_to_dict, input_to_artisan

query = QueryType()
mutation = MutationType()

# -- Query Resolvers --
@query.field("get_artisans")
def resolve_get_artisans(_, info):
    artisans = Artisan.get(db_source_name='Artisan')
    return [artisan_to_dict(a) for a in artisans]

@query.field("get_artisan_by_oid")
def resolve_get_artisan_by_oid(_, info, oid):
    artisan = Artisan.get(UUID(oid), db_source_name='Artisan')
    return artisan_to_dict(artisan[0]) if artisan else None

# -- Mutation Resolvers --
@mutation.field("create_artisan")
def resolve_create_artisan(_, info, artisan):
    new_artisan = input_to_artisan(artisan)
    new_artisan.save(db_source_name='Artisan')
    return artisan_to_dict(new_artisan)

@mutation.field("update_artisan_by_oid")
def resolve_update_artisan_by_oid(_, info, oid, artisan):
    updated = input_to_artisan(artisan)
    updated.oid = UUID(oid)
    updated.save(db_source_name='Artisan')
    return artisan_to_dict(updated)
