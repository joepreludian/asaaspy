# Contribuindo para o projeto
Primeiramente, obrigado pelo interesse em ajudar a manter esse projeto cada vez melhor!

Este guia visa justamente pontuar alguns detalhes acerca da forma como será desenvolvido os trabalhos, como reproduzir o projeto localmente, executar testes, escrever documentação entre outros.

## Como Ajudar?
Esse tópico é bem aberto. Há diversas formas de você ajudar o desenvolvimento desse projeto! Abaixo há algumas opções:

* **Utilizando o projeto** -> Forma mais simples e padrão para todos os desenvolvedores. Caso haja algum problema, poderá logar bugs e issues no próprio repositório.
* **Favoritando no github** -> Seria uma forma de demonstrar suporte ao nosso projeto. Isso também dá um calorzinho no coração do time de desenvolvimento. =D
* **Contribuindo com código** -> Seria uma outra forma bastante desejável, uma vez que esse projeto está sendo fruto de apenas um desenvolvedor, por ora, que quer contribuir bastante para a comunidade, entregando um software de qualidade.
* **[Pagando-me um cafezinho](/para_desenvolvedores/pague-me_um_cafezinho)** -> Contribuições financeiras são sempre muito bem vindas! Qualquer valor seria muito bom. Sou uma máquina de processar café, logo sua contribuição certamente virará algumas muitas doses de espresso. =D

## Requisitos para desenvolver a biblioteca
Para o desenvolvimento da solução se faz necessário ter os seguintes recursos.

* Python 3.10 instalado na máquina. Recomendo fortemente utilizar [https://github.com/pyenv/pyenv](Pyenv) para o gerenciamento das versões Python na sua máquina;
* PIPX - para poder instalar bibliotecas de suporte.
* PDM - Gerenciador de dependencias com suporte à metadados seguindo a [https://www.python.org/dev/peps/pep-0621](PEP-621). [https://github.com/pdm-project/pdm]()
    * Recomenda-se instalar o PDM usando o pipx

## Instalando dependências
Uma vez com o projeto clonado, instale as dependências tanto de teste quanto de documentação.

```bash
$ pdm install --group dev --group docs
```

### Visualizando essa documentação localmente
Para poder trabalhar nessa documentação localmente, basta executar o seguinte comando abaixo:

```bash
$ pdm run mkdocs serve
```

### Executando testes
Para os testes, estou utilizando `pytest` como biblioteca para tanto os testes unitários quanto de integração.
Também estou utilizando uma excelente biblioteca para a captura de requisições chamada [VCRPy](http://vcrpy.readthedocs.io)

Inicialmente você precisará de uma conta sandbox para poder trabalhar dentro do projeto. Veja mais informações aqui: [](http://sandbox.asaas.com).

Uma vez com o token de API para sandbox, copie o arquivo `.env.sample` para `.env` adicionando sua chave de API lá. Com isso você conseguirá executar todos os testes.

```bash
$ pdm run pytest
```
