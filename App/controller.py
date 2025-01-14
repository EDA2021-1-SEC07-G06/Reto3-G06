﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from App.model import crearGeneros
import time
import tracemalloc

import config as cf
from DISClib.ADT import list as lt
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del analizador

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadData(analyzer):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """

    crearGeneros(analyzer)
    loadEtiquetas(analyzer)
    loadSenValues(analyzer)
    eventos = loadEventos(analyzer)

    

    return eventos, delta_time, delta_memory   
    
    

def loadEventos(analyzer):
    """
    Carga los videos del archivo.
    """
    eventosfile = cf.data_dir + 'context_content_features-small.csv'
    input_file = csv.DictReader(open(eventosfile, encoding='utf-8'))
    contador = 0
    tamaño = 0
    listaInicial = lt.newList('ARRAY_LIST')
    listaFinal = lt.newList('ARRAY_LIST')

    fichero = open(eventosfile, encoding='utf-8')
    tamaño = len(fichero.readlines())
    
    
    for evento in input_file:
        if contador <= 4:
            lt.addLast(listaInicial,evento)
            
        elif contador >= (tamaño - 6):
            lt.addLast(listaFinal,evento)

        model.addEvento(analyzer, evento)
        contador += 1

   
    
    return listaInicial, listaFinal


def loadEtiquetas(analyzer):
    """
    Carga los videos del archivo.
    """
    etiquetasfile = cf.data_dir + 'user_track_hashtag_timestamp-small.csv'
    input_file = csv.DictReader(open(etiquetasfile, encoding='utf-8'))
    for etiqueta in input_file:
        model.addEtiquetas(analyzer, etiqueta)
       

def loadSenValues(analyzer):
    """
    Carga los videos del archivo.
    """
    valuesfile = cf.data_dir + 'sentiment_values.csv'
    input_file = csv.DictReader(open(valuesfile, encoding='utf-8'))
    for value in input_file:
        model.addSentimentalValue(analyzer, value)
      
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
    """
    Retorna el numero de artistas sin repetir.
    """
def tamañoArtistas(analyzer):
    return model.artistasSize(analyzer)
    
    """
    Retorna el numero de eventos.
    """
def tamañoEventos(analyzer):
    return model.eventosSize(analyzer)

    """
    Retorna el numero de artistas sin repetir.
    """
def tamañoPistas(analyzer):
    return model.pistasSize(analyzer)

def getReproducciones(analyzer, contenido, min, max):
    """
    Retorna el total de reproducciones (eventos de escucha) que se tienen en el sistema de
    recomendación basado en una característica de contenido y con un rango determinado
    """
    rep = model.getReproducciones(analyzer, contenido, min, max)
    return rep


def getMusicapara(analyzer, c1, c2, min_c1, max_c1, min_c2, max_c2):
    """
    Retorna las pistas en el sistema de recomendación que cumplen dos características
    """
    musica = model.getMusicapara(analyzer, c1, c2, min_c1, max_c1, min_c2, max_c2)
    return musica

def estudiarGenerosMusicales(analyzer,genero):
    estudio = model.estudiarGenerosMusicales(analyzer,genero)
    return estudio

def existeGenero(analyzer,genero):
    existe = model.existeGenero(analyzer,genero)
    return existe

def generoMasEscuchado(analyzer,horaI,horaF):
    metodo = model.generoMasEscuchado(analyzer,horaI,horaF)
    return metodo
    
def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory


