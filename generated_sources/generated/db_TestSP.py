########################################################################################################################
################## Generated Code. DO NOT CHANGE THIS CODE. Change it in the generator and regenerate ##################
########################################################################################################################

from dataclasses import dataclass
from typing import Optional
import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import TextAsFrom

from .common.db_common import DBMixin, Base, DBColumn
from .common import db_types
from .common.processing import process_bind_params, process_result_rec



TESTSP_SCHEMA = "todolist_app"
class DB_TestSP(Base, DBMixin):
    ID: int = DBColumn("id", sa.Integer(),
        primary_key=True,
        autoincrement=True)
    Payload: str = DBColumn("payload", db_types.NonNullableString(length=255))

    __schema__ = TESTSP_SCHEMA

    def __init__(self,
        Payload: str):
        self.Payload = Payload

@dataclass
class DB_TestSPInsertReturning:
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
                        "/* PROC ToDoList_App.TestSP.Insert */"
                        "insert into ToDoList_App.TestSP ("
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
                     ) -> Optional['DB_TestSPInsertReturning']:
        params = process_bind_params(
            session,
            [
                db_types.NonNullableString,
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
                DB_TestSPInsertReturning,
                session,
                [
                    sa.types.Integer,
                ],
                rec,
            )

        return None

@dataclass
class DB_TestSPIdentity:
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
                        "select max(ID) ID from ToDoList_App.TestSP")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      )
        return text_statement

    @classmethod
    def execute(cls, session: Session) -> Optional['DB_TestSPIdentity']:
        res = session.execute(cls.get_statement())
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(
                DB_TestSPIdentity,
                session,
                [
                    sa.types.Integer,
                ],
                rec,
            )

        return None

@dataclass
class DB_TestSPUpdate:
    

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
                        "update ToDoList_App.TestSP"
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
                db_types.NonNullableString,
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
class DB_TestSPSelectOne:
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
                        "/* PROC ToDoList_App.TestSP.SelectOne */"
                        "select"
                        "  Payload"
                        " from ToDoList_App.TestSP"
                        " where ID = :ID")

        text_statement = statement.columns(Payload=db_types.NonNullableString,
                                      )
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> Optional['DB_TestSPSelectOne']:
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
                DB_TestSPSelectOne,
                session,
                [
                    db_types.NonNullableString,
                ],
                rec,
                ID=ID,
            )

        return None

@dataclass
class DB_TestSPDeleteOne:
    

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
                        "/* PROC ToDoList_App.TestSP.DeleteOne */"
                        "delete from ToDoList_App.TestSP"
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
class DB_TestSPExists:
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
                        "/* PROC ToDoList_App.TestSP.Exists */"
                        "select count(*) noOf from ToDoList_App.TestSP"
                        " where ID = :ID")

        text_statement = statement.columns(noOf=sa.types.Integer,
                                      )
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> Optional['DB_TestSPExists']:
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
                DB_TestSPExists,
                session,
                [
                    sa.types.Integer,
                ],
                rec,
            )

        return None

@dataclass
class DB_TestSPCheckIfStoredProcCreated:
    

    @classmethod
    def get_statement(cls
                     , ID: int
                     , Payload: str
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.TestSP.CheckIfStoredProcCreated */"
                        "SELECT "
                        "Payload "
                        "FROM "
                        "TestSP "
                        "WHERE "
                        "ID = :ID ")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(ID=ID,
                                         Payload=Payload,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     , Payload: str
                     ) -> None:
        params = process_bind_params(
            session,
            [
                sa.types.Integer,
                db_types.NonNullableString,
            ],
            [
                ID,
                Payload,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        res.close()
