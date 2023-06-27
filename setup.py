from setuptools import setup, find_packages
from setuptools.command.install import install
from os import path
import subprocess

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    # $ pip install omero-wrapper
    name='omero-wrapper',
    version='0.0.1',
    description='Wrapper for omero cli',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/estorrs/omero-wrapper',
    author='Erik Storrs',
    author_email='estorrs@wustl.edu',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='omero command line tool wrapper',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'omero-py',
    ],
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'omero-wrapper=omero_wrapper.omero:main',
        ],
    },
)
