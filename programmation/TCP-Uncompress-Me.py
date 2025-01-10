import socket as sc
import re, base64, zlib

def base64Decode(code: str) -> bytes:
  """Décode un message encodé avec base64"""
  return base64.b64decode(code)

def decompressZlib(data: bytes) -> bytes:
  """
  Décompresse le message zippé avec Zlib
  """
  return zlib.decompress(data)

def decode_message(encoded_message: str) -> str:
  """Décoder un message encodé"""
  try:
    # Décodage avec base64
    decoded_bytes = base64Decode(encoded_message)

    # Décompression avec Zlib
    decompressed_bytes = decompressZlib(decoded_bytes)

    # Conversion en chaîne de caractères
    return decompressed_bytes.decode("utf-8")
  except Exception as e:
    print(f"Erreur lors du décodage : {e}")
    return None

def main(host: str, port: int) -> None:
  """
  La fonction principale qui communique avec le server
  """
  try:
    with sc.socket(sc.AF_INET, sc.SOCK_STREAM) as client_socket:
      print(f"Connexion à {host}:{port}...")
      client_socket.connect((host, port))
      print("Connecté avec succès !\n")

      while True:
        # Réception du message du serveur
        data = client_socket.recv(1024).decode('utf-8').strip()
        if not data:
          print("Aucune donnée reçue, fermeture de la connexion.")
          break

        print(f"Reçu du serveur :\n{data}")

        # Extraction de la chaîne encodée
        extracted = re.findall(r"'(.*?)'", data)
        if not extracted:
          print("Aucune chaîne encodée trouvée dans le message.")
          break

        encoded_string = extracted[0]
        print(f"Chaîne encodée : {encoded_string}")

        # Décodage et décompression
        decoded_message = decode_message(encoded_string)
        print(f"Chaîne décodée : {decoded_message}")

        # Envoi de la chaîne décodée
        client_socket.sendall(f"{decoded_message}\n".encode('utf-8'))
        print("\n-------------------------------------------------\n")

  except Exception as e:
    print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
  host = "challenge01.root-me.org"
  port = 52022
  main(host, port)
