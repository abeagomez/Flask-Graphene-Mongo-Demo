# flask_graphene_mongo/database.py
from mongoengine import connect

from models import Department, Person, Role

connect('test')


def init_db():
    # Create the fixtures
    engineering = Department(name='Engineering')
    engineering.save()

    hr = Department(name='Human Resources')
    hr.save()

    manager = Role(name='manager')
    manager.save()

    engineer = Role(name='engineer')
    engineer.save()

    peter = Person(first_name='Peter', last_name='Parker', department=engineering, role=engineer)
    peter.save()

    roy = Person(first_name='Roy', last_name='Royce', department=engineering, role=engineer)
    roy.save()

    tracy = Person(first_name='Tracy', last_name='Monita', department=hr, role=manager)
    tracy.save()
