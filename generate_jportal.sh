echo Running JPortal2 from ${PWD}
docker pull ghcr.io/si-gen/jportal2:latest #To force a check for a newer "latest" on the server
#docker run --rm -v ${PWD}:/local bbdsoftware/jportal2:latest \
docker run --rm -v ${PWD}:/local ghcr.io/si-gen/jportal2:latest \
                      --inputdir=/local/tests/si \
                      --template-location=/local \
                      --flag SQLAlchemy.generateBuiltIns \
                      --template-generator \
                        SQLAlchemy:/local/generated_sources/generated \
                      --builtin-generator \
                      PostgresDDL:/local/generated_sources/generated_sql
