# python-cookiecutter

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) for Python projects.

**Main Features**
* [Pipenv](https://github.com/pypa/pipenv) as packaging tool.
* [pylint](https://github.com/PyCQA/pylint) as source code analyzer.
* [pytest](https://github.com/pytest-dev/pytest) as testing framework.
* [pytest-cov](https://github.com/pytest-dev/pytest-cov) to produce coverage reports.
* [isort](https://github.com/timothycrosley/isort) to sort imports.
* [black](https://github.com/psf/black) as (uncompromising) code formatter.
* [pre-commit](https://pre-commit.com/) to manage pre-commit hooks.
* [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) as main configuration file.


## Usage

Install cookiecutter
```bash
$ pip install --user cookiecutter
```

Run cookiecutter pointing to this repo
```bash
$ cookiecutter https://github.com/jonathadv/python-cookiecutter.git
```
