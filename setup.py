#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'flask>=0.11',
    'pika>=0.10.0',
]

test_requirements = [
]

setup(
    name='cosmicpi_web',
    version='0.2.0',
    description="Web frontend for Cosmic Pi",
    long_description=readme + '\n\n' + history,
    author="CosmicPi team",
    author_email='info@cosmicpi.org',
    url='https://github.com/CosmicPi/cosmicpi-web',
    packages=[
        'cosmicpi_web',
    ],
    package_dir={'cosmicpi_web':
                 'cosmicpi_web'},
    entry_points={
        'console_scripts': [
            'cosmicpi_web=cosmicpi_web.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='cosmicpi_web',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
