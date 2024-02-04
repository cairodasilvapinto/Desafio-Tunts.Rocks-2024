# Desafio-Tunts.Rocks-2024
PROCESSO SELETIVO – DESAFIO DE PROGRAMAÇÃO – NÍVEL 1

# Student Grade Management

## Descrição

Este projeto é um script Python que interage com o Google Sheets para gerenciar as notas dos alunos de um curso. Ele lê os dados dos alunos de uma planilha, calcula a situação de cada aluno com base em suas faltas e média de notas, e então escreve os resultados de volta na planilha.

## Pré-requisitos

Para executar este script, você precisará:

- Python 3.6 ou superior
- Uma conta do Google com acesso ao Google Sheets
- As bibliotecas `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, `gspread` e `oauth2client` instaladas. Você pode instalar todas elas com o seguinte comando:

```bash
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 gspread oauth2client
```

# Configuração

1. Clone este repositório para o seu computador local.
2. Crie um projeto no Google Cloud Console.
3. Ative a API do Google Sheets para o seu projeto.
4. Crie credenciais OAuth2 e baixe o arquivo JSON das credenciais.
5. Renomeie o arquivo de credenciais para client_secret.json e mova-o para a pasta do projeto.
6. Compartilhe a planilha do Google Sheets com a conta de serviço criada quando você gerou as credenciais (o e-mail da conta de serviço pode ser encontrado no arquivo client_secret.json).
   
    **https://developers.google.com/sheets/api/quickstart/python?hl=pt-br**

## Uso

Para executar o script, navegue até a pasta do projeto no terminal e execute o seguinte comando:

```bash
python main.py
```

O script irá ler os dados dos alunos da planilha, calcular a situação de cada aluno e então escrever os resultados de volta na planilha.

## Contribuição

Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de enviar uma pull request.