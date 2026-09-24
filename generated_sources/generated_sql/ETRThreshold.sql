USE ExampleDatabase

DROP TABLE IF EXISTS ToDoList_App.ETRThreshold CASCADE;

CREATE TABLE ToDoList_App.ETRThreshold
( ID serial
, YOA integer
, StartAmount numeric(15, 2)
, EndAmount numeric(15, 2)
, TaxBaseAmount numeric(15, 2)
, Percentage numeric(15, 2)
, Threshold numeric(15, 2)
, UsrID varchar(16)
, TMStamp timestamp
);

ALTER TABLE ToDoList_App.ETRThreshold ALTER ID SET NOT NULL;
ALTER TABLE ToDoList_App.ETRThreshold ALTER YOA SET NOT NULL;
ALTER TABLE ToDoList_App.ETRThreshold ALTER StartAmount SET NOT NULL;
ALTER TABLE ToDoList_App.ETRThreshold ALTER UsrID SET NOT NULL;
ALTER TABLE ToDoList_App.ETRThreshold ALTER TMStamp SET NOT NULL;

ALTER TABLE ToDoList_App.ETRThreshold
 ADD CONSTRAINT ETRTHRESHOLD_PKEY PRIMARY KEY
  ( ID
  )
;

