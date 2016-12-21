# -*- coding: utf-8 -*-
import os

from flask import Flask

from .handlers import socketio


def create_app(info):
    app = Flask('cosmicpi_web')

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    socketio.init_app(app, message_queue=os.environ.get('BROKER_URL'))
    return app
