#!python3
from setuptools import setup
desc = '''
Nustack is a stack-oriented concatenative programming language
with support for high-level modular programming and Python integration.

For more info, please visit https://gitub.com/BookOwl/Nustack
'''

setup(
    name='nustack',

    version="0.9.1",

    description='Nustack programming langusge',
    long_description=desc,

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

    packages=["nustack", "nustack.doc", "nustack.stdlib"],

    install_requires=["requests>=2.8,<3",]

    entry_points={
    'console_scripts': [
        'nustack=nustack.__main__:main',
        ],
    },
)
