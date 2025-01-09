import requests
import re

def extraction_info(text: str) -> tuple[int,int,str]:
  """
  Extrait les informations nécessaires depuis la réponse du serveur.
  """
  num_exp = r"(\-?\d+)"
  sign_exp = r"([\-\+])"
  # Extraction de U0
  u0 = int(re.search(rf"U<sub>0</sub> = {num_exp}", text).group(1))
  # Extraction de n
  n = int(re.search(r"You must find U<sub>(\d+)</sub>", text).group(1))
  # Extraction de la formule de récurrence
  u = re.search(rf"U<sub>n\+1</sub> = \[ {num_exp} \+ U<sub>n</sub> \] {sign_exp} \[ n \* {num_exp} \]", text)
  # Conversion de la formule en une chaîne Python
  u_expr = f"{u.group(1)}*n {u.group(2)} {u.group(3)}*(n-1)*n/2 + u0"
  return u0, n, u_expr

def calculate_u(u0: int, n: int, expr: str) -> int:
  """
  Calcule la valeur de U_n rapidement en simulant la récurrence.
  """
  return eval(expr, {"n": n, "u0": u0})

def solution(url: str, response_url: str) -> None:
  """
  Résout le problème en deux étapes : extraction et soumission du résultat.
  """
  # Étape 1 : Récupérer les données initiales
  response = requests.get(url)
  if response.status_code != 200:
    raise ValueError(f"Failed to fetch data: {response.status_code}")
  
  # Gestion des cookies
  cookies = response.cookies
  text = response.text
  print(text)
  # Extraction des informations
  u0, n, expr = extraction_info(text)
  print(f"n = {n}\nU0 = {u0} \nU = {expr}")
  # Étape 2 : Calcul rapide de U_n
  result = int(calculate_u(u0, n, expr))
  print(result)
  # Étape 3 : Envoi de la réponse au serveur
  final_response = requests.get(f"{response_url}{result}", cookies=cookies)
  print(final_response.text)

if __name__ == "__main__":
  url = "http://challenge01.root-me.org/programmation/ch1/"
  response_url = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="
  solution(url, response_url)