from typing import Any, Dict, List, Type


class InsertReturnHelper:
    _dialect_dict: Dict[str, Type["InsertReturnHelper"]] = {}
    _sql_dialect: str

    def __init__(self, is_insert: bool, outputs: List[str]):
        self.sequence: str
        self.output: str
        self.tail: str

    def __init_subclass__(cls: Type["InsertReturnHelper"], **kwargs: Dict[str, Any]):
        super().__init_subclass__(**kwargs)
        cls._dialect_dict[cls._sql_dialect] = cls

    @classmethod
    def get(cls, sql_dialect: str) -> Type["InsertReturnHelper"]:
        ret_val = cls._dialect_dict.get(sql_dialect)
        if ret_val is None:
            raise KeyError(f"SQL dialect '{sql_dialect}' InsertReturnHelper not found")
        return ret_val


class PostgresInsertReturnHelper(InsertReturnHelper):  # type: ignore
    _sql_dialect = "postgres"

    def __init__(self, is_insert: bool, outputs: List[str]):
        super().__init__(is_insert, outputs)
        self.sequence = "default,"  # postgres uses default for sequences
        self.output = (
            f" OUTPUT ({', '.join(outputs)})"
            if len(outputs) > 0 and not is_insert
            else ""
        )
        self.tail = f" RETURNING {', '.join(outputs)}" if len(outputs) > 0 else ""


class MsSqlInsertReturnHelper(InsertReturnHelper):  # type: ignore
    _sql_dialect = "mssql"

    def __init__(self, is_insert: bool, outputs: List[str]):
        super().__init__(is_insert, outputs)
        self.sequence = "default,"
        self.output = (
            f" OUTPUT ({', '.join([f'Inserted.{o}' for o in outputs])})"
            if len(outputs) > 0
            else ""
        )
        self.tail = ""
