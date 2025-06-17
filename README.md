---
icon: book-open
---

# README

### **Visão Geral do Projeto**

Este projeto desenvolve uma **Lixeira Inteligente IoT** controlada remotamente. No seu cerne, há um servidor Python que atua como um hub central, recebendo comandos de clientes via **socket TCP** e os retransmitindo para um **Arduino** conectado via **porta serial**. O objetivo principal é permitir que usuários abram ou fechem a tampa da lixeira de forma remota, utilizando comandos enviados pela rede.

***

### **Documentação Completa**

Para uma documentação mais detalhada sobre o projeto, sua arquitetura, funcionamento e exemplos de uso, acesse nosso GitBook:

[**Link para o GitBook**](introducao.md)

***

### **Estrutura do Projeto**

O projeto é dividido em dois componentes principais:

* **`server.py`**: Este é o código principal do **servidor**, responsável por toda a lógica de comunicação e controle.
* **`Arduino`**: Refere-se ao hardware Arduino, que é o dispositivo físico encarregado de executar as ações de abrir e fechar a tampa da lixeira.

***

### **Funcionamento Detalhado**

#### **Inicialização do Servidor**

1. Ao iniciar, o servidor tenta estabelecer uma conexão com o **Arduino** na porta serial especificada (padrão: `/dev/ttyACM0` com baudrate `9600`).
2. Caso a conexão com o Arduino falhe, o servidor exibirá uma mensagem de erro e será encerrado.

#### **Servidor TCP**

1. O servidor configura um **socket TCP** para escutar na porta `5000` em todas as interfaces de rede (`0.0.0.0`), tornando-o acessível de qualquer máquina na rede.
2. Ele é capaz de aceitar **múltiplas conexões simultâneas**, gerenciando cada uma delas em uma **thread** separada para garantir a responsividade.

#### **Comunicação com o Cliente**

1. Clientes se conectam ao servidor e enviam comandos de texto simples: "**abrir**" ou "**fechar**".
2. O servidor executa as seguintes validações e ações:
   * **Comando Válido e Arduino Conectado**: Se o comando for "abrir" ou "fechar" e o Arduino estiver conectado, o comando é enviado via comunicação serial para o Arduino.
   * **Arduino Desconectado**: Se o Arduino não estiver disponível, o servidor retorna uma mensagem de erro ao cliente informando sobre a desconexão.
   * **Comando Inválido**: Se o comando recebido não for "abrir" nem "fechar", o servidor envia uma mensagem de uso correto ao cliente, indicando os comandos permitidos.
3. Após processar o comando, o servidor responde ao cliente com o status da operação (sucesso ou erro).

#### **Encerramento do Servidor**

1. O servidor pode ser encerrado de forma segura pressionando `CTRL+C` no terminal onde está em execução.
2. Durante o encerramento, o servidor garante o fechamento adequado da conexão com o Arduino e do socket do servidor, liberando os recursos.

***

### **Instalação e Execução**

Para colocar o projeto em funcionamento, siga os passos abaixo:

1.  **Instale as dependências** do Python:

    ```bash
    pip install pyserial
    ```
2.  **Execute o servidor** para monitorar eventos e repassar os comandos ao Arduino:

    ```bash
    python server/server.py
    ```
3.  Em outro terminal, **execute o cliente** para interagir com a lixeira:

    ```bash
    python client/client.py
    ```

***

### **Integrantes do Projeto**

**Grupo Cliente:**

* 1134868 - Ábner Panazollo
* 1134821 - Vitor Quadros
* 1135384 - Gabriel Onofre

**Grupo Servidor:**

* 1134433 - Ariel Diefenthaeler
* 1134933 - Eduardo Sichelero
