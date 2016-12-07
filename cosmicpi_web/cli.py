# -*- coding: utf-8 -*-

from __future__ import absolute_import

import click
from flask.cli import FlaskGroup

from .cosmicpi_web import app


@click.group(cls=FlaskGroup, create_app=lambda info: app)
def main():
    """This is the main entry point for the web application."""
