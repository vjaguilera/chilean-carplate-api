---
title: Chilean Plates FastAPI
description: A FastAPI server to retrieve chilean car plates data
tags:
  - fastapi
  - python
  - chile
  - cars
---

# Chilean Plates FastAPI in Railway

This example starts up a [FastAPI](https://fastapi.tiangolo.com/) server.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/-NvLj4?referralCode=milo)


## 💁‍♀️ How to deploy

- Deploy using the button 👆
- Clone locally and install packages with Pip using `pip install -r requirements.txt` or Poetry using `poetry install`
- Connect to your project using `railway link`
- Run locally using `uvicorn main:app --reload`

## 📝 DEtails
- Utilizando una query cURL muy especifica, se puede obtener los datos de las patentes chilenas.

## Running Local
Para correr el programa se debe:

1. Instalar Python >3.8
2. Crear un ambiente virtual con `python -m venv venv`
2. Activar el ambiente virtual con el comando `source venv/bin/activate`
3. Instalar paquetes con el comando `pip install -r requirements.txt`
4. Correr el comando `python main.py`

Consideraciones:

- Se creará un archivo `response.html` con el codigo HTML del sitio web scrapeado


Para correr el proyecto como API

1. Asegurar instalacion de paquetes *fastapi* y *uvicorn[standard]*
2. Abrir terminal y correr el comando `uvicorn main:app --reload`
3. Abrir el puerto que aparece

## Recommended
- Abrir el siguiente url para ver documentacion: `http://127.0.0.1:8000/docs`, el path `docs` lleva directamente a una documentacion en OpenAPI