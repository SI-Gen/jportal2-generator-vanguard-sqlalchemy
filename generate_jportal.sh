echo Running JPortal2 from ${PWD}
docker run --rm -v ${PWD}:/local bbdsoftware/jportal2 \
                      --inputdir=/local/tests/si \
                      --template-location=/local \
                      --flag SQLAlchemy.generateBuiltIns \
                      --template-generator \
                        SQLAlchemy:/local/generated_sources/generated \
                      --builtin-generator \
                        PythonCliCode:/local/generated_sources/pymod \
                      --builtin-generator \
                        CSNetCode:/local/generated_sources/csnet \
                      --builtin-generator \
                      PostgresDDL:/local/generated_sources/generated_sql