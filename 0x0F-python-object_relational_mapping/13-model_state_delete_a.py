#!/usr/bin/python3
"""Script deletes State objects with a name containing the letter 'a' from the database"""

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
    states_to_delete = session.query(State).filter(State.name.ilike('%a%')).all()

    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit()
        print("States deleted successfully")
    else:
        print("No states found with a name containing 'a'")

    session.close()
