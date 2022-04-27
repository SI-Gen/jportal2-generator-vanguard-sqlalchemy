# jportal2-generator-vanguardg-sqlalchemy
This is a JPortal2 generator that generates SQLAlchemy-based database access for the Vanguard framework

Usage:
======

```shell
cd <template_directory>
curl -fsSL https://github.com/SI-Gen/jportal2-generatoror-vanguard-sqlalchemy/releases/tag/1.2/jportal2-generator-vanguardg-sqlalchemy-1.2.zip > sqlalchemy.zip && unzip sqlalchemy.zip && rm sqlalchemy.zip
java -jar jportal.jar \
        --inputdir=<input_directory> \
        --template-location=<template_directory> \
        --flag SQLAlchemy.generateBuiltIns \
        --template-generator \
          SQLAlchemy:<output_directory>

```
