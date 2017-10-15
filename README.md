# Web Python Pereira

[![Join the chat at https://gitter.im/python-pereira/Lobby](https://badges.gitter.im/python-pereira/Lobby.svg)](https://gitter.im/python-pereira/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## Requerimientos

* Python >= 3.5

### Virtualenv

#### Instalación

```bash
apt install python-virtualenv
```

#### Crear Ambiente

```bash
virtualenv -p python3 env
```

## Deploy

```bash
cd web/
python freeze.py
```

### Virtualenv

```bash
env/bin/python web/freeze.py
```

## Run

```bash
cd web/
python run.py
```

### Virtualenv

```bash
env/bin/python web/run.py
```

* La aplicación se ejecutará sobre localhost:5000

## Test deploy

```bash
env/bin/python -m http.server <port>
```

## Referencias

### Plantilla de Bootstrap

Copyright 2013-2017 Blackrock Digital LLC. Code released under the [MIT](https://github.com/BlackrockDigital/startbootstrap-creative/blob/gh-pages/LICENSE) license.
