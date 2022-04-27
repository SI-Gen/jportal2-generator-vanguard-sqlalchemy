# jportal2-generator-vanguardg-sqlalchemy
This is a JPortal2 generator that generates SQLAlchemy-based database access for the Vanguard framework

Usage:
======

```shell

#Change directory to template directory
cd <template_directory>

#Download version $VERSION template
SQLALCHEMY_TEMPLATE_VERSION=1.2
curl -fsSL https://github.com/SI-Gen/jportal2-generatoror-vanguard-sqlalchemy/releases/tag/$SQLALCHEMY_TEMPLATE_VERSION/jportal2-generator-vanguardg-sqlalchemy-$SQLALCHEMY_TEMPLATE_VERSION.zip > sqlalchemy.zip && unzip sqlalchemy.zip && rm sqlalchemy.zip

#Run JPortal2
java -jar jportal.jar \
        --inputdir=<input_directory> \
        --template-location=<template_directory> \
        --flag SQLAlchemy.generateBuiltIns \
        --template-generator \
          SQLAlchemy:<output_directory>

```
