from conftest import postgres_db

def test_JPortalInsertReturning(generate_jportal, postgres_db, run_takeons):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoListInsert
    import datetime

    session = Session(postgres_db)
    rec = DB_ToDoListInsert.execute(session,"JPortalInsert List", 1,"Jportal Insert List Description",datetime.datetime.now())
    session.commit()

    res = postgres_db.execute("SELECT ID, ListName,ListType,Description,LastUpdated "
                              "FROM ToDoList_App.ToDoList "
                              "WHERE ID="+str(rec.ID))

    x = res.fetchall()

    assert(x[0] == rec.ID)

def test_JPortalInsertWithoutReturning(generate_jportal, postgres_db, run_takeons):
    from sqlalchemy.orm import Session
    from generated import DB_ToDo_ItemInsert
    import datetime

    session = Session(postgres_db)

    res = postgres_db.execute(
        f"/* PROC ToDoList_App.ToDoList.Insert */"
        f"insert into ToDoList_App.ToDoList ("
        f"  ID,"
        f"  ListName,"
        f"  ListType,"
        f"  Description,"
        f"  LastUpdated"
        f" ) "
        f" values ("
        f" default ,"
        f"  'LIST',"
        f"  1,"
        f"  'Desc',"
        f"  '2020-01-01'"
        f" )"
        f"returning ID")
    id = res.fetchone()[0]

    rec = DB_ToDo_ItemInsert.execute(session,TodoList_ID=id, ItemName="Item 1", ItemDescription="Description", LastUpdated=datetime.datetime.now())
    session.commit()

    res = postgres_db.execute("SELECT TodoList_ID, ItemName,ItemDescription "
                              "FROM ToDoList_App.ToDo_Item "
                              "WHERE TodoList_ID="+str(id))

    x = res.fetchone()

    assert(x[0] == id)
    assert(x[1] == "Item 1")
    assert(x[2] == "Description")


def test_JPortalSelectOne(generate_jportal, postgres_db, run_takeons):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoListSelectOne
    import datetime

    res = postgres_db.execute(
        f"/* PROC ToDoList_App.ToDoList.Insert */"
        f"insert into ToDoList_App.ToDoList ("
        f"  ID,"
        f"  ListName,"
        f"  ListType,"
        f"  Description,"
        f"  LastUpdated"
        f" ) "
        f" values ("
        f" default ,"
        f"  'LIST',"
        f"  1,"
        f"  'Desc',"
        f"  '2020-01-01'"
        f" )"
        f"returning ID")
    id = res.fetchone()[0]
    session = Session(postgres_db)
    rec = DB_ToDoListSelectOne.execute(session, id)

    assert(rec.ListName == "LIST")
    assert(rec.ListType == 1)
    assert(rec.Description == "Desc")
    assert(rec.LastUpdated == datetime.date(2020, 1, 1))



def test_AlchemySelectByPK(generate_jportal, postgres_db, run_takeons):
    from sqlalchemy.orm import Session
    from sqlalchemy import select
    from generated import DB_ToDoList
    import datetime

    #Insert test record
    res = postgres_db.execute("INSERT INTO ToDoList_App.ToDoList(ListName,ListType,Description,LastUpdated) "
                              "VALUES ('Takeon Test List 2', 1, 'Take on test 2 list description', CURRENT_DATE ) "
                              "RETURNING ID")
    id = res.fetchone()[0]

    session = Session(postgres_db)
    stmt = select(DB_ToDoList).where(DB_ToDoList.ID == id)
    lst = (DB_ToDoList) (session.scalar(stmt))
    assert(lst.ID==id)
    assert(lst.ListName=='Takeon Test List 2')
    assert(lst.Description=='Take on test 2 list description')
    assert(lst.LastUpdated is not None)
    assert(lst.LastUpdated.date()==datetime.date.today())
    session.add(lst)
    session.flush()
