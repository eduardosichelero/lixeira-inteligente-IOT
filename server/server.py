import socket
import threading
import serial

class ServerController:
    def __init__(self):
        self.running = True
        self.server = None
        self.arduino = None
        self.ARDUINO_PORT = '/dev/ttyACM0'
        self.ARDUINO_BAUD = 9600

    def handle_client(self, client_socket):
        try:
            while self.running:
                data = client_socket.recv(1024).decode().strip()
                if not data:
                    break

                print(f"[SERVIDOR] Comando recebido: {data}")

                arduino_ok = self.arduino and self.arduino.is_open

                if data in ["abrir", "fechar"]:
                    if arduino_ok:
                        self.arduino.write(f"{data}\n".encode())
                        response = "Comando executado!"
                    else:
                        response = "Erro: Arduino desconectado!"
                else:
                    response = "Comando inválido. Use 'abrir' ou 'fechar'"

                client_socket.send(response.encode())

        except Exception as e:
            print(f"[ERRO] {e}")
        finally:
            client_socket.close()

    def shutdown_server(self):
        self.running = False

        if self.arduino and self.arduino.is_open:
            self.arduino.close()
            print("\n[Conexão Arduino] Desconectado")

        if self.server:
            self.server.close()
            print("[Servidor] Desligado corretamente")

    def start_server(self):
        try:
            self.arduino = serial.Serial(
                self.ARDUINO_PORT,
                self.ARDUINO_BAUD,
                timeout=1
            )
            print(f"[ARDUINO] Conectado em {self.ARDUINO_PORT}")
        except Exception as e:
            print(f"[ERRO] Falha ao conectar no Arduino: {e}")
            return

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('0.0.0.0', 5000))
        self.server.listen(5)
        print("[SERVIDOR] Ouvindo na porta 5000...")
        print("Pressione CTRL+C para encerrar\n")

        try:
            while self.running:
                client_sock, addr = self.server.accept()
                print(f"[SERVIDOR] Conexão de {addr[0]}:{addr[1]}")
                threading.Thread(
                    target=self.handle_client,
                    args=(client_sock,)
                ).start()
        except KeyboardInterrupt:
            self.shutdown_server()
        except Exception as e:
            print(f"[ERRO CRÍTICO] {e}")
        finally:
            self.shutdown_server()

if __name__ == "__main__":
    ServerController().start_server()
