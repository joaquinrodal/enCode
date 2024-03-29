#---------------------------------------------------------
# SERVIDOR 
#---------------------------------------------------------

from fastapi import FastAPI

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(  title='enCode',
                description='Aplicacion Profesional', 
                version='1.0',
                contact={
                    "name": "JOAQUIN RODAL CHORRO",
                    "url": "http://joaquinrodalchorro.com",
                    "email": "informatico.joaquin@gmail.com",
                })

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
plantilla = Jinja2Templates(directory="plantillas")

from rutas import *
