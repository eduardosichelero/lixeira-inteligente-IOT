---
icon: computer
---

# Client

### **Visão Geral do Cliente**

Este cliente Python é a interface para o usuário interagir com a Lixeira Inteligente IoT. Ele foi projetado para se conectar ao servidor via **socket TCP** e enviar comandos para abrir ou fechar a tampa da lixeira. O cliente também é responsável por exibir as respostas do servidor, informando o status da operação.

***

### **Funcionamento Detalhado do Cliente**

#### **Configuração da Conexão**

1. O cliente é configurado para se conectar ao servidor usando um **endereço IP** e uma **porta** predefinidos (geralmente definidos nas variáveis `HOST` e `PORT` dentro do código do cliente).

#### **Menu Interativo**

1. Após a execução, o cliente apresenta um **menu interativo** no console. O usuário pode escolher entre as seguintes opções:
   * `1`: Para enviar o comando "abrir" e solicitar a abertura da tampa da lixeira.
   * `2`: Para enviar o comando "fechar" e solicitar o fechamento da tampa da lixeira.
   * `3`: Para sair do programa do cliente.

#### **Envio de Comando e Resposta**

1. Uma vez que o usuário seleciona uma opção (1 ou 2), o cliente envia o comando correspondente ao servidor.
2. O cliente então aguarda a resposta do servidor e a exibe no console, informando se o comando foi executado com sucesso ou se houve algum erro.

***

### **Principais Funções**

A funcionalidade central do cliente reside na função **`send_command(command)`**.

#### **`send_command(command)`**

Esta função é responsável por toda a interação de rede do cliente.

* **Cria uma conexão TCP**: Estabelece uma conexão socket TCP com o servidor usando o `HOST` e `PORT` configurados.
* **Envia o comando**: Codifica o comando (por exemplo, "abrir" ou "fechar") e o envia através do socket para o servidor.
* **Recebe e imprime a resposta**: Aguarda a resposta do servidor, decodifica-a e a imprime no console para o usuário.

***

### **Exemplo de Uso do Cliente**

Para executar o cliente, navegue até o diretório do projeto e execute o arquivo Python:

Bash

```
python client.py
```

Após a execução, um menu interativo será exibido:

```
Opções:
1. Abrir a lixeira
2. Fechar a lixeira
3. Sair
Escolha uma opção:
```

Siga as instruções do menu para enviar comandos ao servidor.

***

### **Possíveis Erros**

* **Servidor não encontrado**: Este erro ocorre se o cliente não conseguir se conectar ao servidor. As causas comuns incluem:
  * O endereço IP (`HOST`) ou a porta (`PORT`) configurados no cliente estão incorretos.
  * O servidor não está em execução ou está inacessível (por exemplo, bloqueado por um firewall).
  * **Verifique se o IP e a porta estão corretos e se o servidor está em execução e acessível.**
* **Resposta de erro do servidor**: O cliente pode receber mensagens de erro do servidor. Isso acontece se:
  * O Arduino estiver desconectado do servidor.
  * O comando enviado pelo cliente for inválido (apesar do menu interativo minimizar isso).

***

### **Requisitos**

Para executar o cliente, você precisará dos seguintes requisitos:

* **Python 3.x**: A versão 3 ou superior do Python é necessária.
* **Biblioteca padrão `socket`**: Já inclusa no Python, não requer instalação adicional.
* **IP e porta do servidor configurados corretamente**: Certifique-se de que o cliente esteja apontando para o IP e a porta corretos do servidor.

***

### **Segurança**

Este cliente **não implementa nenhum mecanismo de autenticação**. Em ambientes onde a segurança é uma preocupação, é recomendado adicionar funcionalidades como:

* **Autenticação de usuário**: Para garantir que apenas usuários autorizados possam usar o cliente.
* **Criptografia**: Para proteger os dados transmitidos entre o cliente e o servidor.

***

### **Extensões Futuras**

Algumas ideias para melhorar a usabilidade e funcionalidade do cliente:

* **Interface gráfica (GUI)**: Desenvolver uma interface gráfica para tornar o uso mais intuitivo, eliminando a necessidade de um console.
* **Histórico de comandos enviados**: Manter um registro dos comandos enviados e das respostas recebidas.
* **Autenticação de usuário**: Incorporar um sistema de login para autenticar os usuários que acessam a lixeira.

***
