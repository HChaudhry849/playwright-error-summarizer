# -*- coding: utf-8 -*-
from setuptools import setup
import os

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='playwright-error-summarizer',
    version='0.1',
    packages=['playwright_error_summarizer'],
    install_requires=[
        'playwright',
    ],
    entry_points={
        'console_scripts': [
            'summarise-playwright-errors=playwright_error_summarizer.main:main',
        ],
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
)