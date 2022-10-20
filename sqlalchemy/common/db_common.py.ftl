from functools import partial
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base, declared_attr

Base = declarative_base()

DBColumn = partial(sa.Column, nullable=False)


class DBMixin:
    @declared_attr
    def __tablename__(cls):
        name = cls.__name__.lower()
        if name.startswith("db_"):
            name = name[3:]
        return name

    @declared_attr
    def __table_args__(cls):
        return {"schema": cls.__schema__}

    __indexes__: list = []  # Not used by SQLAlchemy!
    __constraints__: list = []  # Not used by SQLAlchemy!

    __mapper_args__ = {"always_refresh": True}

    @classmethod
    def map_from_rec(cls, existing_rec):
        kwargs = {}
        primary_keys = []
        for col_name, col in cls._sa_class_manager.local_attrs.items():
            if col.prop.columns[0].primary_key:
                primary_keys.append(col_name)
            elif hasattr(existing_rec, col_name) and col.prop.columns[0].onupdate is None:
                kwargs[col_name] = getattr(existing_rec, col_name)
        tmp = cls(**kwargs)
        for pk in primary_keys:
            if hasattr(existing_rec, pk):
                setattr(tmp, pk, getattr(existing_rec, pk))
        return tmp

    @classmethod
    def update_from_existing(cls, existing_rec):
        where_clause = []
        kwargs = {}
        for col_name, col in cls._sa_class_manager.local_attrs.items():
            if col.prop.columns[0].primary_key:
                where_clause.append(col == getattr(existing_rec, col_name))  # the == calls __eq__ on col.
            elif hasattr(existing_rec, col_name) and col.prop.columns[0].onupdate is None:
                new_col_name = getattr(cls, col_name).prop.columns[0].name
                kwargs[new_col_name] = getattr(existing_rec, col_name)

        return sa.update(cls).where(*where_clause).values(**kwargs)

    # Default Fields:
    # @declared_attr
    # def UsrID(cls):
    #     return DBColumn(sa.String(64))
    # @declared_attr
    # def TmStamp(cls):
    #     return DBColumn(sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.current_timestamp())


#
# def update_timestamp(mapper, connection, target):
#     # type: (None, None, DBMixin) -> None
#     if not sa.orm.Session.object_session(target).is_modified(
#         target, include_collections=False
#     ):
#         return
#     target.TmStamp = sa.func.current_timestamp()