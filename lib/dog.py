from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

from models import Dog

def create_table(base):
    base.metadata.create_all(engine)
    return engine

def save(session, dog):
    session.add(dog)
    session.commit()
    return session

def new_from_db(session, row):
    # return session.query(Dog).filter(Dog.id == row.id).first()
    return session.query(Dog).filter_by(id = row.id).first()
    # return session.query(Dog).first() still passes 

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name = name).first() #filter_by using kwarg (key word argument), sqlalchemy query
    # return session.query(Dog).filter(Dog.name == name).first(), filter uses sql syntax, still sqlalchmey query, keep note of the double "=="

def find_by_id(session, id):
    # return session.query(Dog).filter(Dog.id == id).first()
    return session.query(Dog).filter_by(id = id).first()

def find_by_name_and_breed(session, name, breed):
    # return session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()
    return session.query(Dog).filter_by(name = name, breed = breed).first()

def update_breed(session, dog, breed):
    session.query(Dog).update({Dog.breed: breed})
    return [dog for dog in session.query(Dog)]
    #the above code passes, but incorrect