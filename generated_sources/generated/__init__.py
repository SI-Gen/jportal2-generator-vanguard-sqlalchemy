########################################################################################################################
################## Generated Code. DO NOT CHANGE THIS CODE. Change it in the generator and regenerate ##################
########################################################################################################################
from .db_TestJSON import DB_TestJSON
from .db_TestJSON import DB_TestJSONInsertReturning
from .db_TestJSON import DB_TestJSONIdentity
from .db_TestJSON import DB_TestJSONUpdate
from .db_TestJSON import DB_TestJSONSelectOne
from .db_TestJSON import DB_TestJSONDeleteOne
from .db_TestJSON import DB_TestJSONExists
from .db_TestSP import DB_TestSP
from .db_TestSP import DB_TestSPInsertReturning
from .db_TestSP import DB_TestSPIdentity
from .db_TestSP import DB_TestSPUpdate
from .db_TestSP import DB_TestSPSelectOne
from .db_TestSP import DB_TestSPDeleteOne
from .db_TestSP import DB_TestSPExists
from .db_TestSP import DB_TestSPCheckIfStoredProcCreated
from .db_ToDoList import DB_ToDoList
from .db_ToDoList import DB_ToDoListInsertReturning
from .db_ToDoList import DB_ToDoListIdentity
from .db_ToDoList import DB_ToDoListUpdate
from .db_ToDoList import DB_ToDoListSelectOne
from .db_ToDoList import DB_ToDoListDeleteOne
from .db_ToDoList import DB_ToDoListExists
from .db_ToDoList import DB_ToDoListSelectOneByListName
from .db_ToDoList import DB_ToDoListSelectByListType
from .db_ToDoList import DB_ToDoListSelectIDByListType
from .db_ToDoList import DB_ToDoListSelectListNameAndListTypeAsString
from .db_ToDoList import DB_ToDoListSelectWithDynamicQuery
from .db_ToDoList import DB_ToDoListStaticData
from .db_TestEnum import DB_TestEnum
from .db_TestEnum import DB_TestEnumInsertReturning
from .db_TestEnum import DB_TestEnumIdentity
from .db_TestEnum import DB_TestEnumUpdate
from .db_TestEnum import DB_TestEnumSelectOne
from .db_TestEnum import DB_TestEnumDeleteOne
from .db_TestEnum import DB_TestEnumExists
from .db_TestEnum import DB_TestEnumCheckIfStoredProcCreated
from .db_ToDo_Item import DB_ToDo_Item
from .db_ToDo_Item import DB_ToDo_ItemInsert
from .db_ToDo_Item import DB_ToDo_ItemIdentity
from .db_ToDo_Item import DB_ToDo_ItemUpdate
from .db_ToDo_Item import DB_ToDo_ItemSelectOne
from .db_ToDo_Item import DB_ToDo_ItemDeleteOne
from .db_ToDo_Item import DB_ToDo_ItemSelectByTodoList_ID
from .db_ToDo_Item import DB_ToDo_ItemUpdateByItemDescription

ALL_TABLES = [
    DB_TestEnum,
    DB_TestJSON,
    DB_TestSP,
    DB_ToDo_Item,
    DB_ToDoList,
]


ALL_PROCS = [
    DB_TestEnumCheckIfStoredProcCreated,
    DB_TestEnumDeleteOne,
    DB_TestEnumExists,
    DB_TestEnumIdentity,
    DB_TestEnumInsertReturning,
    DB_TestEnumSelectOne,
    DB_TestEnumUpdate,

    DB_TestJSONDeleteOne,
    DB_TestJSONExists,
    DB_TestJSONIdentity,
    DB_TestJSONInsertReturning,
    DB_TestJSONSelectOne,
    DB_TestJSONUpdate,

    DB_TestSPCheckIfStoredProcCreated,
    DB_TestSPDeleteOne,
    DB_TestSPExists,
    DB_TestSPIdentity,
    DB_TestSPInsertReturning,
    DB_TestSPSelectOne,
    DB_TestSPUpdate,

    DB_ToDo_ItemDeleteOne,
    DB_ToDo_ItemIdentity,
    DB_ToDo_ItemInsert,
    DB_ToDo_ItemSelectByTodoList_ID,
    DB_ToDo_ItemSelectOne,
    DB_ToDo_ItemUpdate,
    DB_ToDo_ItemUpdateByItemDescription,

    DB_ToDoListStaticData,
    DB_ToDoListDeleteOne,
    DB_ToDoListExists,
    DB_ToDoListIdentity,
    DB_ToDoListInsertReturning,
    DB_ToDoListSelectByListType,
    DB_ToDoListSelectIDByListType,
    DB_ToDoListSelectListNameAndListTypeAsString,
    DB_ToDoListSelectOne,
    DB_ToDoListSelectOneByListName,
    DB_ToDoListSelectWithDynamicQuery,
    DB_ToDoListUpdate,

]


__all__ = [
    "DB_TestEnum",
    "DB_TestJSON",
    "DB_TestSP",
    "DB_ToDo_Item",
    "DB_ToDoList",

    "DB_TestEnumCheckIfStoredProcCreated",
    "DB_TestEnumDeleteOne",
    "DB_TestEnumExists",
    "DB_TestEnumIdentity",
    "DB_TestEnumInsertReturning",
    "DB_TestEnumSelectOne",
    "DB_TestEnumUpdate",

    "DB_TestJSONDeleteOne",
    "DB_TestJSONExists",
    "DB_TestJSONIdentity",
    "DB_TestJSONInsertReturning",
    "DB_TestJSONSelectOne",
    "DB_TestJSONUpdate",

    "DB_TestSPCheckIfStoredProcCreated",
    "DB_TestSPDeleteOne",
    "DB_TestSPExists",
    "DB_TestSPIdentity",
    "DB_TestSPInsertReturning",
    "DB_TestSPSelectOne",
    "DB_TestSPUpdate",

    "DB_ToDo_ItemDeleteOne",
    "DB_ToDo_ItemIdentity",
    "DB_ToDo_ItemInsert",
    "DB_ToDo_ItemSelectByTodoList_ID",
    "DB_ToDo_ItemSelectOne",
    "DB_ToDo_ItemUpdate",
    "DB_ToDo_ItemUpdateByItemDescription",

    "DB_ToDoList",
    "DB_ToDoListDeleteOne",
    "DB_ToDoListExists",
    "DB_ToDoListIdentity",
    "DB_ToDoListInsertReturning",
    "DB_ToDoListSelectByListType",
    "DB_ToDoListSelectIDByListType",
    "DB_ToDoListSelectListNameAndListTypeAsString",
    "DB_ToDoListSelectOne",
    "DB_ToDoListSelectOneByListName",
    "DB_ToDoListSelectWithDynamicQuery",
    "DB_ToDoListUpdate",

]
