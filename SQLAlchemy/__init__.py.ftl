<#-- @ftlvariable name="table" type="bbd.jportal2.Table" -->
########################################################################################################################
################## Generated Code. DO NOT CHANGE THIS CODE. Change it in the generator and regenerate ##################
########################################################################################################################
<#list database.getTables() as table>
from .db_${table.getName()} import DB_${table.getName()}
<#list table.getProcs() as proc>
<#if !proc.isBuiltIn() || database.flags?seq_contains("SQLAlchemy.generateBuiltIns")>
from .db_${table.getName()} import DB_${table.getName()}${proc.name}<#if proc.hasReturning>Returning</#if>
</#if>
</#list>
</#list>

ALL_TABLES = [
<#list database.getTables()?sort as table>
    DB_${table.getName()},
</#list>
]

ALL_PROCS = [
<#list database.getTables()?sort as table>
    <#list table.getProcs()?sort as proc>
<#if !proc.isBuiltIn() || database.flags?seq_contains("SQLAlchemy.generateBuiltIns")>
    DB_${table.getName()}${proc.name}<#if proc.hasReturning>Returning</#if>,
</#if>
    </#list>
<#sep>${"\n"}</#list>
]


__all__ = [
<#list database.getTables()?sort as table>
    "DB_${table.getName()}",
</#list>

<#list database.getTables()?sort as table>
    <#list table.getProcs()?sort as proc>
        <#if !proc.isBuiltIn() || database.flags?seq_contains("SQLAlchemy.generateBuiltIns")>
    "DB_${table.getName()}${proc.name}<#if proc.hasReturning>Returning</#if>",
        </#if>
    </#list>
<#sep>${"\n"}</#list>
]
