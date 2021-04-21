"""
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

import config as cf
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
    loadEventos(analyzer)
    loadEtiquetas(analyzer)
    loadSenValues(analyzer)
    pass

def loadEventos(analyzer):
    """
    Carga los videos del archivo.
    """
    eventosfile = cf.data_dir + 'context_content_features-small.csv'
    input_file = csv.DictReader(open(eventosfile, encoding='utf-8'))
    for evento in input_file:
        model.addEvento(analyzer, evento)


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

