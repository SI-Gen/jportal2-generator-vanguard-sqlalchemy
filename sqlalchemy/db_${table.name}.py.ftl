<#-- @ftlvariable name="table" type="bbd.jportal2.Table" -->
########################################################################################################################
################## Generated Code. DO NOT CHANGE THIS CODE. Change it in the generator and regenerate ##################
########################################################################################################################

<#function getSQLAlchemyColumnType field table>
<#--    <#if field.enums?size gt 0><#return "EnumAsSmallInteger()"></#if>-->
    <#if field.enums?size gt 0>
        <#if field.type?c == '3'><#return "db_types.IntEnum(${field.name}Enum)">
        <#elseif field.type?c == '10'><#return "db_types.IntEnum(${field.name}Enum)">
        <#elseif field.type?c == '11'><#return "db_types.IntEnum(${field.name}Enum)">
        <#elseif field.type?c == '14'><#return "db_types.IntEnum(${field.name}Enum)">
        <#elseif field.type?c == '15'><#return "db_types.IntEnum(${field.name}Enum)">
        </#if>
    </#if>
    <#if field.type?c == '1'><#return "sa.LargeBinary()">
    <#elseif field.type?c == '2'><#return "db_types.Boolean()">
    <#elseif field.type?c == '3'><#return "sa.SmallInteger()">
    <#elseif field.type?c == '4' && field.isNull()><#return "sa.String(length=#{field.length; M0})">
    <#elseif field.type?c == '4'><#return "db_types.NonNullableString(length=#{field.length; M0})">
    <#elseif field.type?c == '5'><#return "sa.DateTime()">
    <#elseif field.type?c == '6'><#return "sa.DateTime()">
    <#elseif field.type?c == '7'><#return "sa.Numeric(precision=${field.precision}, scale=${field.scale})">
    <#elseif field.type?c == '9'><#return "sa.Float(precision=${field.precision})">
    <#elseif field.type?c == '10'><#return "sa.Integer()">
    <#elseif field.type?c == '11'><#return "sa.Integer()">
    <#elseif field.type?c == '12'><#return "sa.BigInteger()">
    <#elseif field.type?c == '13'><#return "sa.Numeric(precision=${field.precision}, scale=${field.scale})">
    <#elseif field.type?c == '14'><#return "sa.Integer()">
    <#elseif field.type?c == '15'><#return "sa.SmallInteger()">
    <#elseif field.type?c == '17'><#return "sa.DateTime()">
    <#elseif field.type?c == '18'><#return "sa.DateTime()">
    <#elseif field.type == STATICS.Field.TLOB><#return "sa.Text()">
    <#elseif field.type?c == '20'><#return "sa.DateTime()">
    <#elseif field.type?c == '21'><#return "sa.String(length=#{field.length; M0})">
    <#elseif field.type?c == '23'><#return "sa.String(length=#{field.length; M0})">
    <#elseif field.type?c == '24'><#return "sa.BigInteger()">
    <#elseif field.type?c == '25'><#return "sa.BigInteger()">
    <#elseif field.type?c == '26'><#return "sa.DateTime()">
    <#elseif field.type?c == '27'><#return "sa.Unicode(length=#{field.length; M0})">
    <#elseif field.type?c == '28'><#return "sa.Unicode(#{field.length; M0})">
    <#elseif field.type?c == '29'><#return "sa.Unicode(#{field.length; M0})">
    <#elseif field.type?c == '30'><#return "sa.String(length=#{field.length; M0})">
    <#elseif field.type == STATICS.Field.JSON><#return "sa.JSON">
    <#elseif field.type == STATICS.Field.BIGJSON><#return "sa.JSON">
    <#else><#return "String(100)">
    </#if>>
</#function>
<#function getSQLAlchemyBaseType field procname>
<#--    <#if field.enums?size gt 0><#return "EnumAsSmallInteger()"></#if>&ndash;&gt;-->
    <#if field.type?c == '1'><#return "sa.types.LargeBinary">
    <#elseif field.type?c == '2'><#return "db_types.Boolean">
    <#elseif field.type?c == '3'><#return "sa.types.SmallInteger">
    <#elseif field.type?c == '4' && field.isNull()><#return "sa.types.String">
    <#elseif field.type?c == '4'><#return "db_types.NonNullableString">
    <#elseif field.type?c == '5'><#return "sa.types.DateTime">
    <#elseif field.type?c == '6'><#return "sa.types.DateTime">
    <#elseif field.type?c == '7'><#return "sa.types.Numeric">
    <#elseif field.type?c == '9'><#return "sa.types.Float">
    <#elseif field.type?c == '10'><#return "sa.types.Integer">
    <#elseif field.type?c == '11'><#return "sa.types.Integer">
    <#elseif field.type?c == '12'><#return "sa.types.BigInteger">
    <#elseif field.type?c == '13'><#return "sa.types.Numeric">
    <#elseif field.type?c == '14'><#return "sa.types.Integer">
    <#elseif field.type?c == '15'><#return "sa.types.SmallInteger">
    <#elseif field.type?c == '17'><#return "sa.types.DateTime">
    <#elseif field.type?c == '18'><#return "sa.types.DateTime">
    <#elseif field.type?c == '19'><#return "sa.types.Text">
    <#elseif field.type?c == '20'><#return "sa.types.DateTime">
    <#elseif field.type?c == '21'><#return "sa.types.String">
    <#elseif field.type?c == '23'><#return "sa.types.String">
    <#elseif field.type?c == '24'><#return "sa.types.BigInteger">
    <#elseif field.type?c == '25'><#return "sa.types.BigInteger">
    <#elseif field.type?c == '26'><#return "sa.types.DateTime">
    <#elseif field.type?c == '27'><#return "sa.types.Unicode">
    <#elseif field.type?c == '28'><#return "sa.types.Unicode">
    <#elseif field.type?c == '29'><#return "sa.types.Unicode">
    <#elseif field.type?c == '30'><#return "sa.types.String">
    <#elseif field.type == STATICS.Field.JSON><#return "sa.JSON">
    <#elseif field.type == STATICS.Field.BIGJSON><#return "sa.JSON">
    <#else><#return "String">
    </#if>>
</#function>
<#function getColumnAttributes field table>
<#-- @ftlvariable name="field" type="bbd.jportal2.Field" -->
<#-- @ftlvariable name="table" type="bbd.jportal2.Table" -->
    <#local retVal = "">
    <#if field.type?c == '14' || field.type?c == '24'>
        <#local retVal = retVal + ', sa.Sequence("' + table.getName()?upper_case + 'SEQ", metadata=Base.metadata, schema=${table.getName()?upper_case}_SCHEMA)'>
    </#if>
    <#if table.getLinkForField(field)??>
        <#assign link = table.getLinkForField(field)>
        <#if link.getName() != table.name>
        <#local retVal = retVal + ", sa.ForeignKey(DB_" + link.getName() + "." + link.getFirstLinkField() + ")">
        </#if>
    </#if>
    <#if field.isPrimaryKey()>
        <#if field.type?c == '10' || field.type?c == '14' || field.type?c == '24' || field.type?c == '25'>
            <#-- All the sequence types.-->
            <#local retVal = retVal + ", primary_key=True">
        <#else>
            <#local retVal = retVal + ", primary_key=True, autoincrement=False">
        </#if>
    </#if>
    <#if field.isNull()><#local retVal = retVal + ", nullable=True"></#if>
    <#if field.getDefaultValue() != ""><#local retVal = retVal + ", default='" + field.getDefaultValue() +"'"></#if>
    <#if field.type?c == '18'>
        <#local retVal = retVal + ", default=datetime.now, onupdate=datetime.now">
    </#if>
    <#if field.type?c == '10' || field.type?c == '25'>
        <#local retVal = retVal + ", autoincrement=True">
    <#elseif field.type?c == '14' || field.type?c == '24'>
        <#local retVal = retVal + ", autoincrement=False">
    </#if>
    <#return retVal>
</#function>
<#function getPythonType apply_to_pk field >
<#-- @ftlvariable name="field" type="bbd.jportal2.Field" -->
    <#if field.enums?size gt 0><#return "${field.name}Enum"></#if>
    <#assign prefix = ''>
    <#assign suffix = ''>

    <#if field.isNull() || (apply_to_pk && field.isPrimaryKey())>
        <#assign prefix = 'Optional['>
        <#assign suffix = ']'>
    </#if>

    <#if field.type?c == '1'><#return prefix + "Any" + suffix>
    <#elseif field.type?c == '2'><#return prefix + "bool" + suffix>
    <#elseif field.type?c == '3'><#return prefix + "int" + suffix>
    <#elseif field.type?c == '4'><#return prefix + "str" + suffix>
    <#elseif field.type?c == '5'><#return prefix + "datetime" + suffix>
    <#elseif field.type?c == '6'><#return prefix + "datetime" + suffix>
    <#elseif field.type?c == '7'><#return prefix + "float" + suffix>
    <#elseif field.type?c == '9'><#return prefix + "float" + suffix>
    <#elseif field.type?c == '10'><#return prefix + "int" + suffix>
    <#elseif field.type?c == '11'><#return prefix + "int" + suffix>
    <#elseif field.type?c == '12'><#return prefix + "int" + suffix>
    <#elseif field.type?c == '13'><#return prefix + "int" + suffix>
    <#elseif field.type?c == '14'><#return prefix + "int" + suffix>
    <#elseif field.type?c == '15'><#return prefix + "int" + suffix>
    <#elseif field.type?c == '17'><#return prefix + "datetime" + suffix>
    <#elseif field.type?c == '18'><#return prefix + "datetime" + suffix>
    <#elseif field.type == STATICS.Field.TLOB><#return prefix + "str" + suffix>
    <#elseif field.type?c == '20'><#return prefix + "datetime" + suffix>
    <#elseif field.type?c == '21'><#return prefix + "str" + suffix>
    <#elseif field.type?c == '23'><#return prefix + "str" + suffix>
    <#elseif field.type?c == '24'><#return prefix + "int" + suffix>
    <#elseif field.type?c == '25'><#return prefix + "int" + suffix>
    <#elseif field.type?c == '26'><#return prefix + "datetime" + suffix>
    <#elseif field.type?c == '27'><#return prefix + "str" + suffix>
    <#elseif field.type?c == '28'><#return prefix + "str" + suffix>
    <#elseif field.type?c == '29'><#return prefix + "str" + suffix>
    <#elseif field.type?c == '30'><#return prefix + "str" + suffix>
    <#elseif field.type == STATICS.Field.JSON><#return prefix + "str" + suffix>
    <#elseif field.type == STATICS.Field.BIGJSON><#return prefix + "str" + suffix>

    <#else><#return prefix + "str" + suffix>
    </#if>>
</#function>

<#function getTableReturnType proc tableName>
    <#if proc.outputs?size <= 0><#return "None">
    <#elseif proc.isSingle()><#return "Optional['${tableName}']">
    <#else><#return "List['${tableName}']">
    </#if>>
</#function>

<#function isMultiLinkFk link table>
<#-- @ftlvariable name="table" type="bbd.jportal2.Table" -->
<#-- @ftlvariable name="link" type="bbd.jportal2.Link" -->
    <#local tableRefCount = 0>
    <#local externalTableName = link.getName()>

    <#list table.getFields() as field>
        <#if table.getLinkForField(field)??>
            <#local linkL = table.getLinkForField(field) >
            <#if linkL.getName() == externalTableName>
                <#return true>
            </#if>
        </#if>
    </#list>
    <#return false>
</#function>

<#function getFkAdditionalParams link table>
<#-- @ftlvariable name="table" type="bbd.jportal2.Table" -->
<#-- @ftlvariable name="link" type="bbd.jportal2.Link" -->
    <#if isMultiLinkFk(link, table)>
        <#local externalTableName = link.getName()>
        <#local field = table.getFieldForLink(link) >
        <#return ", foreign_keys=[${field.name}]">
<#--        <#list table.getFields() as field>-->
<#--            <#if table.getLinkForField(field)??>-->
<#--                <#local linkL = table.getLinkForField(field) >-->
<#--                <#if linkL.getName() == externalTableName>-->
<#--                    <#return ", foreign_keys=[${field.name}]">-->
<#--                </#if>-->
<#--            </#if>-->
<#--        </#list>-->
    </#if>
    <#return "">
</#function>

<#function getFkName link table>
<#-- @ftlvariable name="table" type="bbd.jportal2.Table" -->
<#-- @ftlvariable name="link" type="bbd.jportal2.Link" -->
    <#local retVal = "${link.getName()}">
    <#if isMultiLinkFk(link, table)>
        <#local retVal = retVal + "_" + link.fields?first>
    </#if>

    <#return retVal>
</#function>
<#function GenerateProcName table proc>
    <#local retVal ="DB_"+table.name+proc.name>
    <#if proc.hasReturning><#local retVal += "Returning"></#if>
    <#if proc.isData()><#local retVal += "StaticData"></#if>
    <#return retVal >
</#function>
<#macro generateEnum parent field>
    # Enum for ${field.name} field
    class ${field.name}Enum(enum.IntEnum):
    <#list field.enums as enum>
        ${enum.name} = ${enum.value}
    </#list>

        @classmethod
        def process_result_value_cls(cls, value, dialect):
            return ${parent}.${field.name}Enum(value)

        @classmethod
        def process_bind_param_cls(cls, value, dialect):
            return value.value
<#---->
<#--        @classmethod-->
<#--        def process_bind_param_cls(cls, value, dialect):-->
<#--            return value.value-->
<#---->
<#--        def process_bind_param(self, value, dialect):-->
<#--            return ${field.name}Enum.process_bind_param_cls(value, dialect)-->

<#--        def process_result_value(self, value, dialect):-->
<#--            return ${field.name}Enum.process_result_value_cls(value, dialect)-->

<#--        def copy(self, **kw):-->
<#--            return ${field.name}Enum(**kw)-->


</#macro>
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Any, Optional
<#list table.fields as field><#if field.enums?size gt 0>import enum<#break></#if></#list>
import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import TextAsFrom

from .common.db_common import DBMixin, Base, DBColumn
from .common import db_types
from .common.processing import process_result_recs, process_result_rec, process_bind_params

<#list table.getLinks() as link>
<#if link.getName() != table.name>
from .db_${link.getName()} import DB_${link.getName()}
</#if>
</#list>

<#function getConstructorList table>
<#-- @ftlvariable name="table" type="bbd.jportal2.Table" -->
    <#local fieldNames = table.fields?filter(field -> field.name?lower_case != 'tmstamp' && field.type != 10 && field.type != 14 && field.type != 24 && field.type != 25)?map(field -> field.name + ': ' + getPythonType(true, field))>
    <#return ", " + fieldNames?join(", ")>
</#function>

<#function getConstructorSetList table>
<#-- @ftlvariable name="table" type="bbd.jportal2.Table" -->
    <#local fieldSetNames = table.fields?filter(field -> field.name?lower_case != 'tmstamp' && field.type != 10 && field.type != 14 && field.type != 24 && field.type != 25)?map(field -> field.name + "=" + field.name)>
    <#return fieldSetNames?join(",\n            ")>
</#function>

<#if (database.flags?seq_contains("SQLAlchemy.generateSQLAlchemyBase"))>
${table.getName()?upper_case}_SCHEMA = "${table.getDatabase().getSchema()?lower_case}"
class DB_${table.name}(Base, DBMixin):
    <#list table.fields as field><#if field.enums?size gt 0>
    <@generateEnum "DB_${table.name}" field/>
    </#if>
    </#list>
    <#list table.fields as field>
<#--        <#if field.name?lower_case != 'tmstamp'>-->
    ${field.name}: <#compress>${getPythonType(false, field)}</#compress> = DBColumn("${field.name?lower_case}", <#compress>${getSQLAlchemyColumnType(field, table)}${getColumnAttributes(field, table)})</#compress>
<#--        </#if>-->
    </#list>
<#--backref="F_${getFkName(link table)}"-->
    <#if table.links?size gt 0>

    # Foreign Key Links
        <#list table.getLinks() as link>
        <#if link.getName() != table.name>
    F_${getFkName(link table)} = sa.orm.relationship(DB_${link.getName()}${getFkAdditionalParams(link, table)})
        </#if>
        </#list>
    </#if>

    __schema__ = ${table.getName()?upper_case}_SCHEMA

    def __init__(self${getConstructorList(table)}):
        super(DB_${table.name}, self).__init__(
            ${getConstructorSetList(table)})
</#if>
<#list table.procs as proc>
<#if (!proc.isBuiltIn() || (proc.isBuiltIn() && !database.flags?seq_contains("SQLAlchemy.skipBuiltIns")))>

@dataclass
class ${GenerateProcName(table, proc)}:
    <#list proc.inputs as field><#if field.enums?size gt 0>
        <@generateEnum GenerateProcName(table, proc) field />
    </#if>
    </#list>
    <#list proc.outputs as field><#if field.enums?size gt 0>
    <@generateEnum GenerateProcName(table, proc) field />
    </#if>
    </#list>
    <#if proc.outputs?size gt 0>#Outputs</#if>
    <#list proc.outputs as field>
    ${field.name}: <#compress>${getPythonType(false, field)}</#compress>
    </#list>

    @classmethod
    def get_statement(cls
                     <#list proc.inputs as field>, ${field.name}: ${getPythonType(false, field)}
                     </#list><#list proc.dynamics as dynamic>, ${dynamic}: str</#list>) -> TextAsFrom:
        class _ret:
            sequence = "default," #postgres uses default for sequences
            output = <#if proc.isInsert()==false && proc.outputs?size gt 0>" OUTPUT (<#list proc.outputs as x>${x.name}<#sep>,</#list>)"<#else>""</#if>
            tail = <#if proc.outputs?size gt 0>" RETURNING <#list proc.outputs as x>${x.name}<#sep> </#list>"<#else>""</#if>
            #session.bind.dialect.name

        statement = sa.text(<#list proc.lines as pl>
                        f"${pl.getDecoratedLine()}"</#list>)

        text_statement = statement.columns(<#list proc.outputs as field>${field.name}=${getSQLAlchemyBaseType(field, GenerateProcName(table, proc))},
                                      </#list>)
        <#--  statement = statement.columns(<#list proc.outputs as field>column('${field.name}'), \
                                    </#list>)  -->
        <#if proc.inputs?size gt 0>
        text_statement = text_statement.bindparams(<#list proc.inputs as field>${field.name}=${field.name},
                                         </#list>)
        </#if>
        return text_statement

    @classmethod
    def execute(cls, session: Session<#list proc.inputs as field>, ${field.name}: ${getPythonType(false, field)}
                     </#list><#list proc.dynamics as dynamic>, ${dynamic}: str</#list>) -> ${getTableReturnType(proc, GenerateProcName(table, proc))}:
        <#if proc.inputs?size gt 0>
        params = process_bind_params(session, [<#list proc.inputs as field>${getSQLAlchemyBaseType(field,GenerateProcName(table, proc))},
                                        </#list><#list proc.dynamics as dynamic>db_types.NonNullableString,</#list>], [<#list proc.inputs as field>${field.name}<#if field.enums?size gt 0>.value if isinstance(${field.name}, enum.IntEnum) else ${field.name}</#if>,
                                        </#list><#list proc.dynamics as dynamic>${dynamic},</#list>])
        </#if>
        res = session.execute(cls.get_statement(<#if proc.inputs?size gt 0>*params</#if>))
        <#if proc.isSingle()>
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(${GenerateProcName(table, proc)}, session, [<#list proc.outputs as field><#if field.enums?size gt 0>${GenerateProcName(table, proc)}.${field.name}Enum<#else>${getSQLAlchemyBaseType(field, proc)}</#if>,
                                        </#list>], rec)

        return None
        <#elseif proc.outputs?size gt 0>
        recs = res.fetchall()
        return process_result_recs(${GenerateProcName(table, proc)}, session, [<#list proc.outputs as field><#if field.enums?size gt 0>${GenerateProcName(table, proc)}.${field.name}Enum<#else>${getSQLAlchemyBaseType(field, proc)}</#if>,
                                        </#list>], recs)
        <#else>
        res.close()
        </#if>
    </#if>
</#list>
