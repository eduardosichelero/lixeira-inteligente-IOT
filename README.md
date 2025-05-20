# lixeira-inteligente-IOT

Sistema de lixeira inteligente utilizando Arduino e RabbitMQ.

## Instalação

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Execute o middleware:

   ```bash
   python middleware/mid.py
   ```

3. Execute o consumidor para monitorar eventos:

   ```bash
   python consumers/all_events.py
   ```
