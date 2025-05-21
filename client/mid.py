import socket

HOST = '10.1.25.154'  # IP do Raspberry Pi
PORT = 5000

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(command.encode())
        response = s.recv(1024).decode()
        print(f"[RESPOSTA] {response}")

if __name__ == "__main__":
    opcoes = {
        '1': 'abrir',
        '2': 'fechar'
    }

    while True:
        print("\n--- CONTROLE DA LIXEIRA ---")
        print("1 - Abrir Tampa")
        print("2 - Fechar Tampa")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao in opcoes:
            send_command(opcoes[opcao])
        elif opcao == '3':
            break
        else:
            print("Opção inválida!")
