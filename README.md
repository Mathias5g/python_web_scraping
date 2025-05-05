# Web Scraper - Mercado Livre

Este projeto é um web scraper desenvolvido em Python para buscar informações de produtos no site Mercado Livre. Ele utiliza as bibliotecas `requests`, `BeautifulSoup`, e `truststore` para realizar requisições HTTP, processar o HTML da página e gerenciar certificados SSL.

## Funcionalidades

- Busca produtos no Mercado Livre com base em uma palavra-chave fornecida pelo usuário.
- Extrai informações como:
  - Título do produto
  - Link do produto
  - Preço do produto
  - Categoria do produto
- Exibe uma barra de progresso durante a execução.
- Salva os resultados em um arquivo JSON com o nome da categoria buscada.

## Estrutura do Projeto
├── req_bs4.py # Script principal do scraper 

## Requisitos

- Python 3.10 ou superior
- Dependências listadas no arquivo `requirements.txt`

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/Mathias5g/python_web_scraping.git
cd python_web_scraping
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso
1. Execute o script req_bs4.py
```bash
python req_bs4.py
```
2. Insira o nome do produto que deseja buscar quando solicitado.
3. O script exibirá uma barra de progresso e salvará os resultados em um arquivo JSON com o nome da categoria buscada.

## Exemplo de Saída
```json
[
    {
        "Titulo do produto": "Sapato Social Masculino",
        "Link do produto": "https://produto.mercadolivre.com.br/...",
        "Preço do produto": "99.90",
        "categoria": "sapato"
    },
    ...
]
```

## Dependências
- requests
- beautifulsoup4
- colorama
- truststore

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.