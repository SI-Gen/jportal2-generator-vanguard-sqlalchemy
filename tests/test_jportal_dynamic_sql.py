import pytest
import sqlalchemy as sa
from sqlalchemy.orm import Session

from generated.db_DynamicSQL import (
    DB_DynamicSQLBatchMarkAsSent,
    DB_DynamicSQLMarkAll,
    DB_DynamicSQLMarkOne,
    DB_DynamicSQLMarkSelected,
)


@pytest.fixture
def dynamic_session():
    engine = sa.create_engine("sqlite:///:memory:")
    session = Session(bind=engine)
    session.execute(sa.text(
        "CREATE TABLE DynamicSQL (Id INTEGER PRIMARY KEY, Sent INTEGER, "
        "SendDateTime TIMESTAMP)"
    ))
    session.execute(sa.text(
        "INSERT INTO DynamicSQL (Id, Sent) VALUES (1, 0), (2, 0), (3, 0)"
    ))
    try:
        yield session
    finally:
        session.close()
        engine.dispose()


@pytest.mark.parametrize("proc, kwargs, expected_sent", [
    (DB_DynamicSQLBatchMarkAsSent, {"SentIds": "1, 3"}, [1, 0, 1]),
    (DB_DynamicSQLMarkSelected, {"Sent": 2, "SentIds": "1, 3"}, [2, 0, 2]),
    (DB_DynamicSQLMarkOne, {"Id": 2}, [0, 1, 0]),
    (DB_DynamicSQLMarkAll, {}, [1, 1, 1]),
], ids=["dynamic-only", "mixed", "input-only", "no-parameters"])
def test_execute_forwards_procedure_arguments(dynamic_session, proc, kwargs, expected_sent):
    assert proc.execute(dynamic_session, **kwargs) is None

    rows = dynamic_session.execute(sa.text(
        "SELECT Sent, SendDateTime FROM DynamicSQL ORDER BY Id"
    )).fetchall()
    assert [row.Sent for row in rows] == expected_sent
    if proc is DB_DynamicSQLBatchMarkAsSent:
        assert [row.SendDateTime is not None for row in rows] == [True, False, True]
