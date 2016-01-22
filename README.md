# Eventex

Sistema de eventos encomendado pela Morena

[![Build Status](https://travis-ci.org/henemer/eventex.svg?branch=master)](https://travis-ci.org/henemer/eventex)
[![Code Climate](https://codeclimate.com/repos/56a274e912baf76a6d005aab/badges/f0d48b79174227a73cee/gpa.svg)](https://codeclimate.com/repos/56a274e912baf76a6d005aab/feed)

## Como desenvolver ?

1. Clone o repositório
2. Crie o virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências
5. Configure a instância com .env
6. Execute os testes

```console
git clone git@github.com:henemer/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy ?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=false
5. Configure o serviço de email
6. Emnvie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG_FALSE
# configuro o email
git push heroku master --force
```

