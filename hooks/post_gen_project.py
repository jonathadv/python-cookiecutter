#!/usr/bin/env python
import os
import subprocess

GIT_INIT_MSG = """
--------------------------------------------------
Creating a git repo and adding all files
--------------------------------------------------
"""

PIPENV_MSG = """
--------------------------------------------------
Installing all project dependencies with Pipenv
--------------------------------------------------
"""

PRECOMMIT_SETUP_MSG = """
--------------------------------------------------
Installing git hooks
--------------------------------------------------
"""

IS_GIT_INIT_ENABLED = "{{ cookiecutter.run_git_init }}" == "y"
IS_PIPENV_INSTALL_ENABLED = "{{ cookiecutter.run_pipenv_install }}" == "y"
IS_HOOKS_INSTALL_ENABLED = "{{ cookiecutter.install_pre_commit_hooks }}" == "y"


def get_python_path():
    result = subprocess.run(["pipenv", "--py"], stdout=subprocess.PIPE)
    python_path = result.stdout.decode('utf-8').replace("\n", "")
    return python_path


def run_git_init():
    print(GIT_INIT_MSG)
    os.system("git init")
    os.system("git add -A")


def display_virtualenv_paths():
    print("\n\n")
    print("--------------------------------------------------")
    print("🐍 - Your virtualenv is here:")
    os.system("pipenv --venv")

    print("🐍 - Your Python path is:")
    os.system("pipenv --py")
    print("--------------------------------------------------")


def run_pipenv_install():
    print(PIPENV_MSG)
    os.system("pipenv install --dev")
    display_virtualenv_paths()


def install_pre_commit():
    print(PRECOMMIT_SETUP_MSG)
    os.system("pipenv run pre-commit install")
    os.system("pipenv run pre-commit run check-yaml")


if __name__ == "__main__":
    if IS_GIT_INIT_ENABLED:
        run_git_init()

    if IS_PIPENV_INSTALL_ENABLED:
        run_pipenv_install()

    if IS_PIPENV_INSTALL_ENABLED and IS_HOOKS_INSTALL_ENABLED:
        install_pre_commit()
