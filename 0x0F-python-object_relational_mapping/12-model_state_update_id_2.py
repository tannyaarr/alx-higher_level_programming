#!/usr/bin/python3
"""Script changes the name of a State object in the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    args = sys.argv

    usr = args[1]
    pwd = args[2]
    db = args[3]
    ht = "localhost"
    pt = 3306

    db_string = f"mysql://{usr}:{pwd}@{ht}:{pt}/{db}"

    engine = create_engine(db_string)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_change = session.query(State).filter(State.id == 2).first()

    if state_to_change:
        state_to_change.name = "New Mexico"
        session.commit()
        print("Name changed successfully")
    else:
        print("State with id=2 not found")

    session.close()
