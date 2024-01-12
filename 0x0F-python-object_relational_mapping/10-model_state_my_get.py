#!/usr/bin/python3
"""Script prints the State object with the name passed as an argument"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    args = sys.argv

    usr = args[1]
    pwd = args[2]
    db = args[3]
    state_name_to_search = args[4]
    ht = "localhost"
    pt = 3306

    db_string = f"mysql://{usr}:{pwd}@{ht}:{pt}/{db}"
    engine = create_engine(db_string)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_found = session.query(State).filter(State.name == state_name_to_search).first()

    if state_found:
        print(state_found.id)
    else:
        print("Not found")

    session.close()
