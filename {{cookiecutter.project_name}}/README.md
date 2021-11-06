# {{cookiecutter.project_title}}

{{cookiecutter.project_short_description}}

# Project Setup

Install all dependencies from Pipfile.lock

`$ pipenv sync --dev`

Install the pre-commit hooks

`$ pipenv run pre-commit install`

Show Pipenv scripts

`$ pipenv scripts`

```bash
Command     Script
----------  ------------------------------------
test        pytest
test:cov    pytest --cov
lint:all    pylint python_project tests setup.py
isort:all   isort python_project tests setup.py
format:all  black python_project tests setup.py
precommit   pre-commit run --all-files

```