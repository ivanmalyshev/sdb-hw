#!/usr/bin/env python3
# coding=utf-8
import pika
credentials = pika.PlainCredentials('mid', 'midx11011')
#connection = pika.BlockingConnection(pika.ConnectionParameters('rmq1', 5672, '/', credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters('rmq2', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


#channel.basic_consume(callback, queue='hello', no_ack=True)
channel.basic_consume('hello', callback, auto_ack=True)
channel.start_consuming()

