SHELL := /bin/bash

.PHONY: help

###############################################################################
# GLOBALS 																      #
###############################################################################

CURRENT_BRANCH = $(shell git rev-parse --abbrev-ref HEAD)
RESET := $(shell tput -Txterm sgr0)
TARGET_COLOR := $(BLUE)
# to see all colors, run
# bash -c 'for c in (0..255); do tput setaf $c; tput setaf $c | cat -v; echo =$c; done'
# the first 15 entries are the 8-bit colors

# define standard colors
BLACK        := $(shell tput -Txterm setaf 0)
RED          := $(shell tput -Txterm setaf 1)
GREEN        := $(shell tput -Txterm setaf 2)
YELLOW       := $(shell tput -Txterm setaf 3)
LIGHTPURPLE  := $(shell tput -Txterm setaf 4)
PURPLE       := $(shell tput -Txterm setaf 5)
BLUE         := $(shell tput -Txterm setaf 6)
WHITE        := $(shell tput -Txterm setaf 7)

BOLD             := $(shell tput bold)
NORMAL           := $(shell tput sgr0)

###############################################################################
# SELF DOCUMENTED MAKEFILE 	        									      #
###############################################################################

help:
	@echo ""
	@echo -e "$(BOLD)$(GREEN)MAKEFILE $(BASENAME)$(RESET)$(NORMAL)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(BOLD)$(TARGET_COLOR)%-20s$(RESET)$(NORMAL) $(BLUE)%s$(RESET)\n", $$1, $$2}'

banner:
	@echo -e "\n$(BOLD)$(PURPLE)$(message)$(RESET)$(NORMAL)"
###############################################################################
# COMMON TASKS 															      #
###############################################################################

commit: ## commit all changes
	git add .
	git commit
	git push origin $(CURRENT_BRANCH)

clean-cache: ## clean cache
	@find . -not -path "./venv/*" | grep -E "(__pycache__|\.pyc|\.pyo$$|\.pytest_cache|\.mypy_cache|\.coverage$$|\.xml|\.egg-info|dist)" | xargs rm -rf