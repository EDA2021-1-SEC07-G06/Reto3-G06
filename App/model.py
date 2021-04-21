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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

# Construccion de modelos

def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los eventos y su contexto.
    Crea una lista vacia para guardar todos los valores sentimentales.
    Crea una lista vacia para guardar toda la informacion de las etiquetas del evento.


    Se crean indices (Maps) por los siguientes criterios:
    -Caracteristica de contenido 
    -Artista


    Retorna el analizador inicializado.
    """
    analyzer = {'eventos': None,
                'sentimental_values': None,
                'evento_etiquetas' : None,
                'contenida':None,
                'artistas': None,
                'pistasIds': None
                }

    analyzer['eventos'] = lt.newList('ARRAY_LIST')
    analyzer['sentimental_values'] = lt.newList('ARRAY_LIST')
    analyzer['evento_etiquetas'] = lt.newList('ARRAY_LIST')
    analyzer['contenido'] = om.newMap(omaptype='RBT')
    analyzer['artistas'] = om.newMap(omaptype='RBT',comparefunction=compareArtistas)
    analyzer['pistasIds'] = om.newMap(omaptype='RBT',comparefunction=compareIds)
    return analyzer

# Funciones para agregar informacion al catalogo

def addEvento(analyzer, evento):
    """
    Añade un evento a la lista de eventos. Y crea los correspondientes 
    apuntadores al map artistas.
    """
    lt.addLast(analyzer['eventos'],evento)
    addEventoArtista(analyzer, evento)


def addSentimentalValue(analyzer, value):
    """
    Añade un elemento con los valores de sentimiento a la lista sentimental_values.
    """
    lt.addLast(analyzer['sentimental_values'],value)

def addEtiquetas(analyzer, etiqueta):
    """
    Añade las etiquetas de un evento a la lista de evento_etiquetas. Y crea los 
    correspondientes apuntadores al map de pistas.
    """
    lt.addLast(analyzer['evento_etiquetas'],etiqueta)
    addTracksId(analyzer, etiqueta)
    
def addEventoArtista(analyzer, evento):
    """
    Añade al map de artistas cada artista con el evento determinado
    """
    artistas = analyzer['artistas']
    existeArtista = om.contains(artistas, evento['artist_id'])
    if existeArtista:
       entry = om.get(artistas, evento['artist_id'])
       value = me.getValue(entry)
       eventosArtista = value['eventos']
       om.put(eventosArtista, evento['artist_id'],evento)
    else:
       nuevoElemento =  newArtista(evento['artist_id'])
       eventos = nuevoElemento['eventos']
       om.put(eventos,evento['artist_id'],evento)
       om.put(artistas,evento['artist_id'],nuevoElemento)
       

def addTracksId(analyzer, etiqueta):
    """
    Añade al map de pistas cada track con las etiquetas determinadas
    """
    etiquetas = analyzer['pistasIds']
    existeEtiqueta = om.contains(etiquetas, etiqueta['track_id'])
    if existeEtiqueta:
       entry = om.get(etiquetas, etiqueta['track_id'])
       value = me.getValue(entry)
       etiquetasTrack = value['etiquetas']
       om.put(etiquetasTrack, etiqueta['track_id'],etiqueta)
    else:
       nuevoElemento =  newPistaId(etiqueta['track_id'])
       eventos = nuevoElemento['etiquetas']
       om.put(eventos,etiqueta['track_id'],etiqueta)
       om.put(etiquetas,etiqueta['track_id'],nuevoElemento)
      
       

# Funciones para creacion de datos
"""
Modela la estructura del entry de un artista.
"""
def newArtista(artista):
    entry = {'artista': None , 'eventos': None}
    entry['artista'] = artista
    entry['eventos'] = om.newMap(omaptype='RBT')
    return entry

"""
Modela la estructura del entry de una pista.
"""

def newPistaId(pista):
    entry = {'pista': None , 'etiquetas': None}
    entry['pista'] = pista
    entry['etiquetas'] = om.newMap(omaptype='RBT')
    return entry


# Funciones de consulta

"""
Retorna los primeros 5 elementos cargados y los ultimos 5 elementos cargados.
"""
def eventosCargados(analyzer):

   pass

"""
Retorna el numero de elementos en el map de artistas
"""

def artistasSize(analyzer):
    artistas = analyzer['artistas']
    return om.size(artistas)

    """
    Retorna el numero de elementos en la lista de eventos
    """

def eventosSize(analyzer):
    eventos = analyzer['eventos']
    return lt.size(eventos)

    """
    Retorna el numero de elementos en el map de pistas

    """

def pistasSize(analyzer):
    pistas = analyzer['pistasIds']
    return om.size(pistas)

# Funciones utilizadas para comparar elementos dentro de una lista

def compareIds(id1, id2):
    """
    Compara los ids del elemento (Pueden ser id(s) de tracks o eventos)
    """
    if (str(id1) == str(id2)):
        return 0
    elif str(id1)> str(id2):
        return 1
    else:
        return -1

def compareArtistas(artista1, artista2):
    """
    Compara dos artistas
    """
    if (artista1 == artista2):
        return 0
    elif (str(artista1) > str(artista2)):
        return 1
    else:
        return -1


# Funciones de ordenamiento
