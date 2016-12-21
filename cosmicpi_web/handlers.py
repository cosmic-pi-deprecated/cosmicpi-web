from flask import current_app
from flask_socketio import SocketIO

socketio = SocketIO()

#
# @socketio.on('connect', namespace='/events')
# def on_connect():
#     current_app.logger.info('Client connected')
