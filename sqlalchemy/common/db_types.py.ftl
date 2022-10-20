from sqlalchemy import types


class NonNullableString(types.TypeDecorator):
    impl = types.String

    @classmethod
    def process_bind_param_cls(cls, value, dialect):
        if value == "" and dialect.name == "oracle":
            return " "
        else:
            return value

    @classmethod
    def process_result_value_cls(cls, value, dialect):
        if value == " " and dialect.name == "oracle":
            return ""
        else:
            return value

    def process_bind_param(self, value, dialect):
        return NonNullableString.process_bind_param_cls(value, dialect)

    def process_result_value(self, value, dialect):
        return NonNullableString.process_result_value_cls(value, dialect)

    def copy(self, **kw):
        return NonNullableString(self.impl.length)

    @property
    def python_type(self) -> type:
        return str


class Boolean(types.TypeDecorator):
    impl = types.Boolean

    @classmethod
    def process_bind_param_cls(cls, value, dialect):
        if dialect.name in ["oracle", "postgresql"]:
            if value is None:
                return None
            elif not value:
                return 0
            else:
                return 1
        else:
            return value

    @classmethod
    def process_result_value_cls(cls, value, dialect):
        if dialect.name in ["oracle", "postgresql"]:
            if value is None:
                return None
            elif not value:
                return False
            else:
                return True
        else:
            return value

    def process_bind_param(self, value, dialect):
        return Boolean.process_bind_param_cls(value, dialect)

    def process_result_value(self, value, dialect):
        return Boolean.process_result_value_cls(value, dialect)

    def copy(self, **kw):
        return Boolean()

    @property
    def python_type(self) -> type:
        return bool