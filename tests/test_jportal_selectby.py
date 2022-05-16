import pytest
from generated import DB_ToDoList

@pytest.fixture
def todolist_single_test_record():
    import datetime
    return DB_ToDoList(ListName="LIST", ListType=1, Description="Desc", LastUpdated=datetime.date(2020, 1, 1))


@pytest.fixture
def todoitem_single_test_record():
    import datetime
    from generated import DB_ToDo_Item
    return DB_ToDo_Item(TodoList_ID=None,
                        ItemName="Item 1",
                        ItemDescription="Description",
                        LastUpdated=datetime.datetime.now())


def test_JPortalSelectOneBySimpleStandard(generate_jportal, postgres14p2_db, run_takeons, todolist_single_test_record):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoListSelectOneByListName
    import datetime

    session = Session(postgres14p2_db)

    session.add(todolist_single_test_record)
    session.commit()

    rec = DB_ToDoListSelectOneByListName.execute(session, todolist_single_test_record.ListName)

    assert (rec.ListName == "LIST")
    assert (rec.ListType == 1)
    assert (rec.Description == "Desc")
    assert (rec.LastUpdated == datetime.datetime(2020, 1, 1, 0, 0))

def test_JPortalSelectByReturningList(generate_jportal, postgres14p2_db, run_takeons):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoListSelectByListType
    import datetime

    session = Session(postgres14p2_db)
    rec1 = DB_ToDoList(ListName="LIST 1", ListType=999, Description="Desc 1", LastUpdated=datetime.date(2020, 1, 1))
    rec2 = DB_ToDoList(ListName="LIST 2", ListType=999, Description="Desc 2", LastUpdated=datetime.date(2020, 1, 1))

    session.add(rec1)
    session.add(rec2)

    session.commit()

    rec = DB_ToDoListSelectByListType.execute(session, 999)
    assert( len(rec) == 2)

    assert (rec[0].ListName == "LIST 1")
    assert (rec[1].ListName == "LIST 2")

def test_JPortalSelectByReturningCustomFields(generate_jportal, postgres14p2_db, run_takeons):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoListSelectIDByListType
    import datetime

    session = Session(postgres14p2_db)
    rec1 = DB_ToDoList(ListName="LIST 1", ListType=888, Description="Desc 1", LastUpdated=datetime.date(2020, 1, 1))
    rec2 = DB_ToDoList(ListName="LIST 2", ListType=888, Description="Desc 2", LastUpdated=datetime.date(2020, 1, 1))

    session.add(rec1)
    session.add(rec2)

    session.commit()

    rec = DB_ToDoListSelectIDByListType.execute(session, 888)
    assert( len(rec) == 2)
    assert (rec[0].ID == rec1.ID)
    assert (rec[1].ID == rec2.ID)

    # Finally, check that only the ID field is generated
    assert(not hasattr(DB_ToDoListSelectIDByListType, 'ListType'))
    assert(not hasattr(DB_ToDoListSelectIDByListType, 'Description'))
    assert(not hasattr(DB_ToDoListSelectIDByListType, 'LastUpdated'))