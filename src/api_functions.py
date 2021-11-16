import json
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
import time
from functools import reduce
import operator

def type_point(lista):
    return {"type":"Point", "coordinates": lista}

def geocode(direccion):
    """
    Esta función saca las coordenadas de la dirección que le pases
    """
    #print(f"     Consultando lat+long a geocode.xyz de {direccion}")
    data = requests.get(f"https://geocode.xyz/{direccion}?json=1").json()
    try:
        return {"type": "Point", "coordinates": [float(data["latt"]), float(data["longt"])]}
    except:
        return data['error']['code']
       
def corregir_lat_long(row) :
    direccion_a_buscar = f"{row['address1']} , {row['city']}"
    if row['latitude'] == None or row["longitude"] == None  :
        print(f"     Latitud o Longitud es none. Llamamos a geocode con la direccion.")
        while row['latitude'] == None or row["longitude"] == None  :
            row["punto"]  = geocode(direccion_a_buscar)
            if row["punto"] == "018" :
                print(f"          Geocode ({direccion_a_buscar}) no se encuentra. Intentamos sólo con la ciudad.")
                direccion_a_buscar = row['city']
            elif row["punto"] == "006" :
                print(f"          Geocode ({direccion_a_buscar}) --> Max request, esperamos y repetimos")
            else : 
                row["latitude"]   = row["punto"]['coordinates'][0]
                row["longitude"]  = row["punto"]['coordinates'][1]
        print(f"Latitud : {row['latitude']} , Longitud: {row['longitude']} CORREGIDOS.")
        row['punto'] = {"type": "Point", "coordinates": [ row["latitude"] , row["longitude"] ]}
    else :
        print(f"Latitud : {row['latitude']} , Longitud: {row['longitude']} correctos.")
    return row['punto']

def sacar_lat(row):
    return row['punto']['coordinates'][0]
def sacar_long(row):
    return row['punto']['coordinates'][1]

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)

def extraetodo(json):
    total = []
    for elemento in json:
        elemento_nuevo = {}
        elemento_nuevo["name"]      = elemento["name"]
        elemento_nuevo["latitude"]  = elemento["location"]["lat"]
        elemento_nuevo["longitude"] = elemento["location"]["lng"]
        elemento_nuevo["location"]  = type_point([elemento_nuevo["latitude"], elemento_nuevo["longitude"]])
        try: 
            elemento_nuevo["type"]  = elemento["categories"][0]["shortName"]
        except IndexError:
            elemento_nuevo["type"]  = ""
        total.append(elemento_nuevo)
    return total