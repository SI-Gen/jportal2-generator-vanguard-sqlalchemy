import dataclasses
import datetime
import enum
import inspect
from decimal import Decimal
from typing import Optional, get_type_hints

from generated import (
    DB_CompositeKeyItem,
    DB_CompositeKeyItemSelectOne,
    DB_ETRThreshold,
    DB_ETRThresholdSelectOne,
    DB_TestEnum,
    DB_TestEnumInsertReturning,
    DB_ToDoList,
    DB_ToDoListSelectListNameAndListTypeAsString,
    DB_ToDoListSelectOne,
)


def test_float_fields_are_annotated_as_int():
    table_hints = get_type_hints(DB_ETRThreshold)
    select_hints = get_type_hints(DB_ETRThresholdSelectOne)

    assert table_hints["StartAmount"] is int
    assert table_hints["EndAmount"] == Optional[int]
    assert table_hints["TaxBaseAmount"] == Optional[int]
    assert table_hints["Percentage"] == Optional[int]
    assert table_hints["Threshold"] == Optional[int]

    assert select_hints["StartAmount"] is int
    assert select_hints["EndAmount"] == Optional[int]
    assert select_hints["ID"] is int


def test_selectone_copies_inputs_that_are_not_outputs():
    select_one_fields = [
        field.name for field in dataclasses.fields(DB_ToDoListSelectOne)
    ]
    other_proc_fields = [
        field.name
        for field in dataclasses.fields(DB_ToDoListSelectListNameAndListTypeAsString)
    ]

    assert select_one_fields[0] == "ID"
    assert "ID" not in other_proc_fields

    rebate_fields = [
        field.name for field in dataclasses.fields(DB_ETRThresholdSelectOne)
    ]
    assert rebate_fields[0] == "ID"
    assert "ID=ID" in inspect.getsource(DB_ETRThresholdSelectOne.execute)


def test_selectone_returns_lookup_key_and_float_values(postgres14p2_db):
    from sqlalchemy.orm import Session

    session = Session(postgres14p2_db)
    row = DB_ETRThreshold(
        YOA=2024,
        StartAmount=100,
        EndAmount=None,
        TaxBaseAmount=1500,
        Percentage=10,
        Threshold=500,
        UsrID="tester",
    )
    session.add(row)
    session.commit()

    rec = DB_ETRThresholdSelectOne.execute(session, row.ID)
    assert rec is not None
    assert rec.ID == row.ID
    assert rec.YOA == 2024
    assert rec.StartAmount == Decimal("100.00")
    assert rec.EndAmount is None
    assert rec.TaxBaseAmount == Decimal("1500.00")
    assert rec.Percentage == Decimal("10.00")
    assert rec.Threshold == Decimal("500.00")
    assert rec.UsrID == "tester"
    assert rec.TMStamp is not None


def test_selectone_returns_lookup_key_with_enum_output(postgres14p2_db):
    from sqlalchemy.orm import Session

    session = Session(postgres14p2_db)
    row = DB_ToDoList(
        ListName="LIST",
        ListType=DB_ToDoList.ListTypeEnum.Private,
        Description="Desc",
        LastUpdated=datetime.datetime(2020, 1, 1),
    )
    session.add(row)
    session.commit()

    rec = DB_ToDoListSelectOne.execute(session, row.ID)
    assert rec is not None

    assert rec.ID == row.ID
    assert rec.ListName == "LIST"
    assert rec.ListType == DB_ToDoListSelectOne.ListTypeEnum.Private


def test_selectone_returns_every_primary_key_field(postgres14p2_db):
    from sqlalchemy.orm import Session

    session = Session(postgres14p2_db)
    row = DB_CompositeKeyItem(
        YearNo=2024,
        ItemCode="RATE",
        Amount=15,
        Note=None,
    )
    session.add(row)
    session.commit()

    rec = DB_CompositeKeyItemSelectOne.execute(session, 2024, "RATE")
    assert rec is not None

    assert [field.name for field in dataclasses.fields(DB_CompositeKeyItemSelectOne)][
        :2
    ] == ["YearNo", "ItemCode"]
    assert rec.YearNo == 2024
    assert rec.ItemCode == "RATE"
    assert rec.Amount == 15
    assert rec.Note is None


def test_character_enums_stay_string_enums():
    node_type = DB_TestEnum.NodeTypeCharEnEnum
    int_enum = DB_TestEnum.IntEnEnum

    assert issubclass(node_type, enum.Enum)
    assert not issubclass(node_type, enum.IntEnum)
    assert node_type.Normal.value == "N"
    assert node_type.Error.value == "E"
    assert node_type.Completed.value == "C"
    assert node_type.DeadLetter.value == "D"
    assert node_type.Storage.value == "S"
    assert node_type.Fail.value == "F"

    assert issubclass(int_enum, enum.IntEnum)
    assert int_enum.First == 1
    assert int_enum.Second == 2

    execute_source = inspect.getsource(DB_TestEnumInsertReturning.execute)
    assert "isinstance(NodeTypeCharEn, enum.Enum)" in execute_source
    assert "isinstance(IntEn, enum.IntEnum)" in execute_source

    bound = (
        node_type.Normal.value
        if isinstance(node_type.Normal, enum.Enum)
        else node_type.Normal
    )
    assert bound == "N"
