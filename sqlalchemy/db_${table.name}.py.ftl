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
        <#local retVal = retVal + ",\n        sa.Sequence(\"" + table.getName()?upper_case + "SEQ\", metadata=Base.metadata, schema=${table.getName()?upper_case}_SCHEMA)">
    </#if>
    <#if table.getLinkForField(field)??>
        <#assign link = table.getLinkForField(field)>
        <#if link.getName() != table.name && link.getFirstLinkField()??>
        <#local retVal = retVal + ",\n        sa.ForeignKey(DB_" + link.getName() + "." + link.getFirstLinkField() + ")">
        </#if>
    </#if>
    <#if field.isPrimaryKey()>
        <#local retVal = retVal + ",\n        primary_key=True">
        <#if !(field.type?c == '10' || field.type?c == '14' || field.type?c == '24' || field.type?c == '25')>
            <#local retVal = retVal + ",\n        autoincrement=False">
        </#if>
    </#if>
    <#if field.isNull()><#local retVal = retVal + ",\n        nullable=True"></#if>
    <#if field.getDefaultValue() != ""><#local retVal = retVal + ",\n        default='" + field.getDefaultValue() +"'"></#if>
    <#if field.type?c == '18'>
        <#local retVal = retVal + ",\n        default=datetime.now,\n        onupdate=datetime.now">
    </#if>
    <#if field.type?c == '10' || field.type?c == '25'>
        <#local retVal = retVal + ",\n        autoincrement=True">
    <#elseif field.type?c == '14' || field.type?c == '24'>
        <#local retVal = retVal + ",\n        autoincrement=False">
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
    <#elseif field.type?c == '7'><#return prefix + "int" + suffix>
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
<#function isSelectOne proc>
    <#return proc.name == "SelectOne">
</#function>
<#function fieldNameInList fields name>
    <#list fields as field>
        <#if field.name == name>
            <#return true>
        </#if>
    </#list>
    <#return false>
</#function>
<#function selectOneInputsNotInOutputs proc>
    <#local result = []>
    <#list proc.inputs as field>
        <#if !fieldNameInList(proc.outputs, field.name)>
            <#local result = result + [field]>
        </#if>
    </#list>
    <#return result>
</#function>
<#macro generateEnum parent field>
    # Enum for ${field.name} field
    <#-- 21 = ansichar, 28 = wansichar -->
    class ${field.name}Enum(<#if field.type?c == '28' || field.type?c == '21'>enum.Enum<#else>enum.IntEnum</#if>):
    <#list field.enums as enum>
        ${enum.name} = <#if field.type?c == '28' || field.type?c == '21'>'${enum.getChar()}'<#else>${enum.value}</#if>
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
<#function isDatetimeField field>
    <#local t = field.type?c>
    <#return t == '5' || t == '6' || t == '17' || t == '18' || t == '20' || t == '26'>
</#function>
<#function isIntEnumField field>
    <#if field.enums?size == 0><#return false></#if>
    <#local t = field.type?c>
    <#return t == '3' || t == '10' || t == '11' || t == '14' || t == '15'>
</#function>
<#function fieldsUseDatetime fields>
    <#list fields as field>
        <#if isDatetimeField(field)><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function fieldsUseAny fields>
    <#list fields as field>
        <#if field.type?c == '1'><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function fieldsUseOptional fields>
    <#list fields as field>
        <#if field.isNull()><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function fieldsUseEnum fields>
    <#list fields as field>
        <#if field.enums?size gt 0><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function fieldUsesDbTypes field>
    <#if field.type?c == '2'><#return true></#if>
    <#if field.type?c == '4' && !field.isNull()><#return true></#if>
    <#return false>
</#function>
<#function fieldsUseDbTypes fields>
    <#list fields as field>
        <#if fieldUsesDbTypes(field)><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function tableUsesDatetime table>
    <#if fieldsUseDatetime(table.fields)><#return true></#if>
    <#list table.procs as proc>
        <#if fieldsUseDatetime(proc.inputs) || fieldsUseDatetime(proc.outputs)><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function tableUsesAny table>
    <#if fieldsUseAny(table.fields)><#return true></#if>
    <#list table.procs as proc>
        <#if fieldsUseAny(proc.inputs) || fieldsUseAny(proc.outputs)><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function tableUsesList table>
    <#list table.procs as proc>
        <#if proc.outputs?size gt 0 && !proc.isSingle()><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function tableUsesOptional table>
    <#if fieldsUseOptional(table.fields)><#return true></#if>
    <#list table.procs as proc>
        <#if proc.isSingle() && proc.outputs?size gt 0><#return true></#if>
        <#if fieldsUseOptional(proc.inputs) || fieldsUseOptional(proc.outputs)><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function tableUsesEnum table>
    <#if fieldsUseEnum(table.fields)><#return true></#if>
    <#list table.procs as proc>
        <#if fieldsUseEnum(proc.inputs) || fieldsUseEnum(proc.outputs)><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function tableUsesDbTypes table>
    <#list table.fields as field>
        <#if fieldUsesDbTypes(field) || isIntEnumField(field)><#return true></#if>
    </#list>
    <#list table.procs as proc>
        <#if proc.dynamics?size gt 0><#return true></#if>
        <#if fieldsUseDbTypes(proc.inputs) || fieldsUseDbTypes(proc.outputs)><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function tableUsesBindParams table>
    <#list table.procs as proc>
        <#if proc.inputs?size gt 0 || proc.dynamics?size gt 0><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function tableUsesResultRec table>
    <#list table.procs as proc>
        <#if proc.isSingle()><#return true></#if>
    </#list>
    <#return false>
</#function>
<#function tableUsesResultRecs table>
    <#list table.procs as proc>
        <#if !proc.isSingle() && proc.outputs?size gt 0><#return true></#if>
    </#list>
    <#return false>
</#function>
<#-- Keep generated SQL literals under the line length. f-strings are only used when the chunk interpolates. -->
<#function pySqlChunks text>
    <#local maxLen = 96>
    <#local chunks = []>
    <#local rest = text>
    <#list 0..500 as _>
        <#if rest?length lte maxLen>
            <#if rest?length gt 0>
                <#local chunks = chunks + [rest]>
            </#if>
            <#break>
        </#if>
        <#local cut = maxLen>
        <#local brace = 0>
        <#local lastSpace = -1>
        <#list 0..<maxLen as i>
            <#local ch = rest?substring(i, i + 1)>
            <#if ch == "{">
                <#local brace = brace + 1>
            <#elseif ch == "}" && brace gt 0>
                <#local brace = brace - 1>
            </#if>
            <#if ch == " " && brace == 0>
                <#local lastSpace = i>
            </#if>
        </#list>
        <#if lastSpace gt 0>
            <#local cut = lastSpace>
        <#elseif brace gt 0>
            <#list maxLen..<rest?length as i>
                <#local ch = rest?substring(i, i + 1)>
                <#if ch == "{">
                    <#local brace = brace + 1>
                <#elseif ch == "}">
                    <#local brace = brace - 1>
                    <#if brace == 0>
                        <#local cut = i + 1>
                        <#break>
                    </#if>
                </#if>
            </#list>
        </#if>
        <#local chunks = chunks + [rest?substring(0, cut)]>
        <#local rest = rest?substring(cut)>
    </#list>
    <#return chunks>
</#function>
<#assign typingNames = []>
<#if tableUsesAny(table)><#assign typingNames = typingNames + ["Any"]></#if>
<#if tableUsesList(table)><#assign typingNames = typingNames + ["List"]></#if>
<#if tableUsesOptional(table)><#assign typingNames = typingNames + ["Optional"]></#if>
<#assign processingNames = []>
<#if tableUsesBindParams(table)><#assign processingNames = processingNames + ["process_bind_params"]></#if>
<#if tableUsesResultRec(table)><#assign processingNames = processingNames + ["process_result_rec"]></#if>
<#if tableUsesResultRecs(table)><#assign processingNames = processingNames + ["process_result_recs"]></#if>
from dataclasses import dataclass
<#if tableUsesDatetime(table)>
from datetime import datetime
</#if>
<#if tableUsesEnum(table)>
import enum
</#if>
<#if typingNames?size gt 0>
from typing import ${typingNames?join(", ")}
</#if>
import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import TextAsFrom

from .common.db_common import DBMixin, Base, DBColumn
<#if tableUsesDbTypes(table)>
from .common import db_types
</#if>
<#if processingNames?size gt 0>
from .common.processing import ${processingNames?join(", ")}
</#if>

<#list table.getLinks() as link>
<#if link.getName() != table.name>
from .db_${link.getName()} import DB_${link.getName()}
</#if>
</#list>

<#function getConstructorList table>
<#-- @ftlvariable name="table" type="bbd.jportal2.Table" -->
    <#local fieldNames = table.fields?filter(field -> field.name?lower_case != 'tmstamp' && field.type != 10 && field.type != 14 && field.type != 24 && field.type != 25)?map(field -> field.name + ': ' + getPythonType(false, field))>
    <#if fieldNames?size == 0>
        <#return "">
    </#if>
    <#return ",\n        " + fieldNames?join(",\n        ")>
</#function>

<#function getConstructorAssignList table>
<#-- @ftlvariable name="table" type="bbd.jportal2.Table" -->
    <#local assignments = table.fields?filter(field -> field.name?lower_case != 'tmstamp' && field.type != 10 && field.type != 14 && field.type != 24 && field.type != 25)?map(field -> "self." + field.name + " = " + field.name)>
    <#if assignments?size == 0>
        <#return "pass">
    </#if>
    <#return assignments?join("\n        ")>
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
    ${field.name}: ${getPythonType(false, field)} = DBColumn("${field.name?lower_case}", ${getSQLAlchemyColumnType(field, table)}${getColumnAttributes(field, table)})
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
        ${getConstructorAssignList(table)}
</#if>
<#list table.procs as proc>
<#if (!proc.isBuiltIn() || (proc.isBuiltIn() && !database.flags?seq_contains("SQLAlchemy.skipBuiltIns")))>

@dataclass
class ${GenerateProcName(table, proc)}:
    <#assign emittedEnumNames = []>
    <#list proc.inputs as field><#if field.enums?size gt 0 && !emittedEnumNames?seq_contains(field.name)>
        <@generateEnum GenerateProcName(table, proc) field />
        <#assign emittedEnumNames = emittedEnumNames + [field.name]>
    </#if>
    </#list>
    <#list proc.outputs as field><#if field.enums?size gt 0 && !emittedEnumNames?seq_contains(field.name)>
    <@generateEnum GenerateProcName(table, proc) field />
        <#assign emittedEnumNames = emittedEnumNames + [field.name]>
    </#if>
    </#list>
<#if isSelectOne(proc) && selectOneInputsNotInOutputs(proc)?size gt 0>
    #Inputs
    <#list selectOneInputsNotInOutputs(proc) as field>
    ${field.name}: <#compress>${getPythonType(false, field)}</#compress>
    </#list>

</#if>
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

        statement = sa.text(<#list proc.lines as pl><#list pySqlChunks(pl.getDecoratedLine()) as chunk>
                        <#if chunk?contains("{")>f"${chunk}"<#else>"${chunk}"</#if></#list></#list>)

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
        <#if proc.inputs?size gt 0 || proc.dynamics?size gt 0>
        params = process_bind_params(
            session,
            [
                <#list proc.inputs as field>
                ${getSQLAlchemyBaseType(field,GenerateProcName(table, proc))},
                </#list>
                <#list proc.dynamics as dynamic>
                db_types.NonNullableString,
                </#list>
            ],
            [
                <#list proc.inputs as field>
                <#if field.enums?size gt 0>
                ${field.name}.value if isinstance(${field.name}, <#if field.type?c == '28' || field.type?c == '21'>enum.Enum<#else>enum.IntEnum</#if>) else ${field.name},
                <#else>
                ${field.name},
                </#if>
                </#list>
                <#list proc.dynamics as dynamic>
                ${dynamic},
                </#list>
            ],
        )
        </#if>
        res = session.execute(cls.get_statement(<#if proc.inputs?size gt 0 || proc.dynamics?size gt 0>*params</#if>))
        <#if proc.isSingle()>
        rec = res.fetchone()
        if rec:
            res.close()
            return process_result_rec(
                ${GenerateProcName(table, proc)},
                session,
                [
                    <#list proc.outputs as field>
                    <#if field.enums?size gt 0>
                    ${GenerateProcName(table, proc)}.${field.name}Enum,
                    <#else>
                    ${getSQLAlchemyBaseType(field, proc)},
                    </#if>
                    </#list>
                ],
                rec,
                <#if isSelectOne(proc)>
                <#list selectOneInputsNotInOutputs(proc) as field>
                ${field.name}=${field.name},
                </#list>
                </#if>
            )

        return None
        <#elseif proc.outputs?size gt 0>
        recs = res.fetchall()
        return process_result_recs(
            ${GenerateProcName(table, proc)},
            session,
            [
                <#list proc.outputs as field>
                <#if field.enums?size gt 0>
                ${GenerateProcName(table, proc)}.${field.name}Enum,
                <#else>
                ${getSQLAlchemyBaseType(field, proc)},
                </#if>
                </#list>
            ],
            recs,
        )
        <#else>
        res.close()
        </#if>
    </#if>
</#list>
