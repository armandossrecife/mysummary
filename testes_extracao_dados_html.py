# -*- coding: utf-8 -*-
"""testes_extracao_dados_html.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y51ZkvgyFT8Bya_kvPZJYMNMdhvC9c_l

# Usando o Beautifulsoup

https://beautiful-soup-4.readthedocs.io/en/latest/

https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)

Parse tree

O processo de web scraping

## Instalando o Beautifulsoap
"""

!pip install beautifulsoup4

"""## Recuperando informações com o Beautifulsoap"""

from bs4 import BeautifulSoup
import requests

# Fetch the HTML content of the webpage
MY_URL = "https://en.wikipedia.org/wiki/Linux"
html_content = ""

try:
  response = requests.get(MY_URL)
  response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

  if response.status_code == 200:
      print("Requisição bem sucedida!")
      html_content = response.content
  else:
      print("Requisição falhou com o código de status:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error fetching the webpage:", e)

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# <div id="mw-content-text"
body_content_div = soup.find('div', id="mw-content-text")

# Extract the text content
if body_content_div:
    content = body_content_div.get_text(strip=True)
    fragmento = content[:1000]
    print(fragmento)
else:
    print("Div with id 'bodyContent' not found.")

"""## Recuperando os dados de um protocolo"""

class DocumentoProcesso:
  def __init__(self, tipo, data, origem, natureza, link):
    self.tipo = tipo
    self.data = data
    self.origem = origem
    self.natureza = natureza
    self.link = link

  def __str__(self):
    return f"Tipo: {self.tipo}, Data: {self.data}, Origem: {self.origem}, Natureza: {self.natureza}, Link: {self.link}"

class MovimentacaoProcesso:
  def __init__(self, data_origem, unidade_origem, unidade_destino, enviado_por, recebido_em, recebido_por):
    self.data_origem = data_origem
    self.unidade_origem = unidade_origem
    self.unidade_destino = unidade_destino
    self.enviado_por = enviado_por
    self.recebido_em = recebido_em
    self.recebido_por = recebido_por

  def __str__(self):
    return f"Data Origem: {self.data_origem}, unidade origem: {self.unidade_origem}, unidade destino: {self.unidade_destino}, enviado por: {self.enviado_por}, recebido em: {self.recebido_em}, recebido por: {self.recebido_por}"

def get_html_content(url):
  html_content = ""
  try:
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

    if response.status_code == 200:
        print("Requisição bem sucedida!")
        html_content = response.content
    else:
        raise ValueError("Requisição falhou com o código de status:", response.status_code)
    return html_content
  except requests.exceptions.RequestException as e:
      raise ValueError("Error fetching the webpage:", e)

URL_PROTOCOLO = "https://www.sipac.ufpi.br/public/jsp/processos/processo_detalhado.jsf?id=594067"

html_protocolo = get_html_content(URL_PROTOCOLO)

# Parse the HTML content
soup = BeautifulSoup(html_protocolo, 'html.parser')

# Recupera os dados das tabelas do site

table_dados = soup.find_all('table', class_='subListagem')
table_dados_interessado = table_dados[0]
table_dados_documentos = table_dados[1]
table_dados_movimentacoes = table_dados[2]

# Recupera dados do interessado do processo
for row in table_dados_interessado.find_all('tr'):
    data_cells = row.find_all('td', recursive=False)
    for cell in data_cells:
        print(cell.text.strip())

# Recupera os dados basicos do processo
# Find the outer table
table_dados_basicos = soup.find('table', class_='formulario', style="width: 100%;")

# Extract data from each row
for i, row in enumerate(table_dados_basicos.find_all('tr')):
    data_cells = row.find_all('td', recursive=False)
    if i < 10:
      for cell in data_cells:
          print(cell.text.strip())

# Recupera os documentos do processo

lista_documentos = []
for row in table_dados_documentos.find_all('tr'):
    data_cells = row.find_all('td', recursive=False)
    my_link = ''
    lista_links = []
    for i, cell in enumerate(data_cells):
        if i == 0:
          tipo = cell.text.strip()
        elif i == 1:
          data = cell.text.strip()
        elif i == 2:
          origem = cell.text.strip()
        elif i == 3:
          natureza = cell.text.strip()
        if cell.find_all('a'):
          for link in cell.find_all('a'):
            lista_links.append(link['href'])
          my_link = lista_links[0]
        documento = DocumentoProcesso(tipo, data, origem, natureza, my_link)
    lista_documentos.append(documento)

for each in lista_documentos:
  print(each)

# Recupera as movimentacoes do processo

lista_movimentacoes = []
for row in table_dados_movimentacoes.find_all('tr'):
    data_cells = row.find_all('td', recursive=False)
    for i, cell in enumerate(data_cells):
      if i == 0:
        data_origem = cell.text.strip()
      elif i == 1:
        unidade_origem = cell.text.strip()
      elif i == 2:
        unidade_destino = cell.text.strip()
      elif i == 3:
        enviado_por = cell.text.strip()
      elif i == 4:
        recebido_em = cell.text.strip()
      elif i == 5:
        recebido_por = cell.text.strip()
      movimentacao = MovimentacaoProcesso(data_origem, unidade_origem, unidade_destino, enviado_por, recebido_em, recebido_por)
    lista_movimentacoes.append(movimentacao)

for movimentacao in lista_movimentacoes:
  print(movimentacao)
  print('--')

"""# Código Refatorado e Simplificado"""

def extract_data_from_table(table, headers):
    """Extrai dados de uma tabela HTML e retorna uma lista de dicionários."""
    data = []
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if cells:  # Verifica se a linha contém dados
            row_data = dict(zip(headers, [cell.text.strip() for cell in cells]))
            data.append(row_data)
    return data

# Exemplo de uso:
table_dados = soup.find_all('table', class_='subListagem')
table_dados_interessado = table_dados[0]
table_dados_documentos = table_dados[1]
table_dados_movimentacoes = table_dados[2]

headers = ['Tipo', 'Identificador', 'Nome']
interessado_data = extract_data_from_table(table_dados_interessado, headers)

for pessoa in interessado_data:
    print(pessoa)

headers_documento = ['Tipo do Documento', 'Data do Documento', 'Origem', 'Natureza']
documentos = extract_data_from_table(table_dados_documentos, headers_documento)

for documento in documentos:
    print(documento)

headers_movimentacao =  ['Data Origem', 'Unidade Origem', 'Unidade Destino',	'Enviado Por',	'Recebido Em',	'Recebido Por']
movimentacoes = extract_data_from_table(table_dados_movimentacoes, headers_movimentacao)

for movimentacao in movimentacoes:
    print(movimentacao)
