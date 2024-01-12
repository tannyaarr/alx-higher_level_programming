#!/usr/bin/python3
"""Scripts prints the first State objects from database"""

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

    states = session.query(State).first()

    if states:
        print(f"{first_state.id}: {first_state_name}")
    else:
        print("Nothing")

    session.close()
~                     
