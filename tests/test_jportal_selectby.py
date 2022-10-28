import pytest
from generated import DB_ToDoList

@pytest.fixture
def todolist_single_test_record():
    import datetime
    # return DB_ToDoList(ListName="LIST", ListType=1, Description="Desc", LastUpdated=datetime.date(2020, 1, 1))
    return DB_ToDoList(ListName="LIST", ListType=DB_ToDoList.ListTypeEnum.Private, Description="Desc", LastUpdated=datetime.date(2020, 1, 1))


@pytest.fixture
def todoitem_single_test_record():
    import datetime
    from generated import DB_ToDo_Item
    return DB_ToDo_Item(TodoList_ID=None,
                        ItemName="Item 1",
                        ItemDescription="Description",
                        LastUpdated=datetime.datetime.now())


def test_JPortalSelectOneBySimpleStandard(postgres14p2_db, todolist_single_test_record):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoListSelectOneByListName
    import datetime

    session = Session(postgres14p2_db)

    session.add(todolist_single_test_record)
    session.commit()

    rec = DB_ToDoListSelectOneByListName.execute(session, todolist_single_test_record.ListName)

    assert (rec.ListName == "LIST")
    assert (rec.ListType == DB_ToDoListSelectOneByListName.ListTypeEnum.Private)
    assert (rec.Description == "Desc")
    assert (rec.LastUpdated == datetime.datetime(2020, 1, 1, 0, 0))
    session.commit()

def test_JPortalSelectByReturningList(postgres14p2_db):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoListSelectByListType
    import datetime

    session = Session(postgres14p2_db)
    rec1 = DB_ToDoList(ListName="LIST 1", ListType=DB_ToDoList.ListTypeEnum.Public, Description="Desc 1", LastUpdated=datetime.date(2020, 1, 1))
    rec2 = DB_ToDoList(ListName="LIST 2", ListType=DB_ToDoList.ListTypeEnum.Public, Description="Desc 2", LastUpdated=datetime.date(2020, 1, 1))

    session.add(rec1)
    session.add(rec2)

    session.commit()

    rec = DB_ToDoListSelectByListType.execute(session, DB_ToDoList.ListTypeEnum.Public)
    assert( len(rec) == 2)

    assert (rec[0].ListName == "LIST 1")
    assert (rec[1].ListName == "LIST 2")
    session.commit()

def test_JPortalSelectByReturningCustomFields(postgres14p2_db):
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
    session.commit()