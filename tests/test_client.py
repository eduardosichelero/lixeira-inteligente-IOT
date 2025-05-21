import socket

HOST = 'localhost'
PORT = 5000

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(command.encode())
        resposta = s.recv(1024).decode()
        print(f"[CLIENTE] Resposta: {resposta}")

if __name__ == "__main__":
    while True:
        print("\n--- MENU ---")
        print("1 - Abrir tampa")
        print("2 - Fechar tampa")
        print("3 - Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            send_command("abrir")
        elif opcao == '2':
            send_command("fechar")
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")
