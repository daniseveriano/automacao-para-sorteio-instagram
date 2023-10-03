# Automação para Sorteios no Instagram, em Python

Para utilização deste projeto, é necessário baixar/instalar as seguintes ferramentas e pacotes:

- ChromeDriver, na versão compatível com o seu navegador do Chrome (coloque o arquivo `chromedriver.exe` dentro da pasta deste projeto)
- Python
- Pacote do Selenium compatível com sua versão do Python
- Pacote do Schedule compatível com sua versão do Python

## Arquivo config.json

Renomeie o arquivo `exemplo.config.json` para `config.json`, e inclua as seguintes informações:
- Login do Instagram
- Senha do Instagram
- Postagem do Sorteio que deseja participar
- Texto do comentário

## Arquivo agendador.py

Ajuste o tempo do agendador na linha `schedule.every(30).minutes.do(executar_meu_script)`.
No exemplo, o tempo de intervalo de execução é de 30 minutos. Para colocar 1 hora, por exemplo, digite no lugar de `every(30).minutes` o texto `every(1).hours`.

## Rodando o script
Estando tudo configurado, acesse a pasta do projeto pelo seu terminal, e digite `python agendador.py` para inicializar o seu script.
Este script está configurado para abrir uma aba do seu navegador Chrome, a cada intervalo de tempo configurado no arquivo `agendador.py`.