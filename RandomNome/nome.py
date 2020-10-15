import requests

texto = requests.get("https://www.wjr.eti.br/nameGenerator/index.php?q=1&o=plain").content
print texto
