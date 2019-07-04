# flask_graphene_mongo/schema.py
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Department as DepartmentModel
from models import Person as PersonModel
from models import Role as RoleModel

class Department(MongoengineObjectType):

    class Meta:
        model = DepartmentModel
        interfaces = (Node,)

class Role(MongoengineObjectType):

    class Meta:
        model = RoleModel
        interfaces = (Node,)


class Person(MongoengineObjectType):

    class Meta:
        model = PersonModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    node = Node.Field()
    all_people = MongoengineConnectionField(Person)
    all_role = MongoengineConnectionField(Role)
    role = graphene.Field(Role)


    #*: Declaring and resolving the "hello field"
    hello = graphene.String(name=graphene.String(default_value="you!"))
    def resolve_hello(root, info, name):
        return f'Hello {name}'



#TODO: Define some resolve functions for testing
# ?: I have a question
# !: Be careful about this!
# *: Remember about this

schema = graphene.Schema(query=Query, types=[Department, Person, Role])