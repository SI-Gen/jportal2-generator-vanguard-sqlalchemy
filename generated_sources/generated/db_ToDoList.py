########################################################################################################################
################## Generated Code. DO NOT CHANGE THIS CODE. Change it in the generator and regenerate ##################
########################################################################################################################

from dataclasses import dataclass
from datetime import datetime
import enum
from typing import List, Optional
import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import TextAsFrom

from .common.db_common import DBMixin, Base, DBColumn
from .common import db_types
from .common.processing import process_bind_params, process_result_rec, process_result_recs



TODOLIST_SCHEMA = "todolist_app"
class DB_ToDoList(Base, DBMixin):
    # Enum for ListType field
    class ListTypeEnum(enum.IntEnum):
        Private = 1
        Public = 2
        Custom = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_ToDoList.ListTypeEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    ID: int = DBColumn("id", sa.Integer(),
        primary_key=True,
        autoincrement=True)
    ListName: str = DBColumn("listname", db_types.NonNullableString(length=255))
    ListType: ListTypeEnum = DBColumn("listtype", db_types.IntEnum(ListTypeEnum))
    Description: str = DBColumn("description", db_types.NonNullableString(length=255))
    LastUpdated: datetime = DBColumn("lastupdated", sa.DateTime(),
        default=datetime.now,
        onupdate=datetime.now)

    __schema__ = TODOLIST_SCHEMA

    def __init__(self,
        ListName: str,
        ListType: ListTypeEnum,
        Description: str,
        LastUpdated: datetime):
        self.ListName = ListName
        self.ListType = ListType
        self.Description = Description
        self.LastUpdated = LastUpdated

@dataclass
class DB_ToDoListInsertReturning:
    # Enum for ListType field
    class ListTypeEnum(enum.IntEnum):
        Private = 1
        Public = 2
        Custom = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_ToDoListInsertReturning.ListTypeEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    #Outputs
    ID: int

    @classmethod
    def get_statement(cls
                     , ListName: str
                     , ListType: ListTypeEnum
                     , Description: str
                     , LastUpdated: datetime
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = " RETURNING ID"
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.ToDoList.Insert */"
                        "insert into ToDoList_App.ToDoList ("
                        "  ListName,"
                        "  ListType,"
                        "  Description,"
                        "  LastUpdated"
                        " ) "
                        f"{_ret.output}"
                        " values ("
                        "  :ListName,"
                        "  :ListType,"
                        "  :Description,"
                        "  :LastUpdated"
                        " )"
                        f"{_ret.tail}")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      )
        text_statement = text_statement.bindparams(ListName=ListName,
                                         ListType=ListType,
                                         Description=Description,
                                         LastUpdated=LastUpdated,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ListName: str
                     , ListType: ListTypeEnum
                     , Description: str
                     , LastUpdated: datetime
                     ) -> Optional['DB_ToDoListInsertReturning']:
        params = process_bind_params(
            session,
            [
                db_types.NonNullableString,
                sa.types.SmallInteger,
                db_types.NonNullableString,
                sa.types.DateTime,
            ],
            [
                ListName,
                ListType.value if isinstance(ListType, enum.IntEnum) else ListType,
                Description,
                LastUpdated,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(
                DB_ToDoListInsertReturning,
                session,
                [
                    sa.types.Integer,
                ],
                rec,
            )

        return None

@dataclass
class DB_ToDoListIdentity:
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
                        "select max(ID) ID from ToDoList_App.ToDoList")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      )
        return text_statement

    @classmethod
    def execute(cls, session: Session) -> Optional['DB_ToDoListIdentity']:
        res = session.execute(cls.get_statement())
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(
                DB_ToDoListIdentity,
                session,
                [
                    sa.types.Integer,
                ],
                rec,
            )

        return None

@dataclass
class DB_ToDoListUpdate:
    # Enum for ListType field
    class ListTypeEnum(enum.IntEnum):
        Private = 1
        Public = 2
        Custom = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_ToDoListUpdate.ListTypeEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    

    @classmethod
    def get_statement(cls
                     , ListName: str
                     , ListType: ListTypeEnum
                     , Description: str
                     , LastUpdated: datetime
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        "update ToDoList_App.ToDoList"
                        " set"
                        "  ListName = :ListName"
                        ", ListType = :ListType"
                        ", Description = :Description"
                        ", LastUpdated = :LastUpdated"
                        " where ID = :ID")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(ListName=ListName,
                                         ListType=ListType,
                                         Description=Description,
                                         LastUpdated=LastUpdated,
                                         ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ListName: str
                     , ListType: ListTypeEnum
                     , Description: str
                     , LastUpdated: datetime
                     , ID: int
                     ) -> None:
        params = process_bind_params(
            session,
            [
                db_types.NonNullableString,
                sa.types.SmallInteger,
                db_types.NonNullableString,
                sa.types.DateTime,
                sa.types.Integer,
            ],
            [
                ListName,
                ListType.value if isinstance(ListType, enum.IntEnum) else ListType,
                Description,
                LastUpdated,
                ID,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        res.close()

@dataclass
class DB_ToDoListSelectOne:
    # Enum for ListType field
    class ListTypeEnum(enum.IntEnum):
        Private = 1
        Public = 2
        Custom = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_ToDoListSelectOne.ListTypeEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    #Inputs
    ID: int

    #Outputs
    ListName: str
    ListType: ListTypeEnum
    Description: str
    LastUpdated: datetime

    @classmethod
    def get_statement(cls
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (ListName,ListType,Description,LastUpdated)"
            tail = " RETURNING ListName ListType Description LastUpdated"
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.ToDoList.SelectOne */"
                        "select"
                        "  ListName"
                        ", ListType"
                        ", Description"
                        ", LastUpdated"
                        " from ToDoList_App.ToDoList"
                        " where ID = :ID")

        text_statement = statement.columns(ListName=db_types.NonNullableString,
                                      ListType=sa.types.SmallInteger,
                                      Description=db_types.NonNullableString,
                                      LastUpdated=sa.types.DateTime,
                                      )
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> Optional['DB_ToDoListSelectOne']:
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
                DB_ToDoListSelectOne,
                session,
                [
                    db_types.NonNullableString,
                    DB_ToDoListSelectOne.ListTypeEnum,
                    db_types.NonNullableString,
                    sa.types.DateTime,
                ],
                rec,
                ID=ID,
            )

        return None

@dataclass
class DB_ToDoListDeleteOne:
    

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
                        "/* PROC ToDoList_App.ToDoList.DeleteOne */"
                        "delete from ToDoList_App.ToDoList"
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
class DB_ToDoListExists:
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
                        "/* PROC ToDoList_App.ToDoList.Exists */"
                        "select count(*) noOf from ToDoList_App.ToDoList"
                        " where ID = :ID")

        text_statement = statement.columns(noOf=sa.types.Integer,
                                      )
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> Optional['DB_ToDoListExists']:
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
                DB_ToDoListExists,
                session,
                [
                    sa.types.Integer,
                ],
                rec,
            )

        return None

@dataclass
class DB_ToDoListSelectOneByListName:
    # Enum for ListType field
    class ListTypeEnum(enum.IntEnum):
        Private = 1
        Public = 2
        Custom = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_ToDoListSelectOneByListName.ListTypeEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    #Outputs
    ID: int
    ListName: str
    ListType: ListTypeEnum
    Description: str
    LastUpdated: datetime

    @classmethod
    def get_statement(cls
                     , ListName: str
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (ID,ListName,ListType,Description,LastUpdated)"
            tail = " RETURNING ID ListName ListType Description LastUpdated"
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.ToDoList.SelectOneByListName */"
                        "select"
                        "  ID"
                        ", ListName"
                        ", ListType"
                        ", Description"
                        ", LastUpdated"
                        " from ToDoList_App.ToDoList"
                        " where ListName = :ListName")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      ListName=db_types.NonNullableString,
                                      ListType=sa.types.SmallInteger,
                                      Description=db_types.NonNullableString,
                                      LastUpdated=sa.types.DateTime,
                                      )
        text_statement = text_statement.bindparams(ListName=ListName,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ListName: str
                     ) -> Optional['DB_ToDoListSelectOneByListName']:
        params = process_bind_params(
            session,
            [
                db_types.NonNullableString,
            ],
            [
                ListName,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(
                DB_ToDoListSelectOneByListName,
                session,
                [
                    sa.types.Integer,
                    db_types.NonNullableString,
                    DB_ToDoListSelectOneByListName.ListTypeEnum,
                    db_types.NonNullableString,
                    sa.types.DateTime,
                ],
                rec,
            )

        return None

@dataclass
class DB_ToDoListSelectByListType:
    # Enum for ListType field
    class ListTypeEnum(enum.IntEnum):
        Private = 1
        Public = 2
        Custom = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_ToDoListSelectByListType.ListTypeEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    #Outputs
    ID: int
    ListName: str
    ListType: ListTypeEnum
    Description: str
    LastUpdated: datetime

    @classmethod
    def get_statement(cls
                     , ListType: ListTypeEnum
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (ID,ListName,ListType,Description,LastUpdated)"
            tail = " RETURNING ID ListName ListType Description LastUpdated"
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.ToDoList.SelectByListType */"
                        "select"
                        "  ID"
                        ", ListName"
                        ", ListType"
                        ", Description"
                        ", LastUpdated"
                        " from ToDoList_App.ToDoList"
                        " where ListType = :ListType")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      ListName=db_types.NonNullableString,
                                      ListType=sa.types.SmallInteger,
                                      Description=db_types.NonNullableString,
                                      LastUpdated=sa.types.DateTime,
                                      )
        text_statement = text_statement.bindparams(ListType=ListType,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ListType: ListTypeEnum
                     ) -> List['DB_ToDoListSelectByListType']:
        params = process_bind_params(
            session,
            [
                sa.types.SmallInteger,
            ],
            [
                ListType.value if isinstance(ListType, enum.IntEnum) else ListType,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        recs = res.fetchall()
        return process_result_recs(
            DB_ToDoListSelectByListType,
            session,
            [
                sa.types.Integer,
                db_types.NonNullableString,
                DB_ToDoListSelectByListType.ListTypeEnum,
                db_types.NonNullableString,
                sa.types.DateTime,
            ],
            recs,
        )

@dataclass
class DB_ToDoListSelectIDByListType:
    # Enum for ListType field
    class ListTypeEnum(enum.IntEnum):
        Private = 1
        Public = 2
        Custom = 3

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_ToDoListSelectIDByListType.ListTypeEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    #Outputs
    ID: int

    @classmethod
    def get_statement(cls
                     , ListType: ListTypeEnum
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (ID)"
            tail = " RETURNING ID"
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.ToDoList.SelectIDByListType */"
                        "select"
                        "  ID"
                        " from ToDoList_App.ToDoList"
                        " where ListType = :ListType")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      )
        text_statement = text_statement.bindparams(ListType=ListType,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ListType: ListTypeEnum
                     ) -> List['DB_ToDoListSelectIDByListType']:
        params = process_bind_params(
            session,
            [
                sa.types.SmallInteger,
            ],
            [
                ListType.value if isinstance(ListType, enum.IntEnum) else ListType,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        recs = res.fetchall()
        return process_result_recs(
            DB_ToDoListSelectIDByListType,
            session,
            [
                sa.types.Integer,
            ],
            recs,
        )

@dataclass
class DB_ToDoListSelectListNameAndListTypeAsString:
    #Outputs
    ListName: str
    ListType: str

    @classmethod
    def get_statement(cls
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (ListName,ListType)"
            tail = " RETURNING ListName ListType"
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.ToDoList.SelectListNameAndListTypeAsString */"
                        "SELECT "
                        "ListName, "
                        "CASE "
                        "WHEN ListType = 1 THEN 'Private' "
                        "WHEN ListType = 2 THEN 'Public' "
                        "END "
                        "FROM "
                        "TodoList "
                        "WHERE "
                        "ID = :ID ")

        text_statement = statement.columns(ListName=db_types.NonNullableString,
                                      ListType=db_types.NonNullableString,
                                      )
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> List['DB_ToDoListSelectListNameAndListTypeAsString']:
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
        recs = res.fetchall()
        return process_result_recs(
            DB_ToDoListSelectListNameAndListTypeAsString,
            session,
            [
                db_types.NonNullableString,
                db_types.NonNullableString,
            ],
            recs,
        )

@dataclass
class DB_ToDoListSelectWithDynamicQuery:
    # Enum for ListType field
    class ListTypeEnum(enum.IntEnum):
        Private = 1
        Public = 2

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_ToDoListSelectWithDynamicQuery.ListTypeEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    #Outputs
    ID: int
    ListName: str
    ListType: ListTypeEnum
    Description: str
    LastUpdated: datetime

    @classmethod
    def get_statement(cls
                     , ListName: str
                     , MyDynamicWhereClause: str) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (ID,ListName,ListType,Description,LastUpdated)"
            tail = " RETURNING ID ListName ListType Description LastUpdated"
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.ToDoList.SelectWithDynamicQuery */"
                        "SELECT "
                        "ID "
                        ",ListName "
                        ",ListType "
                        ",Description "
                        ",LastUpdated "
                        "FROM "
                        "ToDoList_App.ToDoList "
                        "WHERE "
                        "ListName = :ListName "
                        "AND  "
                        f"{MyDynamicWhereClause}"
                        " ")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      ListName=db_types.NonNullableString,
                                      ListType=sa.types.SmallInteger,
                                      Description=db_types.NonNullableString,
                                      LastUpdated=sa.types.DateTime,
                                      )
        text_statement = text_statement.bindparams(ListName=ListName,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ListName: str
                     , MyDynamicWhereClause: str) -> List['DB_ToDoListSelectWithDynamicQuery']:
        params = process_bind_params(
            session,
            [
                db_types.NonNullableString,
                db_types.NonNullableString,
            ],
            [
                ListName,
                MyDynamicWhereClause,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        recs = res.fetchall()
        return process_result_recs(
            DB_ToDoListSelectWithDynamicQuery,
            session,
            [
                sa.types.Integer,
                db_types.NonNullableString,
                DB_ToDoListSelectWithDynamicQuery.ListTypeEnum,
                db_types.NonNullableString,
                sa.types.DateTime,
            ],
            recs,
        )

@dataclass
class DB_ToDoListStaticData:
    

    @classmethod
    def get_statement(cls
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        "INSERT INTO ToDoList_App.ToDoList(ListName,ListType,Description,LastUpdated) VALUES ('Takeon"
                        " Test List 1', 1, 'Take on test list description', CURRENT_DATE );")

        text_statement = statement.columns()
        return text_statement

    @classmethod
    def execute(cls, session: Session) -> None:
        res = session.execute(cls.get_statement())
        res.close()
