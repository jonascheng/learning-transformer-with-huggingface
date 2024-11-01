.DEFAULT_GOAL := help

.PHONY: setup
setup: ## setup
	python -m pip install --upgrade pip
	pip install -r requirements.txt -q

.PHONY: jupyter
jupyter: setup ## start jupyter notebook
	jupyter lab build
	Jupyter-lab

.PHONY: help
help: ## prints this help message
	@echo "Usage: \n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
