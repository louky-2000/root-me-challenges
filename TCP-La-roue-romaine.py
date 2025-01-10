import socket as sc
import re, codecs

def decodeRot13(cipher: str) -> str:
  """Décode un message encodé avec l'algorithme ROT13."""
  return codecs.decode(cipher, 'rot_13')

def main(host: str, port: int) -> None:
  try:
    with sc.socket(sc.AF_INET, sc.SOCK_STREAM) as client_socket:
      print(f"Connexion à {host}:{port}...")
      client_socket.connect((host, port))
      print("Connecté avec succès !\n")

      # Réception du message du serveur
      data = str(client_socket.recv(1024).decode('utf-8').strip())
      print(f"Reçu du serveur :\n{data}")

      # Extraction de la chaîne encodée
      extracted = re.findall(r"'(.*?)'", data)
      encoded_string = extracted[0]
      print(f"Chaîne encodée : {encoded_string}")

      # Décodage avec ROT13
      decoded_string = decodeRot13(encoded_string)
      print(f"Chaîne décodée à envoyer : {decoded_string.strip()}")

      # Envoi de la chaîne décodée
      client_socket.sendall((decoded_string.strip() + '\n').encode('utf-8'))

      # Réception de la réponse du serveur
      response = str(client_socket.recv(1024).decode('utf-8').strip())
      print(f"Réponse du serveur :\n{response}")
      
      client_socket.close()
  except Exception as e:
    print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
  host = "challenge01.root-me.org"
  port = 52021
  main(host, port)
