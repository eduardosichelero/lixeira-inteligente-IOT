---
icon: python
---

# Server

### **Principais Classes e Métodos**

A lógica principal do servidor é encapsulada na classe **`ServerController`**.

#### **`ServerController`**

Esta classe gerencia a inicialização, a comunicação com clientes e o Arduino, e o encerramento do servidor.

**Atributos**

* **`running`**: Uma _flag_ booleana que controla o loop principal do servidor. Quando `False`, o servidor é desligado.
* **`server`**: A instância do objeto **socket** do servidor, responsável por escutar e aceitar conexões de clientes.
* **`arduino`**: A instância da conexão serial com o **Arduino**, usada para enviar comandos ao hardware.
* **`ARDUINO_PORT`**: String que define a porta serial onde o Arduino está conectado (ex: `"/dev/ttyACM0"`).
* **`ARDUINO_BAUD`**: Inteiro que define a taxa de transmissão (baudrate) da comunicação serial com o Arduino (padrão: `9600`).

**Métodos**

* **`start_server()`**: Este método é o ponto de entrada para iniciar o servidor. Ele:
  * Tenta inicializar a conexão serial com o Arduino.
  * Configura o socket do servidor TCP para escutar por conexões.
  * Entra em um loop para aceitar e gerenciar novas conexões de clientes, despachando cada uma para uma _thread_ separada.
* **`handle_client(client_socket)`**: Responsável por lidar com a comunicação de um único cliente conectado. Dentro desta função:
  * Ela recebe os comandos do cliente.
  * Valida os comandos e os retransmite para o Arduino, se aplicável.
  * Envia a resposta de volta ao cliente.
* **`shutdown_server()`**: Método invocado para encerrar o servidor de forma graciosa. Ele:
  * Fecha a conexão serial com o Arduino.
  * Fecha o socket principal do servidor, impedindo novas conexões.
  * Define a _flag_ `running` como `False` para finalizar o loop principal.

***

### **Exemplo de Uso do Servidor**

Para iniciar o servidor, execute o arquivo `server.py` no seu terminal:

Bash

```
python server.py
```

Para interagir com o servidor, você pode usar um cliente (veja a seção de documentação do cliente abaixo) ou ferramentas como `netcat`.

**Exemplo de Envio de Comando (usando netcat):**

Abra um novo terminal ou máquina e envie um comando para o servidor:

Bash

```
echo "abrir" | nc <IP_DO_SERVIDOR> 5000
echo "fechar" | nc <IP_DO_SERVIDOR> 5000
```

Substitua `<IP_DO_SERVIDOR>` pelo endereço IP da máquina onde o servidor está em execução.

***

### **Possíveis Erros**

* **Erro ao conectar no Arduino**: Isso pode acontecer se o Arduino não estiver conectado à porta serial correta, se a porta estiver sendo usada por outro programa, ou se o nome da porta (`ARDUINO_PORT`) ou o `ARDUINO_BAUD` estiverem incorretos. **Verifique se o Arduino está conectado e os parâmetros de configuração estão corretos.**
* **Comando inválido**: O servidor está programado para aceitar apenas os comandos "**abrir**" e "**fechar**". Qualquer outro comando será rejeitado.
* **Arduino desconectado**: Se a conexão com o Arduino for perdida após o servidor iniciar, o servidor não conseguirá enviar comandos para a lixeira, retornando uma mensagem de erro ao cliente.

***

### **Requisitos**

Para executar o servidor, você precisará dos seguintes requisitos:

* **Python 3.x**: A versão 3 ou superior do Python é necessária.
* **Bibliotecas Python**:
  * **`socket`**: Biblioteca padrão do Python para comunicação de rede.
  * **`threading`**: Biblioteca padrão do Python para lidar com múltiplas threads (para conexões simultâneas).
  *   **`serial` (pyserial)**: Biblioteca para comunicação serial com o Arduino. Instale-a via pip:Bash

      ```
      pip install pyserial
      ```
* **Arduino conectado via USB**: O hardware Arduino deve estar fisicamente conectado ao computador onde o servidor está rodando.

***

### **Segurança**

Atualmente, o servidor aceita conexões de **qualquer endereço IP**. Para um ambiente de produção ou em cenários onde a segurança é crítica, **é altamente recomendável implementar medidas de segurança adicionais**:

* **Restringir o acesso por firewall**: Configure as regras do firewall para permitir conexões na porta 5000 apenas de IPs confiáveis.
* **Implementar autenticação**: Adicione um mecanismo de autenticação para que apenas clientes autorizados possam enviar comandos.

***

### **Extensões Futuras**

Algumas ideias para expandir a funcionalidade do servidor:

* **Implementar autenticação de clientes**: Exigir credenciais para que um cliente possa enviar comandos.
* **Adicionar comandos para status da lixeira**: Por exemplo, um comando para verificar se a lixeira está aberta ou fechada.
* **Interface web para controle remoto**: Desenvolver uma interface web para controlar a lixeira de um navegador.

***

### **Contato**

Para dúvidas ou sugestões relacionadas ao servidor, entre em contato com o desenvolvedor responsável pelo projeto.
