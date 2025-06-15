import graphene
from graphene import ObjectType, Field, List, \
    Mutation, UUID as GrapheneUUID, String
from graphene_pydantic import PydanticObjectType, \
    PydanticInputObjectType

from hms.core.business_objects import Artisan, Address
from uuid import UUID

# --- Graphene Types ---

class AddressInput(PydanticInputObjectType):
    class Meta:
        model = Address
        exclude_fields = ()

class AddressType(PydanticObjectType):
    class Meta:
        model = Address
        exclude_fields = ()

class ArtisanType(PydanticObjectType):
    class Meta:
        model = Artisan
        exclude_fields = (
            # Custom handling
            "email_address",
            # Ignoring Product associations for now
            "products"
        )

    email_address = graphene.String()

    def resolve_email_address(parent, info):
        return str(parent.email_address)

class ArtisanInput(PydanticInputObjectType):
    class Meta:
        model = Artisan
        exclude_fields = (
            # Let this be auto-generated
            "oid",
            # This has special handling
            "email_address",
            # Ignoring Product associations for now
            "products",
        )

    email_address = graphene.String(required=True)

# --- Mutations ---

class CreateArtisan(Mutation):
    class Arguments:
        artisan_data = ArtisanInput(required=True)

    Output = ArtisanType

    def mutate(root, info, artisan_data):
        artisan = Artisan(**artisan_data.model_dump())
        artisan.save()
        return artisan

class UpdateArtisanByOid(Mutation):
    class Arguments:
        oid = GrapheneUUID(required=True)
        artisan_data = ArtisanInput(required=True)

    Output = ArtisanType

    def mutate(root, info, oid: UUID, artisan_data):
        existing = Artisan.get(oid)
        if not existing:
            raise Exception(f"Artisan with oid {oid} not found")
        updated_artisan = artisan_data.model_copy(update={"oid": oid})
        updated_artisan.save(db_source_name='Artisan')
        return updated_artisan

# --- Queries ---

class Query(ObjectType):
    get_artisans = List(ArtisanType)
    get_artisan_by_oid = Field(ArtisanType, oid=GrapheneUUID(required=True))

    def resolve_get_artisans(root, info):
        return Artisan.get(db_source_name='Artisan')

    def resolve_get_artisan_by_oid(root, info, oid: UUID):
        return Artisan.get(oid,db_source_name='Artisan')[0] if Artisan.get(oid) else None

# --- Mutation Root ---

class Mutation(ObjectType):
    create_artisan = CreateArtisan.Field()
    update_artisan_by_oid = UpdateArtisanByOid.Field()

# --- Final Schema ---

schema = graphene.Schema(query=Query, mutation=Mutation)
