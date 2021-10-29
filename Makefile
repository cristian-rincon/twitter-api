.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

commit:
	@git add $(MAKEFILE_LIST)
	@git commit -m "Update $(MAKEFILE_LIST)"
	@git push origin $(git rev-parse --abbrev-ref HEAD)