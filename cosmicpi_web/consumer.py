import pika

from flask import current_app

from .handlers import socketio


def consume(broker_url):
    connection = pika.BlockingConnection(pika.URLParameters(broker_url))
    channel = connection.channel()
    queue_name = channel.queue_declare(exclusive=True).method.queue
    channel.queue_bind(exchange='events', queue=queue_name)

    def on_event(channel, method, properties, body):
        current_app.logger.info(body)
        socketio.emit('event', body, namespace='/events')

    channel.basic_consume(on_event, queue=queue_name, no_ack=True)
    channel.start_consuming()
