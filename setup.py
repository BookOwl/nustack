#!python3
from setuptools import setup, find_packages

setup(
    name='nustack',

    version="0.1.0",

    description='Nustack programming langusge',
    long_description="Nustack is a stack-oriented concatenative programming language with support for high-level modular programming and Python integration",

    url='https://github.com/BookOwl/nustack',

    author='Matthew S. (BookOwl)',
    author_email='Unknown',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='nustack programming language',

    packages=find_packages()
)
