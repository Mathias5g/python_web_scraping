import time
import colorama
import requests as r
from bs4 import BeautifulSoup
import json
import truststore
truststore.inject_into_ssl()

produto_selecionado = str(input('Qual produto você deseja buscar?\n'))

def progress_bar(progress, total, color=colorama.Fore.YELLOW):
  percent = 100 * (progress / float(total))
  bar = '█' * int(percent) + '░' * (100 - int(percent))
  print(color + f'\rProgress: |{bar}| {percent:.2f}% complete', end='\r')
  if progress == total:
    print(colorama.Fore.GREEN + f'\rProgress: |{bar}| {percent:.2f}% complete', end='\r')

if produto_selecionado:
  prod = []
  print(f'Buscando: {produto_selecionado}...', end='\n')
  response = r.get(f'https://lista.mercadolivre.com.br/{produto_selecionado}')
  site = BeautifulSoup(response.text, 'html.parser')
  produtos = site.find_all('div', attrs={'class': 'andes-card poly-card poly-card--grid-card poly-card--large poly-card--CORE andes-card--flat andes-card--padding-0 andes-card--animated'})

  for i, p in enumerate(produtos):
    titulo = p.find('h3', attrs={'class': 'poly-component__title-wrapper'})
    link = p.find('a', attrs={'class': 'poly-component__title'})
    real = p.find('span', attrs={'class': 'andes-money-amount__fraction'})
    centavos = p.find('span', attrs={'class': 'andes-money-amount__cents'})

    preco = ''
    if centavos:
      preco = f'{real.text}.{centavos.text}'
    else:
      preco = real.text

    prod.append({'Titulo do produto': titulo.text, 'Link do produto': link['href'], 'Preço do produto': preco, 'categoria': produto_selecionado})
    time.sleep(0.05)
    progress_bar(i+1, len(produtos))

  with open(f'{produto_selecionado}.json', 'w') as f:
    f.write(json.dumps(prod, indent=4))

  print(colorama.Fore.RESET)
  print(f'🏁 Busca concluida e salva no arquivo `{produto_selecionado}.json` 🏁')
else:
  print('Você não definiu nenhum produto, processo encerrado!')

  