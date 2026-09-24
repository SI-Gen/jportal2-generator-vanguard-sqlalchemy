USE ExampleDatabase

DROP TABLE IF EXISTS ToDoList_App.CompositeKeyItem CASCADE;

CREATE TABLE ToDoList_App.CompositeKeyItem
( YearNo integer
, ItemCode varchar(8)
, Amount integer
, Note varchar(32)
);

ALTER TABLE ToDoList_App.CompositeKeyItem ALTER YearNo SET NOT NULL;
ALTER TABLE ToDoList_App.CompositeKeyItem ALTER ItemCode SET NOT NULL;
ALTER TABLE ToDoList_App.CompositeKeyItem ALTER Amount SET NOT NULL;

ALTER TABLE ToDoList_App.CompositeKeyItem
 ADD CONSTRAINT COMPOSITEKEYITEM_PKEY PRIMARY KEY
  ( YearNo
  , ItemCode
  )
;

