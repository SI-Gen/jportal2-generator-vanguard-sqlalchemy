USE ExampleDatabase

DROP TABLE IF EXISTS ToDoList_App.ToDo_Item CASCADE;

CREATE TABLE ToDoList_App.ToDo_Item
( ID int generated by default as identity
, TodoList_ID integer
, ItemName varchar(255)
, ItemDescription text
, LastUpdated timestamp
);

ALTER TABLE ToDoList_App.ToDo_Item ALTER ID SET NOT NULL;
ALTER TABLE ToDoList_App.ToDo_Item ALTER TodoList_ID SET NOT NULL;
ALTER TABLE ToDoList_App.ToDo_Item ALTER ItemName SET NOT NULL;
ALTER TABLE ToDoList_App.ToDo_Item ALTER ItemDescription SET NOT NULL;
ALTER TABLE ToDoList_App.ToDo_Item ALTER LastUpdated SET NOT NULL;

ALTER TABLE ToDoList_App.ToDo_Item
 ADD CONSTRAINT TODO_ITEM_PKEY PRIMARY KEY
  ( ID
  )
;
