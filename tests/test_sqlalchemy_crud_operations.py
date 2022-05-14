from conftest import postgres_db

def test_AlchemyInsert(generate_jportal, postgres_db, run_takeons):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoList
    import datetime

    session = Session(postgres_db)
    lst = DB_ToDoList(ListName="Alchemy Insert List 1", ListType=1,Description="XXX",LastUpdated=datetime.datetime.now())
    session.add(lst)
    session.flush()

    res = postgres_db.execute("SELECT ListName,ListType,Description,LastUpdated "
                              "FROM ToDoList_App.ToDoList ")
                              #"WHERE ID="+str(lst.ID))

    x = res.fetchall()

    #assert((res.fetchall())[0]==lst.ID)

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
