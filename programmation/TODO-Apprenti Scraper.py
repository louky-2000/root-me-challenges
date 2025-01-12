import socket as sc
import re, base64

def main(host : str, port : int) -> None :
  try:
    with sc.socket(sc.AF_INET,sc.SOCK_STREAM) as client_socket :
      print(f"Connecting to {host}:{port}...")
      client_socket.connect((host, port))
      print("Connected successfully!\n")

      data = str(client_socket.recv(1024).decode('utf-8').strip())
      print(data)
      data = str(client_socket.recv(1024).decode('utf-8').strip())
      print(data)

      data = str(client_socket.recv(1024).decode('utf-8').strip())
      print(data)
      # data = re.findall(r"\'.*\'",data)[0]

      # client_socket.sendall((f"{base64.b64decode(data).decode('utf-8')}\n").encode('utf-8'))

      # data = str(client_socket.recv(1024).decode('utf-8').strip())
      # print(data)
      
      client_socket.close()
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__" :
  host = "ctf13.root-me.org"
  port = 4444
  main(host, port)