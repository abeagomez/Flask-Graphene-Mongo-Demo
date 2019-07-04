# flask_graphene_mongo/models.py
from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField,
)

class Department(Document):
    meta = {'collection': 'department'}
    name = StringField()


class Role(Document):
    meta = {'collection': 'role'}
    name = StringField()


class Person(Document):
    meta = {'collection': 'person'}
    first_name = StringField()
    last_name = StringField()
    hired_on = DateTimeField(default=datetime.now)
    department = ReferenceField(Department)
    role = ReferenceField(Role)