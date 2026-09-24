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



COMPOSITEKEYITEM_SCHEMA = "todolist_app"
class DB_CompositeKeyItem(Base, DBMixin):
    YearNo: int = DBColumn("yearno", sa.Integer(),
        primary_key=True,
        autoincrement=False)
    ItemCode: str = DBColumn("itemcode", db_types.NonNullableString(length=8),
        primary_key=True,
        autoincrement=False)
    Amount: int = DBColumn("amount", sa.Integer())
    Note: Optional[str] = DBColumn("note", sa.String(length=32),
        nullable=True)

    __schema__ = COMPOSITEKEYITEM_SCHEMA

    def __init__(self,
        YearNo: int,
        ItemCode: str,
        Amount: int,
        Note: Optional[str]):
        self.YearNo = YearNo
        self.ItemCode = ItemCode
        self.Amount = Amount
        self.Note = Note

@dataclass
class DB_CompositeKeyItemInsert:
    

    @classmethod
    def get_statement(cls
                     , YearNo: int
                     , ItemCode: str
                     , Amount: int
                     , Note: Optional[str]
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = ""
            tail = ""
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.CompositeKeyItem.Insert */"
                        "insert into ToDoList_App.CompositeKeyItem ("
                        "  YearNo,"
                        "  ItemCode,"
                        "  Amount,"
                        "  Note"
                        " ) "
                        " values ("
                        "  :YearNo,"
                        "  :ItemCode,"
                        "  :Amount,"
                        "  :Note"
                        " )")

        text_statement = statement.columns()
        text_statement = text_statement.bindparams(YearNo=YearNo,
                                         ItemCode=ItemCode,
                                         Amount=Amount,
                                         Note=Note,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, YearNo: int
                     , ItemCode: str
                     , Amount: int
                     , Note: Optional[str]
                     ) -> None:
        params = process_bind_params(
            session,
            [
                sa.types.Integer,
                db_types.NonNullableString,
                sa.types.Integer,
                sa.types.String,
            ],
            [
                YearNo,
                ItemCode,
                Amount,
                Note,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        res.close()

@dataclass
class DB_CompositeKeyItemSelectOne:
    #Inputs
    YearNo: int
    ItemCode: str

    #Outputs
    Amount: int
    Note: Optional[str]

    @classmethod
    def get_statement(cls
                     , YearNo: int
                     , ItemCode: str
                     ) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = " OUTPUT (Amount,Note)"
            tail = " RETURNING Amount Note"
            #session.bind.dialect.name

        statement = sa.text(
                        "/* PROC ToDoList_App.CompositeKeyItem.SelectOne */"
                        "select"
                        "  Amount"
                        ", Note"
                        " from ToDoList_App.CompositeKeyItem"
                        " where YearNo = :YearNo"
                        "   and ItemCode = :ItemCode")

        text_statement = statement.columns(Amount=sa.types.Integer,
                                      Note=sa.types.String,
                                      )
        text_statement = text_statement.bindparams(YearNo=YearNo,
                                         ItemCode=ItemCode,
                                         )
        return text_statement

    @classmethod
    def execute(cls, session: Session, YearNo: int
                     , ItemCode: str
                     ) -> Optional['DB_CompositeKeyItemSelectOne']:
        params = process_bind_params(
            session,
            [
                sa.types.Integer,
                db_types.NonNullableString,
            ],
            [
                YearNo,
                ItemCode,
            ],
        )
        res = session.execute(cls.get_statement(*params))
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(
                DB_CompositeKeyItemSelectOne,
                session,
                [
                    sa.types.Integer,
                    sa.types.String,
                ],
                rec,
                YearNo=YearNo,
                ItemCode=ItemCode,
            )

        return None
