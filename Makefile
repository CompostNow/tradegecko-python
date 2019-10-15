.PHONY: help default test check format
.DEFAULT_GOAL := help
PROJECT := tradegecko

help:                      ## Show help.
	@grep -E '^[a-zA-Z2_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


test:                    ## Run tests and coverage.
	@py.test -v --cov "$(PROJECT)" "$(PROJECT)"


check:                   ## Run code checks.
	@flake8 "$(PROJECT)"
	@pydocstyle "$(PROJECT)"


format:                  ## Format the code.
	@black --target-version=py37 --safe --line-length=79 .
