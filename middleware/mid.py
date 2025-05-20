import pika
import serial
import time
import json
from src.config import RABBIT_CONFIG

arduino = serial.Serial('COM3', 9600) 

params = pika.URLParameters(RABBIT_CONFIG)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange='sistema_lixeira', exchange_type='topic', durable=True)

def publish_event(routing_key, evento):
    mensagem = json.dumps(evento)
    channel.basic_publish(
        exchange='sistema_lixeira',
        routing_key=routing_key,
        body=mensagem,
        properties=pika.BasicProperties(delivery_mode=2)  
    )
    print(f"[ENVIADO] {routing_key}: {mensagem}")

def listen_serial():
    while True:
        if arduino.in_waiting > 0:
            linha = arduino.readline().decode().strip()
            print(f"[ARDUINO] {linha}")

            if linha == "Botão pressionado":
                publish_event('lixeira.evento', {"tipo": "botao_pressionado"})
            elif linha == "Abrindo tampa":
                publish_event('lixeira.status', {"status": "abrindo"})
            elif linha == "Tampa aberta":
                publish_event('lixeira.status', {"status": "aberta"})
                
        time.sleep(0.1)

if __name__ == "__main__":
    print("Middleware iniciado. Pressione CTRL+C para sair.")
    try:
        listen_serial()
    except KeyboardInterrupt:
        print("\nEncerrando middleware.")
        arduino.close()
        connection.close()