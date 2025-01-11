import requests
import base64
import re
import subprocess
from PIL import Image

# Installé gocr sous linux avant de lancer le script
# sudo apt-get update
# sudo apt-get install gocr -y
# gocr à une marge d'erreur de 7 à 8%, donc il faut executer le script plusieurs fois 
def deleteNoise(filename : str) -> None :
  """
  Delete all the noise from the image 
  """
  img = Image.open(filename) 
  width, height = img.size
  pix = img.load()
  for i in range(width):
    for j in range(height):
      if pix[i, j] == (0, 0, 0):
        pix[i, j] = (255, 255, 255)
  img.save(filename)

def main(url: str, filename: str) -> str :
  # Étape 1 : Récupérer la page
  r = requests.get(url)
  resp = r.text  
  cookies = r.cookies 
  # Étape 2 : Extraire l'image CAPTCHA encodée en Base64
  express = r'data:image/png;base64,(.*)" /><br><br>'
  res = re.search(express, resp)  

  # Décoder l'image en Base64
  res = res.group(1)
  captcha_image = base64.b64decode(res)  

  # Sauvegarder l'image CAPTCHA dans un fichier
  with open(filename, 'wb') as fil:
    fil.write(captcha_image)

  # Nettoyer l'image
  deleteNoise(filename)

  # Étape 3 : Utiliser `gocr` pour traiter l'image et extraire le texte
  res = subprocess.run(f"gocr -i {filename}", stdout=subprocess.PIPE, shell=True).stdout

  # Nettoyer la sortie OCR
  res = res.decode('utf-8').strip().replace("\n", "").replace("\r", "").replace(" ", "").replace(",", "").replace("_", "")

  # Étape 4 : Soumettre la solution
  value = {'cametu': res}
  rex = requests.post(url, cookies=cookies, data=value)

  # Afficher la réponse
  print(rex.text)

if __name__ == "__main__":
  # URL du challenge
  url = "http://challenge01.root-me.org/programmation/ch8/"
  filename = "captcha.png"
  main(url, filename)