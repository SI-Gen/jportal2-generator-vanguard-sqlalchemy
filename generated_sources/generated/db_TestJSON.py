########################################################################################################################
################## Generated Code. DO NOT CHANGE THIS CODE. Change it in the generator and regenerate ##################
########################################################################################################################

from dataclasses import dataclass
from typing import Optional
import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import TextAsFrom

from .common.db_common import DBMixin, Base, DBColumn
from .common.processing import process_bind_params, process_result_rec



TESTJSON_SCHEMA = "todolist_app"
class DB_TestJSON(Base, DBMixin):
    ID: int = DBColumn("id", sa.Integer(),
        primary_key=True,
        autoincrement=True)
    Payload: str = DBColumn("payload", sa.JSON)

    __schema__ = TESTJSON_SCHEMA

    def __init__(self,
        Payload: str):
        self.Payload = Payload

@dataclass
class DB_TestJSONInsertReturning:
    #Outputs
    ID: int

    @classmethod
    def get_statement(cls
                     , Payload: str
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = " RETURNING ID"
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.TestJSON.Insert */"
                        "insert into ToDoList_App.TestJSON ("
                        "  Payload"
                        " ) "
                        f"{_ret.output}"
                        " values ("
                        "  :Payload"
                        " )"
                        f"{_ret.tail}")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      )
        text_statement = text_statement.bindparams(Payload=Payload,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, Payload: str
                     ) -> Optional['DB_TestJSONInsertReturning']:
        params = process_bind_params(
            session,
            [
                sa.JSON,
            ],
            [
                Payload,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(
                DB_TestJSONInsertReturning,
                session,
                [
                    sa.types.Integer,
                ],
                rec,
            )

        return None

@dataclass
class DB_TestJSONIdentity:
    #Outputs
    ID: int

    @classmethod
    def get_statement(cls
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (ID)"
            tail = " RETURNING ID"
            #session.bind.dialect.name

        statement = sa.text(
                        "select max(ID) ID from ToDoList_App.TestJSON")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      )
        return text_statement

    @classmethod
    def execute(cls, session: Session) -> Optional['DB_TestJSONIdentity']:
        res = session.execute(cls.get_statement())
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(
                DB_TestJSONIdentity,
                session,
                [
                    sa.types.Integer,
                ],
                rec,
            )

        return None

@dataclass
class DB_TestJSONUpdate:
    

    @classmethod
    def get_statement(cls
                     , Payload: str
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        "update ToDoList_App.TestJSON"
                        " set"
                        "  Payload = :Payload"
                        " where ID = :ID")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(Payload=Payload,
                                         ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, Payload: str
                     , ID: int
                     ) -> None:
        params = process_bind_params(
            session,
            [
                sa.JSON,
                sa.types.Integer,
            ],
            [
                Payload,
                ID,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        res.close()

@dataclass
class DB_TestJSONSelectOne:
    #Inputs
    ID: int

    #Outputs
    Payload: str

    @classmethod
    def get_statement(cls
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (Payload)"
            tail = " RETURNING Payload"
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.TestJSON.SelectOne */"
                        "select"
                        "  Payload"
                        " from ToDoList_App.TestJSON"
                        " where ID = :ID")

        text_statement = statement.columns(Payload=sa.JSON,
                                      )
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> Optional['DB_TestJSONSelectOne']:
        params = process_bind_params(
            session,
            [
                sa.types.Integer,
            ],
            [
                ID,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(
                DB_TestJSONSelectOne,
                session,
                [
                    sa.JSON,
                ],
                rec,
                ID=ID,
            )

        return None

@dataclass
class DB_TestJSONDeleteOne:
    

    @classmethod
    def get_statement(cls
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.TestJSON.DeleteOne */"
                        "delete from ToDoList_App.TestJSON"
                        " where ID = :ID")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> None:
        params = process_bind_params(
            session,
            [
                sa.types.Integer,
            ],
            [
                ID,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        res.close()

@dataclass
class DB_TestJSONExists:
    #Outputs
    noOf: int

    @classmethod
    def get_statement(cls
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (noOf)"
            tail = " RETURNING noOf"
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.TestJSON.Exists */"
                        "select count(*) noOf from ToDoList_App.TestJSON"
                        " where ID = :ID")

        text_statement = statement.columns(noOf=sa.types.Integer,
                                      )
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> Optional['DB_TestJSONExists']:
        params = process_bind_params(
            session,
            [
                sa.types.Integer,
            ],
            [
                ID,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(
                DB_TestJSONExists,
                session,
                [
                    sa.types.Integer,
                ],
                rec,
            )

        return None
