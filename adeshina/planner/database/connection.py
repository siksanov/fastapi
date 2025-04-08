from sqlmodel import SQLModel, Session, create_engine

database = "planner_db"
database_connection_string = f"postgresql://postgres:postgres@localhost/{database}"
connect_args = {}
engine_url = create_engine(database_connection_string,
                    echo=True, connect_args=connect_args)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session