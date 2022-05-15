import pytest


@pytest.fixture
def todolist_single_test_record():
    import datetime
    from generated import DB_ToDoList

    return DB_ToDoList(ListName="LIST", ListType=1, Description="Desc", LastUpdated=datetime.date(2020, 1, 1))


@pytest.fixture
def todoitem_single_test_record():
    import datetime
    from generated import DB_ToDo_Item
    return DB_ToDo_Item(TodoList_ID=None,
                        ItemName="Item 1",
                        ItemDescription="Description",
                        LastUpdated=datetime.datetime.now())


def test_JPortalInsertReturning(generate_jportal, postgres14p2_db, run_takeons):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoListInsertReturning
    import datetime

    session = Session(postgres14p2_db)
    rec = DB_ToDoListInsertReturning.execute(session,
                                             "JPortalInsert List",
                                             1,
                                             "Jportal Insert List Description",
                                             datetime.datetime.now())
    session.commit()

    res = postgres14p2_db.execute("SELECT ID, ListName,ListType,Description,LastUpdated "
                                    "FROM ToDoList_App.ToDoList "
                                    "WHERE ID=" + str(rec.ID))

    x = res.fetchone()

    assert(x[0] == rec.ID)

def test_JPortalInsertWithoutReturning(generate_jportal, postgres14p2_db, run_takeons, todolist_single_test_record):
    from sqlalchemy.orm import Session
    from generated import DB_ToDo_ItemInsert
    import datetime

    session = Session(postgres14p2_db)

    #Insert parent record
    session.add(todolist_single_test_record)
    session.flush()
    DB_ToDo_ItemInsert.execute(session,
                                     TodoList_ID=todolist_single_test_record.ID,
                                     ItemName="Item 1",
                                     ItemDescription="Description",
                                     LastUpdated=datetime.datetime.now())
    session.commit()

    res = postgres14p2_db.execute("SELECT TodoList_ID, ItemName,ItemDescription "
                              "FROM ToDoList_App.ToDo_Item "
                              "WHERE TodoList_ID=" + str(todolist_single_test_record.ID))

    x = res.fetchone()

    assert(x[0] == todolist_single_test_record.ID)
    assert(x[1] == "Item 1")
    assert(x[2] == "Description")


def test_JPortalSelectOne(generate_jportal, postgres14p2_db, run_takeons, todolist_single_test_record):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoListSelectOne
    import datetime

    session = Session(postgres14p2_db)

    session.add(todolist_single_test_record)
    session.commit()

    rec = DB_ToDoListSelectOne.execute(session, todolist_single_test_record.ID)

    assert(rec.ListName == "LIST")
    assert(rec.ListType == 1)
    assert(rec.Description == "Desc")
    assert(rec.LastUpdated == datetime.datetime(2020, 1, 1, 0, 0))

def test_JPortalExists(generate_jportal, postgres14p2_db, run_takeons, todolist_single_test_record):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoListExists

    session = Session(postgres14p2_db)

    session.add(todolist_single_test_record)
    session.commit()

    rec = DB_ToDoListExists.execute(session, todolist_single_test_record.ID)
    assert(rec.noOf == 1)

    rec = DB_ToDoListExists.execute(session, -500)
    assert(rec.noOf == 0)

def test_JPortalDeleteOne(generate_jportal, postgres14p2_db, run_takeons, todolist_single_test_record):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoListDeleteOne, DB_ToDoListSelectOne

    session = Session(postgres14p2_db)

    session.add(todolist_single_test_record)
    session.commit()

    rec = DB_ToDoListSelectOne.execute(session, todolist_single_test_record.ID)
    assert rec

    DB_ToDoListDeleteOne.execute(session, todolist_single_test_record.ID)
    session.expunge_all() #Expunge all objects from the session to force Alchmemy to look at the database instead of memory

    rec = DB_ToDoListSelectOne.execute(session, todolist_single_test_record.ID)
    assert (rec is None)


def test_JPortalUpdate(generate_jportal, postgres14p2_db, run_takeons, todolist_single_test_record, todoitem_single_test_record):
    from sqlalchemy.orm import Session
    from generated import DB_ToDo_ItemUpdate, DB_ToDo_ItemSelectOne
    import datetime

    session = Session(postgres14p2_db)

    session.add(todolist_single_test_record)
    session.flush()
    todoitem_single_test_record.TodoList_ID = todolist_single_test_record.ID
    session.add(todoitem_single_test_record)
    session.commit()

    DB_ToDo_ItemUpdate.execute(session, ID=todoitem_single_test_record.ID,
                               ItemName="UPDATED",
                               TodoList_ID=todoitem_single_test_record.TodoList_ID,
                               LastUpdated=datetime.datetime(2021, 1, 1, 0, 0),
                               ItemDescription=todoitem_single_test_record.ItemDescription)
    session.commit()

    #TODO: Check with normal alchmemy select instead
    rec = DB_ToDo_ItemSelectOne.execute(session, todoitem_single_test_record.ID)

    assert(rec.ItemName == "UPDATED")
    assert(rec.TodoList_ID == todoitem_single_test_record.TodoList_ID)
    assert(rec.ItemName == todoitem_single_test_record.ItemName)
    assert(rec.ItemDescription == todoitem_single_test_record.ItemDescription)
    assert(rec.LastUpdated == datetime.datetime(2021, 1, 1, 0, 0))

def test_JPortalDynamicSQL(generate_jportal, postgres14p2_db, run_takeons, todolist_single_test_record):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoListSelectWithDynamicQuery
    import datetime

    session = Session(postgres14p2_db)

    session.add(todolist_single_test_record)
    session.commit()

    recs = DB_ToDoListSelectWithDynamicQuery.execute(session, todolist_single_test_record.ListName, f"ID = {todolist_single_test_record.ID}")
    rec = recs[0]
    assert(rec.ListName == "LIST")
    assert(rec.ListType == 1)
    assert(rec.Description == "Desc")
    assert(rec.LastUpdated == datetime.datetime(2020, 1, 1, 0, 0))
