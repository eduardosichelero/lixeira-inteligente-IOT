import pika
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.config import RABBIT_CONFIG

connection = pika.BlockingConnection(pika.URLParameters(RABBIT_CONFIG))
channel = connection.channel()
channel.exchange_declare(exchange='sistema_lixeira', exchange_type='topic', durable=True)

eventos = [
    {"evento": "servo_iniciando"},
    {"evento": "abrindo_lixeira"},
    {"evento": "lixeira_aberta"}
]

for evento in eventos:
    mensagem = json.dumps(evento)
    channel.basic_publish(
        exchange='sistema_lixeira',
        routing_key='lixeira.status',
        body=mensagem
    )
    print(f"[ENVIADO] Mensagem: {mensagem}")

connection.close()
