import socket as sc
import re, math

def main(host : str, port : int) -> None :
  try:
    with sc.socket(sc.AF_INET,sc.SOCK_STREAM) as client_socket :
      print(f"Connecting to {host}:{port}...")
      client_socket.connect((host, port))
      print("Connected successfully!\n")

      data = str(client_socket.recv(1024).decode('utf-8').strip())
      print(data)
      data = [int(num) for num in re.findall("\d+",data)]

      print(f"Found numbers : {data}")

      data = math.sqrt(data[1]) * data[2]
      data = f"{data:.2f}"

      print(f"Result = {data}")

      client_socket.sendall((f"{data}\n").encode('utf-8'))

      data = str(client_socket.recv(1024).decode('utf-8').strip())
      print(data)
      
      client_socket.close()
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__" :
  host = "challenge01.root-me.org"
  port = 52002
  main(host, port)