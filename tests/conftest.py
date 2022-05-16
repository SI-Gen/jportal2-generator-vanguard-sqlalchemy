import pytest as pytest
import sqlalchemy
from sqlalchemy import text
from testcontainers.postgres import PostgresContainer
import docker
import os


@pytest.fixture(scope="session")
def postgres14p2_db():
    """
    Returns an open SQLAlchemy connection to a Postgres
    :return:
    """
    with PostgresContainer("postgres:14.2") as postgres:
        e = sqlalchemy.create_engine(postgres.get_connection_url())
        result = e.execute("select version()")
        print("RESULT: ", result.fetchone())
        yield e


@pytest.fixture(scope="session")
def generate_jportal():
    client = docker.from_env()
    cwd = os.getcwd()
    parent = os.path.dirname(cwd)
    print(parent)
    client.containers.run("ghcr.io/si-gen/jportal2:latest",
                          "--inputdir=/local/tests/si \
                          --template-location=/local \
                          --flag SQLAlchemy.generateBuiltIns \
                          --template-generator \
                            SQLAlchemy:/local/generated_sources/generated \
                          --builtin-generator \
                            PostgresDDL:/local/generated_sources/generated_sql",
                          auto_remove=True,
                          volumes=[f'{parent}:/local']
                          )


@pytest.fixture(scope="session")
def run_takeons(postgres14p2_db):
    cwd = os.getcwd()
    parent = os.path.dirname(cwd)

    takeon = open(os.path.join(parent, "generated_sources", "generated_sql", "ExampleDatabase.sql")).readlines()
    takeon = ''.join([str(elem) for elem in takeon])

    postgres14p2_db.execute(text("CREATE SCHEMA todolist_app;"))
    # postgres_db.execute(text("CREATE TABLE ToDoList_App.ToDoList ( ID serial )"))
    # postgres_db.execute(text("CREATE TABLE ToDoList_App.ToDo_item ( ID serial )"))
    postgres14p2_db.execute(text(takeon))

