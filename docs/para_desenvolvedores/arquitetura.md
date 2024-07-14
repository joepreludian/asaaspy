# Arquitetura do projeto

Esse parte da documentação é interessante mais caso tenha interesse em contribuir para o desenvolvimento dessa biblioteca. Obrigado pelo interesse antemão e seja bem vindo!

O projeto do AsaasPy possui uma arquitetura separada em camadas de modo a garantir um isolamento de responsabilidades. Pode parecer um pouco complexo em uma leitura fria, mas a longo prazo ele se tornará bastante útil e previsível.

## Estrutura
O projeto do AsaasPy está estruturado, de maneira geral, conforme o gráfico abaixo:

``` mermaid
flowchart TD
    AsaasPY(AsaasPy)
    Service(AsaasService)
    Schemas(Schemas)
    AsaasClient
    AsaasResource

    AsaasClientHTTPX(HTTPX Handler)
    AsaasClientHeaders(Client low level Headers)

    AsaasSchemasPerResource(Per Resource Schemas)

    AsaasSchemaView(ViewSchema)
    AsaasSchemaCreate(CreateSchema)
    AsaasSchemaPaginatedOutputPayload(PaginatedOutputPayload)

    AsaasResourceCustomer(Customer)
    AsaasResourcePayment(Payment)

    AsaasPY --> Service
    AsaasPY --> Schemas
    Service --> AsaasClient
    Service --> AsaasResource
 
    AsaasResource --> AsaasResourceCustomer
    AsaasResource --> AsaasResourcePayment

    AsaasClient --> AsaasClientHTTPX
    AsaasClient --> AsaasClientHeaders

    Schemas --> AsaasSchemasPerResource
    Schemas --> AsaasSchemaPaginatedOutputPayload
    AsaasSchemasPerResource --> AsaasSchemaCreate
    AsaasSchemasPerResource --> AsaasSchemaView

```

### Entendendo as estruturas
As camadas ficam distribuidas da seguinte maneira. Tentarei separar por níveis de camada

* **AsaasService** -> Serviço Principal onde será feita a comunicação entre o cliente e o projeto do Asaas.
* **Schemas** -> Possui os DTOs (Data Transfer Objects) utilizados para visualização dos dados.
 
#### Schemas
Os Schemas são Dataclasses do python que representam os dados trafegados no app das seguintes maneiras:

* **Schemas de Criação** -> São payloads que podemos injetar dentro dos recursos. Por exemplo **CustomerCreateSchema** possui um DataClass que pode ser utilizado para a criação de um novo *Customer* dentro do *AsaasService*.
    * Eles conterão dados minimos e opcionais conforme declarados na documentação oficial da API.
* **Schemas de Visualização** -> Estes são utilizados para representar um dado que veio da API. Geralmente possui mais campos. Por exemplo, ao Criar um novo *Customer* o método retornará um objeto do tipo *CustomerViewSchema*, onde trará o campo `id`, entre outros.
* **PaginatedOutputPayload** -> Esta estrutura é a representação do retorno de um payload que vem da API, quando o resultado é paginado. Tentei seguir o padrão a ser utilizado de modo a manter uma camada de compatibilidade com o retorno atual, apenas tornando o retorno previsível por meio de dataclasses.

#### AsaasService
Este é o coração do projeto a ser oferecido. Ele encapsula o `Client` e os `Resources` dentro de si. É por meio dele que voce acessa os recursos na qual as peças são encaixadas.

* **Client** -> Seria o cliente de conexão com a API do Asaas. Ele possui a implementação mais baixo nível, onde há o esquema de configuração dos headers, etc. Também possui um método onde ele instancia o `Cliente HTTP` que fará as chamadas para o servidor WEB.
    * Neste caso específico, utilizei a implementação do HTTPX para tentar algo diferente à já consolidada `requests`.
* **Resource** -> Seria justamente uma implementação especial do serviço especializada no recurso que estamos querendo utilizar. Eu me inspirei no conceito de Resource do próprio design [https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api](REST)
    * Por exemplo, `CustomerResource` será uma classe Python que possuirá os métodos `all`, `create`, `delete`.

## Ajude-me a melhorar esse documento

Você poderá me ajudar a complementar essa documentação ao contribuir no projeto.