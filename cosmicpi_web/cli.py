# -*- coding: utf-8 -*-

from __future__ import absolute_import

import click
from flask.cli import FlaskGroup, with_appcontext

from .cosmicpi_web import create_app
from . import consumer


@click.group(cls=FlaskGroup, create_app=create_app)
def main():
    """This is the main entry point for the web application."""


@main.command()
@click.option('--broker-url', envvar='BROKER_URL')
@with_appcontext
def consume(broker_url):
    consumer.consume(broker_url)


