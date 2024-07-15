# Bem vindo!

Esta é uma Biblioteca python não oficial de abstração dos endpoints do Asaas. [https://www.asaas.com/]()

## AVISO - Projeto em Desenvolvimento
Esta biblioteca não faz parte do time de desenvolvimento do Asaas e também não possui garantia. Apesar de estar usando boas práticas de desenvolvimento, sua utilização em ambiente de produção requer cuidado.

Como se trata de um projeto em alpha, a API utilizada poderá sofrer modificações.

**Use por sua conta e risco**

## Motivação

Este projeto utiliza as seguintes tecnologias:

* Python 3.10+
* Pydantic 2
* HTTPX - [https://www.python-httpx.org]()

E foi pensado baseado nos seguintes pontos:

* Possuir uma arquitetura simples e funcional
* Poder ter na camada de serviço formas de encapsular diferentes contratos da API
* As estruturas de dados (DTO) serem previsiveis por meio de Pydantic Models
* Possuir uma biblioteca que possa ser mantida pela comunidade

Ao se utilizar uma chamada com um retorno previsível, por meio de TypedHints, o desenvolvimento acaba se tornando mais agradável para o desenvolvedor que poderá contar com a ajuda da sua IDE.

Também foi pensado uma estrutura de encapsulamento da solução de modo que ela possa ser plugável por meio de Recursos. (Como a API é versionada, poder utilizar um contrato anterior, ou suportar diferentes contratos dentro da mesma API)

Para mais informações, confira a [arquitetura do projeto](/para_desenvolvedores/arquitetura)

## Roadmap

Pra essa primeira versão do projeto, eu tenho a seguinte missão:

* Cadastrar, Listar, Buscar e Apagar Clientes;
* Criar, Listar, Buscar e Apagar Cobranças;
* Automatizar o processo de deployment dessa biblioteca;
* Criar um arquivo de documentação em inglês.

A ideia seria expandir para todas as funcionalidades do APP.

Também voce pode contribuir com o desenvolvimento do projeto. Saiba mais aqui.

## Gostou do projeto?

Você pode apoiar o trabalho favoritando esse projeto, contribuindo com código ou me pagando um cafezinho. :)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="joepreludian" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Pague-me um cafezinho :)" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
