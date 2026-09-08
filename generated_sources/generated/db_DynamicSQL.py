########################################################################################################################
################## Generated Code. DO NOT CHANGE THIS CODE. Change it in the generator and regenerate ##################
########################################################################################################################

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Any, Optional

import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import TextAsFrom

from .common.db_common import DBMixin, Base, DBColumn
from .common import db_types
from .common.processing import process_result_recs, process_result_rec, process_bind_params



DYNAMICSQL_SCHEMA = "todolist_app"
class DB_DynamicSQL(Base, DBMixin):
    Id: int = DBColumn("id", sa.Integer(), primary_key=True, autoincrement=False)
    Sent: int = DBColumn("sent", sa.SmallInteger())
    SendDateTime: Optional[datetime] = DBColumn("senddatetime", sa.DateTime(), nullable=True, default=datetime.now, onupdate=datetime.now)

    __schema__ = DYNAMICSQL_SCHEMA

    def __init__(self, Id: Optional[int], Sent: int, SendDateTime: Optional[datetime]):
        super(DB_DynamicSQL, self).__init__(
            Id=Id,
            Sent=Sent,
            SendDateTime=SendDateTime)

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
                        f"/* PROC ToDoList_App.DynamicSQL.BatchMarkAsSent */"
                        f"UPDATE DynamicSQL "
                        f"SET Sent = 1, "
                        f"SendDateTime = CURRENT_TIMESTAMP "
                        f"WHERE Id IN (  "
                        f"{SentIds}"
                        f" ) ")

        text_statement = statement.columns()
        return text_statement

    @classmethod
    def execute(cls, session: Session, SentIds: str) -> None:
        params = process_bind_params(session, [db_types.NonNullableString,], [SentIds,])
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
                        f"/* PROC ToDoList_App.DynamicSQL.MarkSelected */"
                        f"UPDATE DynamicSQL "
                        f"SET Sent = :Sent "
                        f"WHERE Id IN (  "
                        f"{SentIds}"
                        f" ) ")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(Sent=Sent,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, Sent: int
                     , SentIds: str) -> None:
        params = process_bind_params(session, [sa.types.SmallInteger,
                                        db_types.NonNullableString,], [Sent,
                                        SentIds,])
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
                        f"/* PROC ToDoList_App.DynamicSQL.MarkAll */"
                        f"UPDATE DynamicSQL SET Sent = 1 ")

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
                        f"/* PROC ToDoList_App.DynamicSQL.MarkOne */"
                        f"UPDATE DynamicSQL SET Sent = 1 WHERE Id = :Id ")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(Id=Id,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, Id: int
                     ) -> None:
        params = process_bind_params(session, [sa.types.Integer,
                                        ], [Id,
                                        ])
        res = session.execute(cls.get_statement(*params))
        res.close()
