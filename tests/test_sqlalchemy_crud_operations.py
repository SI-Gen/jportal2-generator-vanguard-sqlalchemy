from conftest import postgres14p2_db
from generated import DB_ToDoList


def test_AlchemyInsert(generate_jportal, postgres14p2_db, run_takeons):
    from sqlalchemy.orm import Session
    from generated import DB_ToDoList
    import datetime

    session = Session(postgres14p2_db)
    lst = DB_ToDoList(ListName="Alchemy Insert List 1",
                      ListType=1,
                      Description="XXX",
                      LastUpdated=datetime.datetime.now())
    session.add(lst)
    session.commit()
    session.expunge_all()
    res = postgres14p2_db.execute("SELECT ListName,ListType,Description,LastUpdated "
                              "FROM ToDoList_App.ToDoList ")
                              #"WHERE ID="+str(lst.ID))

    x = res.fetchall()

    #assert((res.fetchall())[0]==lst.ID)

def test_AlchemySelectByPK(generate_jportal, postgres14p2_db, run_takeons):
    from sqlalchemy.orm import Session
    from sqlalchemy import select
    from generated import DB_ToDoList
    import datetime

    #Insert test record
    session = Session(postgres14p2_db)
    lst = DB_ToDoList(ListName="Alchemy Insert List 1",
                      ListType=1,
                      Description="XXX",
                      LastUpdated=datetime.datetime.now())
    session.add(lst)
    session.commit()

    stmt = session.query(DB_ToDoList).get(lst.ID)
    res = session.execute(stmt)
    lst=res.fetchall()
    lst=lst[0]
    assert(lst.ID==id)
    assert(lst.ListName=='Takeon Test List 2')
    assert(lst.Description=='Take on test 2 list description')
    assert(lst.LastUpdated is not None)
    assert(lst.LastUpdated.date()==datetime.date.today())
    session.add(lst)
    session.flush()
