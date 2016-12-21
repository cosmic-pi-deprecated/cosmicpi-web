# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os

import pika
import click

from flask import Flask
from flask.cli import FlaskGroup, with_appcontext
from flask_socketio import SocketIO

app = Flask('cosmicpi_web')
socketio = SocketIO(app, message_queue=os.environ.get('BROKER_URL'))


@app.route('/')
def index():
    return app.send_static_file('index.html')


@click.group(cls=FlaskGroup, create_app=lambda info: app)
def main():
    """This is the main entry point for the web application."""


@main.command()
@click.option('--broker-url', envvar='BROKER_URL')
@with_appcontext
def consume(broker_url):
    connection = pika.BlockingConnection(pika.URLParameters(broker_url))
    channel = connection.channel()
    queue_name = channel.queue_declare(exclusive=True).method.queue
    channel.queue_bind(exchange='events', queue=queue_name)

    def on_event(channel, method, properties, body):
        app.logger.info(body)
        socketio.emit('event', body, namespace='/events')

    channel.basic_consume(on_event, queue=queue_name, no_ack=True)
    channel.start_consuming()


__author__ = """CosmicPi team"""
__email__ = 'info@cosmicpi.org'
__version__ = '0.2.1'
__all__ = ('app', 'main')
