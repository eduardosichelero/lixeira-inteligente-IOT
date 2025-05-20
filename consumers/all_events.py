import pika
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.config import RABBIT_CONFIG

def callback(ch, method, properties, body):
    print(f"[MONITOR] Nova mensagem recebida - Routing Key: {method.routing_key}")
    print(f"          Conteúdo: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

params = pika.URLParameters(RABBIT_CONFIG)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='sistema_lixeira', exchange_type='topic', durable=True)
channel.queue_declare(queue='fila_monitor', durable=True)
channel.queue_bind(exchange='sistema_lixeira', queue='fila_monitor', routing_key='lixeira.#')

print(" [*] Monitor iniciado. Aguardando mensagens...")
channel.basic_consume(queue='fila_monitor', on_message_callback=callback, auto_ack=False)
channel.start_consuming()
