from models import Dog
from sqlalchemy import (create_engine, desc,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



Base = declarative_base()



def create_table(Base,engine):
        
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())
    Base.metadata.create_all(engine)


if __name__ == '__main__':
     engine= create_engine("sqlite:///dogs.db")
     create_table(Base,engine)
    


def save(session, dog):
    if __name__ == '__main__':

        dog= Dog(
            name=Dog.name,
            email=Dog.breed,
            )

    session.add(dog)
    session.commit()
    

def get_all(session):
    return  session.query(Dog).all()


def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name.like(name)).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id.like(id)).first()


def find_by_name_and_breed(session, name, breed):
        return session.query(Dog).filter(Dog.name.like(name), Dog.breed == breed).first()


def update_breed(session, dog, breed):
        for dog in session.query(Dog):
            dog.breed = breed