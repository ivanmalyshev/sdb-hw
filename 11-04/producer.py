#!/usr/bin/env python3
# coding=utf-8
import pika
credentials = pika.PlainCredentials('mid', 'midx11011')
#connection = pika.BlockingConnection(pika.ConnectionParameters('rmq1', 5672, '/', credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters('rmq2', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
connection.close()
