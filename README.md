# jportal2-generator-vanguard-sqlalchemy
This is a JPortal2 generator that generates SQLAlchemy-based database access for the Vanguard framework

Usage:
======

```shell

#Change directory to template directory
cd <template_directory>

#Download version $VERSION template
SQLALCHEMY_TEMPLATE_VERSION=1.2
curl -fsSL https://github.com/SI-Gen/jportal2-generatoror-vanguard-sqlalchemy/releases/tag/$SQLALCHEMY_TEMPLATE_VERSION/jportal2-generator-vanguardg-sqlalchemy-$SQLALCHEMY_TEMPLATE_VERSION.zip > sqlalchemy.zip && unzip sqlalchemy.zip && rm sqlalchemy.zip

#Run JPortal2
java -jar jportal.jar \
        --inputdir=<input_directory> \
        --template-location=<template_directory> \
        --flag SQLAlchemy.generateBuiltIns \
        --template-generator \
          SQLAlchemy:<output_directory>

```
Output:
=======

Flags:
=====

- SQLAlchemy.generateBuiltIns
Generates the built-in PROC's like Insert, SelectOne, Update, SelectBy etc.

Usage in Python code:
=====================

This generated code leverages SQLAlchemy.
You need to install the following requirements:
```shell
pip install sqlalchemy
```

Using the generated procs:
```python
res = db_ExampleTable.DB_ExampleTableSelectOne.execute(session, primary_key)
```

If you want to use the standard alchemy way to select a record
```python
res = session.query(db_ExampleTable.DB_ExampleTable).get(primary_key)
```

Input:
=====

```sql
///
/// Name:Example.si
///
DATABASE jportal_example_db
PACKAGE  sigen.org.jportal2.example.db
OUTPUT   ExampleTable
SERVER   PostgeSQL95

Table ExampleTable
   ID                            BIGSEQUENCE
   IntField                      INT
   StandardString                CHAR(64)
   TMStamp                       TIMESTAMP


KEY PKEY PRIMARY ID
KEY UKEY_UNIQUEINT_REF UNIQUE UniqueInt
//LINK foreign key section

PROC SelectOne
PROC Update

PROC SelectByStandardString
INPUT
     StandardString  =
OUTPUT
     ID       =
     IntField =
     TMStamp  =

```


Output:
=======

With `SQLAlchemy.generateBuiltIns` flag:

```python
########################################################################################################################
################## Generated Code. DO NOT CHANGE THIS CODE. Change it in the generator and regenerate ##################
########################################################################################################################


from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Any, Optional

import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import TextAsFrom

from bbdcommon.database.db_common import DBMixin, Base, DBColumn
from bbdcommon.database import db_types
from bbdcommon.database.processing import process_result_recs, process_result_rec, process_bind_params


EXAMPLETABLE_SCHEMA = "contentstore"


class DB_ExampleTable(Base, DBMixin):
    ID: int = DBColumn("id", sa.BigInteger(), sa.Sequence("EXAMPLETABLESEQ", metadata=Base.metadata, schema=EXAMPLETABLE_SCHEMA), primary_key=True, autoincrement=False)
    IntField: int = DBColumn("intfield", sa.Integer())
    StandardString: str = DBColumn("standardstring", db_types.NonNullableString(length=64))
    TMStamp: datetime = DBColumn("tmstamp", sa.DateTime(), default=datetime.now, onupdate=datetime.now)

    __schema__ = EXAMPLETABLE_SCHEMA

    def __init__(self, IntField: int, StandardString: str):
        super(DB_ExampleTable, self).__init__(
            IntField=IntField,
            StandardString=StandardString)


@dataclass
class DB_ExampleTableSelectOne:
    IntField: int = field(default=None)
    StandardString: str = field(default=None)
    TMStamp: datetime = field(default=None)

    @classmethod
    def get_statement(cls
                      , ID: int
                      ) -> TextAsFrom:
        statement = sa.text(
            "/* PROC CONTENTSTORE.ExampleTable.SelectOne */"
            "select"
            "  IntField"
            ", StandardString"
            ", TMStamp"
            " from CONTENTSTORE.ExampleTable"
            " where ID = :ID")
        text_statement = statement.columns(IntField=sa.types.Integer,
                                           StandardString=db_types.NonNullableString,
                                           TMStamp=sa.types.DateTime,
                                           )
        text_statement = text_statement.bindparams(ID=ID,
                                                   )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                ) -> Optional['DB_ExampleTableSelectOne']:
        params = process_bind_params(session, [sa.types.BigInteger,
                                               ], [ID,
                                                   ])
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(DB_ExampleTableSelectOne, session, [sa.types.Integer,
                                                                          db_types.NonNullableString,
                                                                          sa.types.DateTime,
                                                                          ], rec)

        return None


@dataclass
class DB_ExampleTableUpdate:

    @classmethod
    def get_statement(cls
                      , IntField: int
                      , StandardString: str
                      , TMStamp: datetime
                      , ID: int
                      ) -> TextAsFrom:
        statement = sa.text(
            "update CONTENTSTORE.ExampleTable"
            " set"
            "  IntField = :IntField"
            ", StandardString = :StandardString"
            ", TMStamp = :TMStamp"
            " where ID = :ID")
        text_statement = statement.columns()
        text_statement = text_statement.bindparams(IntField=IntField,
                                                   StandardString=StandardString,
                                                   TMStamp=TMStamp,
                                                   ID=ID,
                                                   )
        return text_statement

    @classmethod
    def execute(cls, session: Session, IntField: int
                , StandardString: str
                , TMStamp: datetime
                , ID: int
                ) -> None:
        params = process_bind_params(session, [sa.types.Integer,
                                               db_types.NonNullableString,
                                               sa.types.DateTime,
                                               sa.types.BigInteger,
                                               ], [IntField,
                                                   StandardString,
                                                   TMStamp,
                                                   ID,
                                                   ])
        res = session.execute(cls.get_statement(*params))
        res.close()


@dataclass
class DB_ExampleTableSelectByStandardString:
    ID: int = field(default=None)
    IntField: int = field(default=None)
    TMStamp: datetime = field(default=None)

    @classmethod
    def get_statement(cls
                      , StandardString: str
                      ) -> TextAsFrom:
        statement = sa.text(
            "/* PROC CONTENTSTORE.ExampleTable.SelectByStandardString */")
        text_statement = statement.columns(ID=sa.types.BigInteger,
                                           IntField=sa.types.Integer,
                                           TMStamp=sa.types.DateTime,
                                           )
        text_statement = text_statement.bindparams(StandardString=StandardString,
                                                   )
        return text_statement

    @classmethod
    def execute(cls, session: Session, StandardString: str
                ) -> List['DB_ExampleTableSelectByStandardString']:
        params = process_bind_params(session, [db_types.NonNullableString,
                                               ], [StandardString,
                                                   ])
        res = session.execute(cls.get_statement(*params))
        recs = res.fetchall()
        return process_result_recs(DB_ExampleTableSelectByStandardString, session, [sa.types.BigInteger,
                                                                                    sa.types.Integer,
                                                                                    sa.types.DateTime,
                                                                                    ], recs)

```
