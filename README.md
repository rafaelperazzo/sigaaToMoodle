# sigaaToMoodle
**uma ferramenta para geração de uma lista de usuários para o moodle, a partir da lista de participantes do SIGAA**
## Requisitos

* [Docker](https://docs.docker.com/get-docker/)
* [Docker-compose](https://docs.docker.com/compose/install/)

## Entrada

* HTML dos participantes de um curso do SIGAA
* configuração do arquivo arquivos/config.ini (exemplo):

```
    [DEFAULT]
    curso = CODIGODOCURSO
    grupo = GRUPODATURMA
    csv = output/export.csv
    arquivo = input/input.html
```
## Saída

* arquivo CSV no formato para importação no moodle
## Como executar
Executar o comando dentro da pasta do projeto
```
docker-compose run --rm sigaa2moodle
```

## TODO
