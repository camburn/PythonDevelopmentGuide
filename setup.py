import os
from setuptools import find_packages, setup

NAME = 'my_module'
DESCRIPTION = 'An example python project'
REQUIRED_PYTHON = '>=3.7.0'
LICENSE = 'MIT'
REQUIRED = [  # A list of required dependencies
    # 'requests',
]  
EXTRAS = {}

pwd = os.path.abspath(os.path.dirname(__file__))
about = {}

try:
    with open(os.path.join(pwd, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

with open(os.path.join(pwd, NAME, '__version__.py')) as f:
    exec(f.read(), about)

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    license=LICENSE,
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=REQUIRED_PYTHON,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    extras_require=EXTRAS
)
