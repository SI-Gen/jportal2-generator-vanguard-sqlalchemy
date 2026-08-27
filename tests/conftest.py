import pytest as pytest
from generated_sources.generated.common.db_common import Base
import sqlalchemy
from sqlalchemy import text
from sqlalchemy.orm import close_all_sessions
from testcontainers.postgres import PostgresContainer
import docker
import os


@pytest.fixture(scope="session")
def postgres14p2_db_clean():
    """
    Returns an open SQLAlchemy connection to a Postgres
    :return:
    """
    with PostgresContainer("postgres:14.2") as postgres:
        e = sqlalchemy.create_engine(postgres.get_connection_url())
        result = e.execute("select version()")
        print("RESULT: ", result.fetchone())
        result.close()
        try:
            yield e
        finally:
            close_all_sessions()
            e.dispose()


@pytest.fixture(scope="session")
def generate_jportal(pytestconfig):
    client = docker.from_env()
    cwd = os.getcwd()
    #parent = os.path.dirname(cwd)
    parent = pytestconfig.rootpath
    print("XXX:",parent)
    # client.containers.run("bbdsoftware/jportal2:latest",
    client.containers.run("ghcr.io/si-gen/jportal2:latest",
                          # "--inputdir=/local/tests/si \
                          # --template-location=/local \
                          # --flag SQLAlchemy.generateBuiltIns \
                          # --template-generator \
                          #   SQLAlchemy:/local/generated_sources/generated \
                          # --builtin-generator \
                          #   PostgresDDL:/local/generated_sources/generated_sql",
                          auto_remove=True,
                          # volumes=[f'{parent}:/local']
                          )


@pytest.fixture(scope="session")
def postgres14p2_db(pytestconfig, generate_jportal, postgres14p2_db_clean):
    cwd = os.getcwd()
    #parent = os.path.dirname(cwd)
    parent = pytestconfig.rootpath
    # takeon = open(os.path.join(parent, "generated_sources", "generated_sql", "ExampleDatabase.sql")).readlines()
    # takeon = ''.join([str(elem) for elem in takeon])

    postgres14p2_db_clean.execute(text("DROP SCHEMA IF EXISTS todolist_app;"))
    postgres14p2_db_clean.execute(text("CREATE SCHEMA IF NOT EXISTS todolist_app;"))
    # postgres_db.execute(text("CREATE TABLE ToDoList_App.ToDoList ( ID serial )"))
    # postgres_db.execute(text("CREATE TABLE ToDoList_App.ToDo_item ( ID serial )"))
    # postgres14p2_db_clean.execute(text(takeon))
    Base.metadata.create_all(postgres14p2_db_clean)

    return postgres14p2_db_clean

