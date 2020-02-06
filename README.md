# Example Python Project

This is an example python project that sets up a best practice layout and starts
with a basic CI pipeline preconfigured. It contains series of guidelines on 
style, resources, structure, and tools to help build sustainable software.

## Table of Contents
  - [Project Structure](#project-structure)
  - [Python Project Structure](#python-project-structure)
    - [Virtual Environments](#virtual-environments)
    - [Documentation](#documentation)
    - [Typing](#typing)
    - [Requirements](#requirements)
  - [Version Control](#version-control)
    - [Git](#git)
    - [Changelog](#changelog)
    - [Versioning](#versioning)
  - [Continuous Integration](#continuous-integration)
    - [Peer Reviews](#peer-reviews)
    - [Unit Tests - PyTest](#unit-tests-pytest)
    - [Code Standards - Pylint](#code-standards-pylint)
    - [Packaging - Wheels](#packaging-wheels)
    - [Releases](#Releases)

## Project Structure

All projects should have a descriptive `README.md` to detail its purpose, usage,
and other information. This project includes an example of a detailed readme.
At a minimum a readme should contain:

``` markdown
# Project Title
Project description

## Usage
This should detail how to use the program command line flags, environment
variables, configuration files or other ways of settings program state.

## Installation howto
This should contain installation instructions, prerequisites, and
verification steps.

## Developer Information
This should include running tests, deployment, and contribution information.
```

#### Useful Reading:
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Python Project Structure

### Virtual Environments

Python applications will often use packages and modules that don’t come as part
of the standard library.  Applications will sometimes need a specific version of
a library.

This means it may not be possible for one Python installation to meet the
requirements of every application.  If application A needs version 1.0 of a
particular module but application B needs version 2.0, then the requirements are
in conflict and installing either version 1.0 or 2.0 will leave one application
unable to run.

The solution for this problem is to create a virtual environment, a
self-contained directory tree that contains a Python installation for a
particular version of Python, plus a number of additional packages.

There are two recommended solutions when to manage virtual environments. The
first is to manually create virtual environments directly with `venv`, the
second is using the `pipenv` package.

``` bash
# Using venv on Linux operating systems:
python -m venv /path/to/venv
source /path/to/venv/bin/activate

# Using venv on Windows operating systems:
py -3 -m venv C:\path\to\venv
C:\path\to\venv\Scripts\activate.bat
```

``` bash
# Using pipenv on Linux operating systems:
# (This command installs pipenv to the system python package directory)
sudo python -m pip install pipenv
cd /path/to/project
pipenv shell

# Using venv on Windows operating systems:
py -3 -m pip install pipenv
cd :\path\to\project
pipenv shell
```
> **WARNING:** You should always create python virtual environments to install packages
> to, this is particulary important on Linux which often has OS dependencies on
> the system python. To this end never run the pip command with sudo or elevated
> privileges, this avoid accidently modifying the system python or its packages.

> *NOTE:* Additionaly on Linux systems it is best to avoid the distributions
> package management system (`yum` and `apt`) to install python packages.
> Packages should be installed via `pip`.

#### Useful Reading:

* [Pipenv Documentation](https://pipenv.readthedocs.io/en/latest/install/)

### Documentation
The python language has built in support for documentation and is available at
any point using the builtin `help()` function.

``` python
>>> help(print)
```
```
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
```
The help function pulls the provided docstring from the `__doc__` attribute.
This can be set by added a multiline string immediatly after defining a class,
function, or module.

``` python
""" Module Docstring """

class Example:
    """ Class Docstring """

    def example(self):Mangement
        """ Method Docstring """

def example():
    """ Function Docstring """
```

Documentation should be added to all public functions, classes, and attributes. It is encouraged to use the [Google Styleguide Docstrings](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
for interfaces that is expected to be used by other developers. This enables
documentation to be built automatically for code. Standard strings
should be sufficient for internal methods or very simple objects.

#### Useful Reading:

* [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
* [Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

### Typing

Since python 3.5 python supports typing hints. Typing hints are a way of
giving IDEs or static typing tools such as `Mypy` a way of compile-time type
checking. For example if you created a basic arithmatic function you would
expect it to only be given floats as arguments. You can detail this as a
soft requirement through typing.

``` python
# This function expects to recieve two float arguments and will return a float
def add_numbers(variable_a: float, variable_b: float) -> float:
    return variable_a + variable_b
```
Typing is entirely optional and has no impact on runtime python. Duck-typing
will still work and no run-time error will be raised if you provide a different
set of data types in the above example.

A project should decide to what level typing will be useful and decide early if
it wants it to be added.

#### Useful Reading:

* [typing module documentation](https://docs.python.org/3/library/typing.html)

### Requirements

Python dependency management has gone through a number of iterations and it can
be difficult to determine which system is the correct one to use.

The current recommendations are:

* Populate the setup.py with dependent packages.
* Populate the `requirements.txt` with exact versions if required.

Example: `requirements.txt` 
``` bash
requests>=2.3.0  # Require at least v2.3.0
lxml==3.8.0      # Require exactly v3.8.0
pyyaml>=3.05,<=3.10 # Require at least v3.05 but a maximum of v3.10
pytest           # Any version
```

Example: `setup.py`
``` python
setup(
    ...
    install_requires=['requests', 'lxml', 'pyyaml', 'pytest'],
    ...
)
```

#### Useful Reading:
* [Requirements File Format](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format)

## Version Control

### Git

Commit messages should be descriptive to the contents of that commit. It should
generally be a logical change, avoid messages with changed x *and* y, that
should be two commits. Merge requests can contain the infromation pertaining to
the feature or bugfix being developed.

Commits should be logical units of work. Prehaps a new function or modifications
to a similar syntax. It is not necessary to preplan these changes as you can use
history altering commands to merge, split, or cherry-pick components from 
commits. Useful commands to know are:

``` bash
# Change/Add to the previous commit
git commit --amend
# Change/Add to any commit in this branch
git commit --fixup 981fffd
git rebase --autosquash --interative 22f759b
```

Projects should all use the gitflow style of branch management. Smaller projects
may forego the develop branch if desired.

History altering commands should be used with caution, and should **never** be
used on the master or develop branches. Rebasing of temporary branches is
encouraged as is the logical grouping of changes into commit which can be
achieved via ammends, and interactive rebases. However if multiple people are
working on a single branch history alterations should be synchronised as soon as
possible.

Conflicts can be complex and IDEs can be helpful to resolve many changes. Both
VSCode and PyCharm have GUI helpers to resolve conflicts. Conflicts typically
occur when rebasing a temporary branch onto the develop/master branch that has
had other changes.

Temporary branches should take the following name forms:
``` bash
# Standard feature branch
git checkout -b feature/new_feature_to_add
# Bugfix branch
git checkout -b bugfix/correction_to_code
# Time critical hotfix
git checkout -b hotfix/important_fix_to_merge_to_master
```

Rebasing should occur on any temporary branch before it can be merged into
develop/master.
``` bash
git checkout develop
git pull
git checkout feature/feature_to_merge
git rebase develop
git push -f orgin feature/feature_to_merge
# Create merge request in Gitlab
```

#### Useful Reading:
* [Interactive Git Branching Tutorial](https://learngitbranching.js.org/)
* [Gitflow Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)

### Changelog

Changelogs should be kept for projects. This is important for deployment and
updating security processes on releases. The preferred changelog format is 
*keepachangelog*, link below. This project includes an example.

#### Useful Reading:
* [Changelog Format](https://keepachangelog.com/en/1.0.0/)

### Versioning

Projects can use any versioning scheme supported by PEP440. Semantic versioning
should be used for projects with defined public interfaces. Otherwise a fixed
incremented number where breaking changes do not have impacts.

Versions should be specified in the module `__version__.py` as per this example.
They will automatically be set by the `setup.py` and packaged into and built
distribution.

#### Useful Reading:
* [PEP 440 -- Version Identification and Dependency Specification](https://www.python.org/dev/peps/pep-0440/)
* [Semantic Versioning](https://semver.org/)


## Continuous Integration

### Peer Reviews

Peer reviews are an important part of the CI pipeline. Code should be
reviewed and approved by at least one peer before being merged into develop or
master branches for a project. Gitlab has full support for peer reviews through
its merge request system. Merge requests should be created through the Gitlab
interface for any branch that wants to be merged in.

Comments can reflect identified problems or stylistic issues but should be kept
profesional and considerate. Style comments should consider some leeway in an
individuals preference with the goal of getting maintainable software.

### Unit Tests - PyTest

#### Useful Reading:
* [PyTest Documentation](https://docs.pytest.org/en/latest/)
* [Mock - Getting Started](https://docs.python.org/3/library/unittest.mock-examples.html)

### Code Standards - Pylint

#### Useful Reading:
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [Raymond Hettinger - Beyond PEP 8 -- Best practices for beautiful intelligible code - PyCon 2015](https://youtu.be/wf-BqAjZb8M)
* [PyLint Documentation](https://www.pylint.org/)

### Packaging - Wheels
The modern python binary package format is called a wheel, this intends to replace the
deprecated `.egg` format. The alternative distribution is a source distribution
or sdist mostly shared as a `.tar.gz` or a `.zip`.

``` bash
# Building a source distribution
python setup.py sdist

# Building a wheel distribution (Requires the package wheel)
python setup.py bdist_wheel
```

These distributions can then be used to install the package into your python
environment. It is recommended to always use `pip` to install both wheels and
source distributions to correctly resolve dependencies.

#### PyPi

The Python Package Index (PyPi) is a public repository for python packages.
Packages can be published for general availablity.

This will require an account with PyPi. The recommended upload tool is `twine`.

``` bash
# For test uploads
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

#### Private Repository

Private repositories can also be created. The simplest library to use is
`pypiserver`. 

Pip can be configured to use a custom repository by using the following
commands:

``` bash
pip config set global.extra-index-url 'https://example.org/simple/'
pip config set global.cert '/etc/pki/tls/certs/ca-bundle.crt'
```

### Publishing Wheels

An automated publish stage has been added to this project it uses
[twine](https://pypi.org/project/twine/) to publish packages to this repository.

The gitlab pipeline has been configured to use environment variables for
specifying the PyPi server, username, and password. Set set these for your
project have a look at the Gitlab Project -> Settings -> CI/CD Settings -> 
Environment Variables. The server uses basic auth via username password and ssl
for encryption. For more details on the server configuration please see the
Documentation Wiki -> PyPi Server Configuration.

#### Useful Reading:
* [Using TestPyPi](https://packaging.python.org/guides/using-testpypi/)
* [PEP 427 -- The Wheel Binary Package Format 1.0](https://www.python.org/dev/peps/pep-0427/)

### Releases
Releases should be considered the formal process of promoting code from
development through testing, QA infrastructure to production infrastructure.

In mature devops models testing, and QA infrastructures are automatically
deployed and production promoting is done via a simple approval.

