#!/usr/bin/env python3
# coding=utf-8
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.88.238'))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback, queue='hello', no_ack=True)
channel.start_consuming()
