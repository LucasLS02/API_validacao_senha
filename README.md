# API Validação de Senha

Essa é uma REST API para validação de senha senhas seguindo os parâmetros enviados pelo usuário.

Essa aplicação foi desenvolvida utilizando-se de containers ([Docker](https://www.docker.com/)) e orquestrado através do [Docker Compose](https://docs.docker.com/compose/gettingstarted/). Para o funcionamento desse sistema seguindo a ideia de uma REST API, foi utilizado a linguagem [Python](https://www.python.org/), principalmente através do micro framework [Flask](https://flask.palletsprojects.com/en/2.2.x/) para criar uma aplicação de REST API.

## Instalação

Para que a API possa ser executada propriamente é necessário que voce instale as seguintes dependências.

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/gettingstarted/)
- [Python](https://www.python.org/)
- [Package Installer for Python (pip)](https://pip.pypa.io/en/stable/installation/)

## Rodar a aplicação

Quando for rodar a aplicação existem 2 maneiras de executar os containers:

- [ ] Iniciar o container, forçando com que a imagem e a instalação dos pacotes seja executada
  - `make install-and-run`
- [ ] Iniciar o container normalmente
  - `make run`

**É importante ressaltar que o Makefile utilizado para rodar os containers acima só consegue ser usado nos sistemas operacionais baseados em Unix, portanto, para rodar a aplicação acima em windows deve-se usar o comandos `docker-compose -f docker-compose.yaml up --build --force-recreate` e `docker-compose -f docker-compose.yaml up` .**

# REST API

Nessa API voce encontrará os seguintes endpoints para validação da senha:

## verify_password

### Request

`POST http://localhost:8080/verify`

    {
     "password":  "password",
     "rules":  [
      {
       "rule":  "rule",
       "value":  0
      }
     ]
    }

### Response

200

    {
     "data":  {
      "noMatch":  [],
      "verify":  true,
     }
    }

422

    {
      "error": {
        "password": [
          "Not a valid string."
        ],
        "rules": {
          "0": {
            "rule": [
              "Must be one of: minSize, minUppercase, minLowercase, minDigit, minSpecialChars, noRepeted."
            ],
            "value": [
              "Must be greater than or equal to 0."
            ]
          }
        }
      }
    }

500

    {
     "error":  "Internal Server Error"
    }

## ✒️ Autor

- [@LucasLS02](https://github.com/LucasLS02)
