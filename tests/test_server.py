import socket
import threading

def handle_client(conn, addr):
    print(f"[SERVIDOR] Conexão de {addr}")
    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if not data:
                break

            print(f"[SERVIDOR] Comando recebido: {data}")
            if data == "abrir":
                resposta = "Tampa aberta"
            elif data == "fechar":
                resposta = "Tampa fechada"
            else:
                resposta = "Comando inválido"

            conn.sendall(resposta.encode())

        except Exception as e:
            print(f"[ERRO] {e}")
            break
    conn.close()

def start_server():
    host = 'localhost'
    port = 5000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[SERVIDOR] Ouvindo em {host}:{port}")

    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
    except KeyboardInterrupt:
        print("\n[SERVIDOR] Encerrado")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
