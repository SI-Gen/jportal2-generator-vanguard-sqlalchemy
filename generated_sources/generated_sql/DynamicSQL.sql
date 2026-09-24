USE ExampleDatabase

DROP TABLE IF EXISTS ToDoList_App.DynamicSQL CASCADE;

CREATE TABLE ToDoList_App.DynamicSQL
( Id integer
, Sent smallint
, SendDateTime timestamp
);

ALTER TABLE ToDoList_App.DynamicSQL ALTER Id SET NOT NULL;
ALTER TABLE ToDoList_App.DynamicSQL ALTER Sent SET NOT NULL;

ALTER TABLE ToDoList_App.DynamicSQL
 ADD CONSTRAINT DYNAMICSQL_PKEY PRIMARY KEY
  ( Id
  )
;

