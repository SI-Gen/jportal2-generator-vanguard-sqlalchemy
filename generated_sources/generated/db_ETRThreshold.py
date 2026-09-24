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
from .common.processing import process_bind_params, process_result_rec



ETRTHRESHOLD_SCHEMA = "todolist_app"
class DB_ETRThreshold(Base, DBMixin):
    ID: int = DBColumn("id", sa.Integer(),
        sa.Sequence("ETRTHRESHOLDSEQ", metadata=Base.metadata, schema=ETRTHRESHOLD_SCHEMA),
        primary_key=True,
        autoincrement=False)
    YOA: int = DBColumn("yoa", sa.Integer())
    StartAmount: int = DBColumn("startamount", sa.Numeric(precision=15, scale=2))
    EndAmount: Optional[int] = DBColumn("endamount", sa.Numeric(precision=15, scale=2),
        nullable=True)
    TaxBaseAmount: Optional[int] = DBColumn("taxbaseamount", sa.Numeric(precision=15, scale=2),
        nullable=True)
    Percentage: Optional[int] = DBColumn("percentage", sa.Numeric(precision=15, scale=2),
        nullable=True)
    Threshold: Optional[int] = DBColumn("threshold", sa.Numeric(precision=15, scale=2),
        nullable=True)
    UsrID: str = DBColumn("usrid", db_types.NonNullableString(length=16))
    TMStamp: datetime = DBColumn("tmstamp", sa.DateTime(),
        default=datetime.now,
        onupdate=datetime.now)

    __schema__ = ETRTHRESHOLD_SCHEMA

    def __init__(self,
        YOA: int,
        StartAmount: int,
        EndAmount: Optional[int],
        TaxBaseAmount: Optional[int],
        Percentage: Optional[int],
        Threshold: Optional[int],
        UsrID: str):
        self.YOA = YOA
        self.StartAmount = StartAmount
        self.EndAmount = EndAmount
        self.TaxBaseAmount = TaxBaseAmount
        self.Percentage = Percentage
        self.Threshold = Threshold
        self.UsrID = UsrID

@dataclass
class DB_ETRThresholdInsert:
    

    @classmethod
    def get_statement(cls
                     , YOA: int
                     , StartAmount: int
                     , EndAmount: Optional[int]
                     , TaxBaseAmount: Optional[int]
                     , Percentage: Optional[int]
                     , Threshold: Optional[int]
                     , UsrID: str
                     , TMStamp: datetime
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.ETRThreshold.Insert */"
                        "insert into ToDoList_App.ETRThreshold ("
                        "  YOA,"
                        "  StartAmount,"
                        "  EndAmount,"
                        "  TaxBaseAmount,"
                        "  Percentage,"
                        "  Threshold,"
                        "  UsrID,"
                        "  TMStamp"
                        " ) "
                        " values ("
                        "  :YOA,"
                        "  :StartAmount,"
                        "  :EndAmount,"
                        "  :TaxBaseAmount,"
                        "  :Percentage,"
                        "  :Threshold,"
                        "  :UsrID,"
                        "  :TMStamp"
                        " )")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(YOA=YOA,
                                         StartAmount=StartAmount,
                                         EndAmount=EndAmount,
                                         TaxBaseAmount=TaxBaseAmount,
                                         Percentage=Percentage,
                                         Threshold=Threshold,
                                         UsrID=UsrID,
                                         TMStamp=TMStamp,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, YOA: int
                     , StartAmount: int
                     , EndAmount: Optional[int]
                     , TaxBaseAmount: Optional[int]
                     , Percentage: Optional[int]
                     , Threshold: Optional[int]
                     , UsrID: str
                     , TMStamp: datetime
                     ) -> None:
        params = process_bind_params(
            session,
            [
                sa.types.Integer,
                sa.types.Numeric,
                sa.types.Numeric,
                sa.types.Numeric,
                sa.types.Numeric,
                sa.types.Numeric,
                db_types.NonNullableString,
                sa.types.DateTime,
            ],
            [
                YOA,
                StartAmount,
                EndAmount,
                TaxBaseAmount,
                Percentage,
                Threshold,
                UsrID,
                TMStamp,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        res.close()

@dataclass
class DB_ETRThresholdSelectOne:
    #Inputs
    ID: int

    #Outputs
    YOA: int
    StartAmount: int
    EndAmount: Optional[int]
    TaxBaseAmount: Optional[int]
    Percentage: Optional[int]
    Threshold: Optional[int]
    UsrID: str
    TMStamp: datetime

    @classmethod
    def get_statement(cls
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (YOA,StartAmount,EndAmount,TaxBaseAmount,Percentage,Threshold,UsrID,TMStamp)"
            tail = " RETURNING YOA StartAmount EndAmount TaxBaseAmount Percentage Threshold UsrID TMStamp"
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.ETRThreshold.SelectOne */"
                        "select"
                        "  YOA"
                        ", StartAmount"
                        ", EndAmount"
                        ", TaxBaseAmount"
                        ", Percentage"
                        ", Threshold"
                        ", UsrID"
                        ", TMStamp"
                        " from ToDoList_App.ETRThreshold"
                        " where ID = :ID")

        text_statement = statement.columns(YOA=sa.types.Integer,
                                      StartAmount=sa.types.Numeric,
                                      EndAmount=sa.types.Numeric,
                                      TaxBaseAmount=sa.types.Numeric,
                                      Percentage=sa.types.Numeric,
                                      Threshold=sa.types.Numeric,
                                      UsrID=db_types.NonNullableString,
                                      TMStamp=sa.types.DateTime,
                                      )
        text_statement = text_statement.bindparams(ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, ID: int
                     ) -> Optional['DB_ETRThresholdSelectOne']:
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
                DB_ETRThresholdSelectOne,
                session,
                [
                    sa.types.Integer,
                    sa.types.Numeric,
                    sa.types.Numeric,
                    sa.types.Numeric,
                    sa.types.Numeric,
                    sa.types.Numeric,
                    db_types.NonNullableString,
                    sa.types.DateTime,
                ],
                rec,
                ID=ID,
            )

        return None

@dataclass
class DB_ETRThresholdUpdate:
    

    @classmethod
    def get_statement(cls
                     , YOA: int
                     , StartAmount: int
                     , EndAmount: Optional[int]
                     , TaxBaseAmount: Optional[int]
                     , Percentage: Optional[int]
                     , Threshold: Optional[int]
                     , UsrID: str
                     , TMStamp: datetime
                     , ID: int
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        "update ToDoList_App.ETRThreshold"
                        " set"
                        "  YOA = :YOA"
                        ", StartAmount = :StartAmount"
                        ", EndAmount = :EndAmount"
                        ", TaxBaseAmount = :TaxBaseAmount"
                        ", Percentage = :Percentage"
                        ", Threshold = :Threshold"
                        ", UsrID = :UsrID"
                        ", TMStamp = :TMStamp"
                        " where ID = :ID")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(YOA=YOA,
                                         StartAmount=StartAmount,
                                         EndAmount=EndAmount,
                                         TaxBaseAmount=TaxBaseAmount,
                                         Percentage=Percentage,
                                         Threshold=Threshold,
                                         UsrID=UsrID,
                                         TMStamp=TMStamp,
                                         ID=ID,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, YOA: int
                     , StartAmount: int
                     , EndAmount: Optional[int]
                     , TaxBaseAmount: Optional[int]
                     , Percentage: Optional[int]
                     , Threshold: Optional[int]
                     , UsrID: str
                     , TMStamp: datetime
                     , ID: int
                     ) -> None:
        params = process_bind_params(
            session,
            [
                sa.types.Integer,
                sa.types.Numeric,
                sa.types.Numeric,
                sa.types.Numeric,
                sa.types.Numeric,
                sa.types.Numeric,
                db_types.NonNullableString,
                sa.types.DateTime,
                sa.types.Integer,
            ],
            [
                YOA,
                StartAmount,
                EndAmount,
                TaxBaseAmount,
                Percentage,
                Threshold,
                UsrID,
                TMStamp,
                ID,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        res.close()
