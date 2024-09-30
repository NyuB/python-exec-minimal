# Cookiecutter template for a minimal Python3 executable

## Usage

**NB**: The [cookiecutter documentation](https://cookiecutter.readthedocs.io/en/stable/usage.html) will always be the most up-to-date regarding cookiecutter usage. The following instructions are just a quickstart helper.

```console
$ cookiecutter gh:NyuB/python-exec-minimal
[1/4] name (main): my-awesome-tool
[2/4] main_name: (my_awesome_tool)
[3/4] description: (An awesome tool)
[4/4] python3: (/bin/python3)
...
$ ls my-awesome-tool
.gitignore
Makefile
my_awesome_tool.py
README.md
requirements.txt
tests.t
```

## Template variables

- **name**: Your project's name, and the generated folder's name.
- **main_name**: The main script name.
- **description**: A description of the executable role
- **python3**: python 3 path
