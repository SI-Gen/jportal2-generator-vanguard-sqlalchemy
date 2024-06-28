########################################################################################################################
################## Generated Code. DO NOT CHANGE THIS CODE. Change it in the generator and regenerate ##################
########################################################################################################################

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Any, Optional
import enum
import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import TextAsFrom

from .common.db_common import DBMixin, Base, DBColumn
from .common import db_types
from .common.processing import process_result_recs, process_result_rec, process_bind_params



TESTENUM_SCHEMA = "todolist_app"
class DB_TestEnum(Base, DBMixin):
    # Enum for NodeTypeCharEn field
    class NodeTypeCharEnEnum( enum.Enum):
        Normal = 'N'
        Error = 'E'
        Completed = 'C'
        DeadLetter = 'D'
        Storage = 'S'
        Fail = 'F'

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_TestEnum.NodeTypeCharEnEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    # Enum for IntEn field
    class IntEnEnum( enum.IntEnum):
        First = 1
        Second = 2

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_TestEnum.IntEnEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    ID: int = DBColumn("id", sa.Integer(), primary_key=True, autoincrement=True)
    NodeTypeCharEn: NodeTypeCharEnEnum = DBColumn("nodetypecharen", sa.String(length=1))
    IntEn: IntEnEnum = DBColumn("inten", db_types.IntEnum(IntEnEnum))

    __schema__ = TESTENUM_SCHEMA

    def __init__(self, NodeTypeCharEn: NodeTypeCharEnEnum, IntEn: IntEnEnum):
        super(DB_TestEnum, self).__init__(
            NodeTypeCharEn=NodeTypeCharEn,
            IntEn=IntEn)

@dataclass
class DB_TestEnumInsertReturning:
    # Enum for NodeTypeCharEn field
    class NodeTypeCharEnEnum( enum.Enum):
        Normal = 'N'
        Error = 'E'
        Completed = 'C'
        DeadLetter = 'D'
        Storage = 'S'
        Fail = 'F'

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_TestEnumInsertReturning.NodeTypeCharEnEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    # Enum for IntEn field
    class IntEnEnum( enum.IntEnum):
        First = 1
        Second = 2

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_TestEnumInsertReturning.IntEnEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    #Outputs
    ID: int

    @classmethod
    def get_statement(cls
                     , NodeTypeCharEn: NodeTypeCharEnEnum
                     , IntEn: IntEnEnum
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = " RETURNING ID"
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.TestEnum.Insert */"
                        f"insert into ToDoList_App.TestEnum ("
                        f"  NodeTypeCharEn,"
                        f"  IntEn"
                        f" ) "
                        f"{_ret.output}"
                        f" values ("
                        f"  :NodeTypeCharEn,"
                        f"  :IntEn"
                        f" )"
                        f"{_ret.tail}")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      )
        text_statement = text_statement.bindparams(NodeTypeCharEn=NodeTypeCharEn,
                                         IntEn=IntEn,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, NodeTypeCharEn: NodeTypeCharEnEnum
                     , IntEn: IntEnEnum
                     ) -> Optional['DB_TestEnumInsertReturning']:
        params = process_bind_params(session, [sa.types.String,
                                        sa.types.Integer,
                                        ], [NodeTypeCharEn.value if isinstance(NodeTypeCharEn, enum.Enum) else NodeTypeCharEn,
                                        IntEn.value if isinstance(IntEn, enum.IntEnum) else IntEn,
                                        ])
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(DB_TestEnumInsertReturning, session, [sa.types.Integer,
                                        ], rec)

        return None

@dataclass
class DB_TestEnumIdentity:
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
                        f"select max(ID) ID from ToDoList_App.TestEnum")

        text_statement = statement.columns(ID=sa.types.Integer,
                                      )
        return text_statement

    @classmethod
    def execute(cls, session: Session) -> Optional['DB_TestEnumIdentity']:
        res = session.execute(cls.get_statement())
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(DB_TestEnumIdentity, session, [sa.types.Integer,
                                        ], rec)

        return None

@dataclass
class DB_TestEnumUpdate:
    # Enum for NodeTypeCharEn field
    class NodeTypeCharEnEnum( enum.Enum):
        Normal = 'N'
        Error = 'E'
        Completed = 'C'
        DeadLetter = 'D'
        Storage = 'S'
        Fail = 'F'

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_TestEnumUpdate.NodeTypeCharEnEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    # Enum for IntEn field
    class IntEnEnum( enum.IntEnum):
        First = 1
        Second = 2

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_TestEnumUpdate.IntEnEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    

    @classmethod
    def get_statement(cls
                     , NodeTypeCharEn: NodeTypeCharEnEnum
                     , IntEn: IntEnEnum
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        f"update ToDoList_App.TestEnum"
                        f" set"
                        f"  NodeTypeCharEn = :NodeTypeCharEn"
                        f", IntEn = :IntEn"
                        f" where ID = :ID")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(NodeTypeCharEn=NodeTypeCharEn,
                                         IntEn=IntEn,
                                         ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, NodeTypeCharEn: NodeTypeCharEnEnum
                     , IntEn: IntEnEnum
                     , ID: int
                     ) -> None:
        params = process_bind_params(session, [sa.types.String,
                                        sa.types.Integer,
                                        sa.types.Integer,
                                        ], [NodeTypeCharEn.value if isinstance(NodeTypeCharEn, enum.Enum) else NodeTypeCharEn,
                                        IntEn.value if isinstance(IntEn, enum.IntEnum) else IntEn,
                                        ID,
                                        ])
        res = session.execute(cls.get_statement(*params))
        res.close()

@dataclass
class DB_TestEnumSelectOne:
    # Enum for NodeTypeCharEn field
    class NodeTypeCharEnEnum( enum.Enum):
        Normal = 'N'
        Error = 'E'
        Completed = 'C'
        DeadLetter = 'D'
        Storage = 'S'
        Fail = 'F'

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_TestEnumSelectOne.NodeTypeCharEnEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    # Enum for IntEn field
    class IntEnEnum( enum.IntEnum):
        First = 1
        Second = 2

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return DB_TestEnumSelectOne.IntEnEnum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value


    #Outputs
    NodeTypeCharEn: NodeTypeCharEnEnum
    IntEn: IntEnEnum

    @classmethod
    def get_statement(cls
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (NodeTypeCharEn,IntEn)"
            tail = " RETURNING NodeTypeCharEn IntEn"
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.TestEnum.SelectOne */"
                        f"select"
                        f"  NodeTypeCharEn"
                        f", IntEn"
                        f" from ToDoList_App.TestEnum"
                        f" where ID = :ID")

        text_statement = statement.columns(NodeTypeCharEn=sa.types.String,
                                      IntEn=sa.types.Integer,
                                      )
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> Optional['DB_TestEnumSelectOne']:
        params = process_bind_params(session, [sa.types.Integer,
                                        ], [ID,
                                        ])
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(DB_TestEnumSelectOne, session, [DB_TestEnumSelectOne.NodeTypeCharEnEnum,
                                        DB_TestEnumSelectOne.IntEnEnum,
                                        ], rec)

        return None

@dataclass
class DB_TestEnumDeleteOne:
    

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
                        f"/* PROC ToDoList_App.TestEnum.DeleteOne */"
                        f"delete from ToDoList_App.TestEnum"
                        f" where ID = :ID")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> None:
        params = process_bind_params(session, [sa.types.Integer,
                                        ], [ID,
                                        ])
        res = session.execute(cls.get_statement(*params))
        res.close()

@dataclass
class DB_TestEnumExists:
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
                        f"/* PROC ToDoList_App.TestEnum.Exists */"
                        f"select count(*) noOf from ToDoList_App.TestEnum"
                        f" where ID = :ID")

        text_statement = statement.columns(noOf=sa.types.Integer,
                                      )
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> Optional['DB_TestEnumExists']:
        params = process_bind_params(session, [sa.types.Integer,
                                        ], [ID,
                                        ])
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(DB_TestEnumExists, session, [sa.types.Integer,
                                        ], rec)

        return None

@dataclass
class DB_TestEnumCheckIfStoredProcCreated:
    

    @classmethod
    def get_statement(cls
                     , ID: int
                     , Payload: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        f"/* PROC ToDoList_App.TestEnum.CheckIfStoredProcCreated */"
                        f"SELECT "
                        f"Payload "
                        f"FROM "
                        f"TestSP "
                        f"WHERE "
                        f"ID = :ID ")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(ID=ID,
                                         Payload=Payload,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     , Payload: int
                     ) -> None:
        params = process_bind_params(session, [sa.types.Integer,
                                        sa.types.Integer,
                                        ], [ID,
                                        Payload,
                                        ])
        res = session.execute(cls.get_statement(*params))
        res.close()
