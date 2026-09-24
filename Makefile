# https://stackoverflow.com/a/14777895
ifeq '$(findstring ;,$(PATH))' ';'
    POSIXSHELL :=
else
    POSIXSHELL := 1
endif

.PHONY: generate-jportal test
.DEFAULT_GOAL := test

generate-jportal: # Generate SQLAlchemy sources from the SI files.
	bash generate_jportal.sh

test: # Run the tests in the tests folder.
	.venv/bin/python -m pytest tests

# https://dwmkerr.com/makefile-help-command/
.PHONY: help_internal
help_internal: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done && printf "\n"

ifeq ($(IN_DEV_CONTAINER),true)
.PHONY: help
help:
	@echo "\e[1m\033[1;31mJPortal2 SQLAlchemy Generator Help\e[0m\n"
	@echo "\e[4m\033[1;34mDevcontainer commands\e[0m"
	@echo "\033[1;32mattach_repo\033[00m [git repo url]: Attach a repo that is a upstream package of this repo"
	@echo "\033[1;32mdetach_repo\033[00m [git repo url]: Detach an attached repo\n"
	@echo "\e[4m\033[1;34mGeneral commands\e[0m"
	@$(MAKE) --no-print-directory help_internal
else ifneq ($(POSIXSHELL),)
.PHONY: help
help:
	@echo "\e[1m\033[1;31mJPortal2 SQLAlchemy Generator Help\e[0m\n"
	@$(MAKE) --no-print-directory help_internal
else
.DEFAULT:
	@powershell Write-Host "Make commands are only available on unix shells. If on Windows, please run in WSL terminal!" -ForegroundColor Yellow
endif
