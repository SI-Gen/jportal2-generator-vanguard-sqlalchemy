########################################################################################################################
################## Generated Code. DO NOT CHANGE THIS CODE. Change it in the generator and regenerate ##################
########################################################################################################################

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import TextAsFrom

from .common.db_common import DBMixin, Base, DBColumn
from .common import db_types
from .common.processing import process_bind_params



DYNAMICSQL_SCHEMA = "todolist_app"
class DB_DynamicSQL(Base, DBMixin):
    Id: int = DBColumn("id", sa.Integer(),
        primary_key=True,
        autoincrement=False)
    Sent: int = DBColumn("sent", sa.SmallInteger())
    SendDateTime: Optional[datetime] = DBColumn("senddatetime", sa.DateTime(),
        nullable=True,
        default=datetime.now,
        onupdate=datetime.now)

    __schema__ = DYNAMICSQL_SCHEMA

    def __init__(self,
        Id: int,
        Sent: int,
        SendDateTime: Optional[datetime]):
        self.Id = Id
        self.Sent = Sent
        self.SendDateTime = SendDateTime

@dataclass
class DB_DynamicSQLBatchMarkAsSent:
    

    @classmethod
    def get_statement(cls
                     , SentIds: str) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.DynamicSQL.BatchMarkAsSent */"
                        "UPDATE DynamicSQL "
                        "SET Sent = 1, "
                        "SendDateTime = CURRENT_TIMESTAMP "
                        "WHERE Id IN (  "
                        f"{SentIds}"
                        " ) ")

        text_statement = statement.columns()
        return text_statement

    @classmethod
    def execute(cls, session: Session, SentIds: str) -> None:
        params = process_bind_params(
            session,
            [
                db_types.NonNullableString,
            ],
            [
                SentIds,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        res.close()

@dataclass
class DB_DynamicSQLMarkSelected:
    

    @classmethod
    def get_statement(cls
                     , Sent: int
                     , SentIds: str) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.DynamicSQL.MarkSelected */"
                        "UPDATE DynamicSQL "
                        "SET Sent = :Sent "
                        "WHERE Id IN (  "
                        f"{SentIds}"
                        " ) ")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(Sent=Sent,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, Sent: int
                     , SentIds: str) -> None:
        params = process_bind_params(
            session,
            [
                sa.types.SmallInteger,
                db_types.NonNullableString,
            ],
            [
                Sent,
                SentIds,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        res.close()

@dataclass
class DB_DynamicSQLMarkAll:
    

    @classmethod
    def get_statement(cls
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.DynamicSQL.MarkAll */"
                        "UPDATE DynamicSQL SET Sent = 1 ")

        text_statement = statement.columns()
        return text_statement

    @classmethod
    def execute(cls, session: Session) -> None:
        res = session.execute(cls.get_statement())
        res.close()

@dataclass
class DB_DynamicSQLMarkOne:
    

    @classmethod
    def get_statement(cls
                     , Id: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.DynamicSQL.MarkOne */"
                        "UPDATE DynamicSQL SET Sent = 1 WHERE Id = :Id ")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(Id=Id,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, Id: int
                     ) -> None:
        params = process_bind_params(
            session,
            [
                sa.types.Integer,
            ],
            [
                Id,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        res.close()
