.PHONY: help

###############################################################################
# GLOBALS 																      #
###############################################################################

CURRENT_BRANCH = $(shell git rev-parse --abbrev-ref HEAD)


help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

commit:
	git add .
	git commit
	git push origin $(CURRENT_BRANCH)