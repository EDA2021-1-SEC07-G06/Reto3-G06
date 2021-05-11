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
from DISClib.Algorithms.Trees import traversal as tv
from datetime import datetime
assert cf

# Construccion de modelos

def newAnalyzer():
    """ 
    Inicializa el analizador
    Retorna el analizador inicializado.
    """
    analyzer = {'eventos': None,
                'sentimental_values': None,
                'evento_etiquetas' : None,
                'artistas': None,
                'pistasIds': None,
                'treeEvents': None,
                'GenerosMusicales' : None
                }

    analyzer['eventos'] = lt.newList('ARRAY_LIST')
    analyzer['sentimental_values'] = lt.newList('ARRAY_LIST')
    analyzer['evento_etiquetas'] = lt.newList('ARRAY_LIST')
    analyzer['pistasIds'] = om.newMap(omaptype='RBT',comparefunction=compareIds)
    analyzer['treeEvents'] = om.newMap(omaptype='RBT',comparefunction=compareIds)
    analyzer['GenerosMusicales'] = mp.newMap(100,prime=109345121,maptype='PROBING',loadfactor=0.5)
    return analyzer

# Funciones para agregar informacion al catalogo

def addEvento(analyzer, evento):
    """
    Añade un evento a la lista de eventos. Y crea los correspondientes 
    apuntadores al map artistas.
    """
    lt.addLast(analyzer['eventos'],evento)
    addTreeEvent(analyzer, evento)

    generos =  analyzer['GenerosMusicales']
    bpm = float(evento['tempo'])
    if (bpm >= float(60)):
        if(bpm >= float(90)):
            entry = mp.get(generos,'reggae')
            valor = me.getValue(entry)
            addEventoArtista(valor['artistas'], evento)
            lt.addLast(valor['eventos'], evento)

    if bpm >= float(70):
        if(bpm >= float(100.000)):
            entry = mp.get(generos,'down-tempo')
            valor = me.getValue(entry)
            addEventoArtista(valor['artistas'], evento)
            lt.addLast(valor['eventos'], evento)

    if bpm >= float(90):
        if bpm >= float(120):
            entry = mp.get(generos,'chill-out')
            valor = me.getValue(entry)
            addEventoArtista(valor['artistas'], evento)
            lt.addLast(valor['eventos'], evento)

    if bpm >= float(85):
        if bpm >= float(115):
            entry = mp.get(generos,'hip-hop')
            valor = me.getValue(entry)
            addEventoArtista(valor['artistas'], evento)
            lt.addLast(valor['eventos'], evento)

    if bpm >= float(120):
        if bpm >= float(125):
            entry = mp.get(generos,'jazz and funk')
            valor = me.getValue(entry)
            addEventoArtista(valor['artistas'], evento)
            lt.addLast(valor['eventos'], evento)

    if bpm >= float(100):
        if bpm >= float(130):
            entry = mp.get(generos,'pop')
            valor = me.getValue(entry)
            addEventoArtista(valor['artistas'], evento)
            lt.addLast(valor['eventos'], evento)

    if bpm >= float(60):
        if bpm >= float(80):
            entry = mp.get(generos,'r&b')
            valor = me.getValue(entry)
            addEventoArtista(valor['artistas'], evento)
            lt.addLast(valor['eventos'], evento)

    if bpm >= float(110):
        if bpm >= float(140):
            entry = mp.get(generos,'rock')
            valor = me.getValue(entry)
            addEventoArtista(valor['artistas'], evento)
            lt.addLast(valor['eventos'], evento)
    
    if bpm >= float(100):
        if bpm >= float(160):
            entry = mp.get(generos,'metal')
            valor = me.getValue(entry)
            addEventoArtista(valor['artistas'], evento)
            lt.addLast(valor['eventos'], evento)




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
    artistas = analyzer
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

def addTreeEvent(analyzer, evento):
    """
    Añade al map de pistas cada track con las etiquetas determinadas
    """
    arbol = analyzer['treeEvents']
    existeEvento = om.contains(arbol, evento['id'])
    if existeEvento:
       entry = om.get(arbol, evento['id'])
       value = me.getValue(entry)
       eventos = value['eventos']
       om.put(eventos,  evento['id'], evento)
    else:
       nuevoElemento =  newTreeEvent(evento['id'])
       eventos = nuevoElemento['eventos']
       om.put(eventos,evento['id'],evento)
       om.put(arbol,evento['id'],nuevoElemento)
      
       

# Funciones para creacion de datos
def newGenero(genero):
    entry = {'genero': None , 'eventos': None,'artistas' : None, 'T1': None,'T2' :None}
    entry['genero'] = genero
    entry['artistas'] = om.newMap(omaptype='RBT',comparefunction=compareArtistas)
    entry['eventos'] = lt.newList('ARRAY_LIST')

    return entry


def newTreeEvent(evento):
    """
    Modela la estructura del entry de un evento.
    """
    entry = {'id': None , 'eventos': None}
    entry['id'] = evento
    entry['eventos'] = om.newMap(omaptype='RBT')
    return entry
    

def newArtista(artista):
    """
    Modela la estructura del entry de un artista.
    """
    entry = {'artista': None , 'eventos': None}
    entry['artista'] = artista
    entry['eventos'] = om.newMap(omaptype='RBT')
    return entry



def newPistaId(pista):
    """
    Modela la estructura del entry de una pista.
    """
    entry = {'pista': None , 'etiquetas': None}
    entry['pista'] = pista
    entry['etiquetas'] = om.newMap(omaptype='RBT')
    return entry


def crearGeneros(analyzer):
    arbolGeneros = analyzer['GenerosMusicales']
    reg = 'reggae'
    dt = 'down-tempo'
    co = 'chill-out'
    hh = 'hip-hop'
    jf = 'jazz and funk'
    pop = 'pop'
    rb = 'r&b'
    rc = 'rock'
    mt = 'metal'
    lista = {reg,dt,co,hh,jf,pop,rb,rc,mt}
    for n in lista:

        if n == reg:
            nuevo = newGenero(n)
            nuevo['T1'] = 60
            nuevo['T2'] = 90
            
        if n == dt:
            nuevo = newGenero(n)
            nuevo['T1'] = 70
            nuevo['T2'] = 100
        if n == co:
            nuevo = newGenero(n)
            nuevo['T1'] = 90
            nuevo['T2'] = 120
        if n == hh:
            nuevo = newGenero(n)
            nuevo['T1'] = 85
            nuevo['T2'] = 115
        if n == jf:
            nuevo = newGenero(n)
            nuevo['T1'] = 120
            nuevo['T2'] =125
        if n == pop:
            nuevo = newGenero(n)
            nuevo['T1'] = 100
            nuevo['T2'] = 130
        if n == rb:
            nuevo = newGenero(n)
            nuevo['T1'] = 60
            nuevo['T2'] = 80
        if n == rc:
            nuevo = newGenero(n)
            nuevo['T1'] = 110
            nuevo['T2'] = 140
        if n == mt:
            nuevo = newGenero(n)
            nuevo['T1'] = 100
            nuevo['T2'] = 160
        
        mp.put(arbolGeneros,n,nuevo)

# Funciones de consulta

def estudiarGenerosMusicales(analyzer,pGenero):
    
    generosMusicales = analyzer['GenerosMusicales']

    totalEventos = 0
    
    genero = pGenero.lower()
    corta = genero.strip()
    generos = corta.split(',')
    
    eventosGenero = mp.newMap(10,prime=109345121,maptype='PROBING', loadfactor=0.5)
    numeroArtistas = mp.newMap(10,prime=109345121,maptype='PROBING', loadfactor=0.5)
    limitesGenero = mp.newMap(10,prime=109345121,maptype='PROBING', loadfactor=0.5)

    tam = len(generos)
    pos = 0
    while tam > 0:
        elemento = generos[pos]
        entry = mp.get(generosMusicales, elemento)

        listaEventos = me.getValue(entry)
        tamañoListaEventos = lt.size(listaEventos['eventos'])
        tamañoArtistas = om.size(listaEventos['artistas'])
        T1 = listaEventos['T1']
        T2 = listaEventos['T2']
        totalEventos += tamañoListaEventos

        entry = { 'genero' : elemento, 'T1': T1,'T2': T2}

        mp.put(eventosGenero,elemento,tamañoListaEventos)
        mp.put(numeroArtistas, elemento, tamañoArtistas)
        mp.put(limitesGenero, elemento, entry)
    
        
        pos += 1
        tam -= 1


    return totalEventos,eventosGenero,numeroArtistas,generos,limitesGenero

def existeGenero(analyzer,pGenero):
    arbolGeneros = analyzer['GenerosMusicales']
    genero = pGenero.lower()
    corta = genero.strip()
    generos = corta.split(',')
    rta = lt.newList('ARRAY_LIST')
    existe = False
    for i in generos:
        i.strip()
    for gen in generos:
        gexiste = mp.contains(arbolGeneros, gen)
        if(gexiste):
            existe = True
        else:
            lt.addLast(rta,gen)
            existe = False

    return rta, existe

def buscarlistatracks(analyzer, trackId):
        tracks = analyzer['pistasIds']
        entry = om.get(tracks,trackId)
        valor = me.getValue(entry)
        etiquetas = valor['etiquetas']
        return etiquetas

def generoMasEscuchado(analyzer,horaI,horaF):

    generos = analyzer['GenerosMusicales']
    tracks = analyzer['pistasIds']
    cantidadTracks = 0


    generoReproducciones = mp.newMap(10,prime=109345121,maptype='PROBING', loadfactor=0.5)
    tracks = mp.newMap(10,prime=109345121,maptype='PROBING', loadfactor=0.5)
    cont = 0
    mayor = None


    keys = tv.inorder(generos)
    for n in keys:
        valor = me.getValue(n)
        reproducciones = valor['eventos']
        numReproducciones = 0

        for elemento in reproducciones:  
            dia = elemento['created_at']
            horaDia = dia.split(' ')
            
            horaEvento = horaDia[1]

            hora1 = datetime.strptime( horaEvento, "%X")
            hora2 = datetime.strptime( horaI, "%X")
            hora3 = datetime.strptime( horaF, "%X")

            if( hora1 > hora2 and hora1 < hora3 ):
                numReproducciones += 1

            
        mp.put(generoReproducciones,numReproducciones,n)
        if (numReproducciones >= cont):
            cont = numReproducciones
            mayor = n
    entry = mp.get(generos, mayor)
    valor = me.getValue(entry)  
    for n in valor:
        trackId = n['track_id']
        etiquetas = buscarlistatracks(analyzer,trackId) 
        lista = lt.newList('ARRAY_LIST')
        contador = 0
        for e in etiquetas():
            entrys = mp.get(etiquetas,e)
            valor = me.getValue(entrys)
            hashtag = valor['hashtag']
            if lt.isPresent(lista,hashtag):
                contador += 1
            else:
                lt.put(lista,hashtag)
        entry = { 'contador' : contador, 'track_id': trackId}
        mp.put(tracks,contador,entry)
            
    sa.sort(tracks, cmpfunction=compareIds)
    sa.sort(generoReproducciones, cmpfunction=compareIds)


    return mayor,cont,generoReproducciones,cantidadTracks,tracks

         


def eventosSize(analyzer):

    """
    Retorna el numero de elementos en la lista de eventos
    """
    eventos = analyzer['eventos']
    return lt.size(eventos)



def pistasSize(analyzer):
    """
    Retorna el numero de elementos en el map de pistas

    """ 
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

def getReproducciones(analyzer, contenido, min, max):
    """
    Retorna el total de reproducciones (eventos de escucha) que se tienen en el sistema de
    recomendación basado en una característica de contenido y con un rango determinado
    """
    num_eventos = 0
    map_art_cumple = om.newMap(omaptype='RBT',comparefunction=compareArtistas)

    for evento in lt.iterator(analyzer["eventos"]):
        if float(evento[contenido]) <= max and float(evento[contenido]) >= min :
            num_eventos += 1
            om.put(map_art_cumple, evento['artist_id'],"")

    num_artistas = om.size(map_art_cumple)

    if num_eventos == 0:
        return None

    return (num_eventos, num_artistas)

def getMusicapara(analyzer, c1, c2, min_c1, max_c1, min_c2, max_c2):
    """
    Retorna las pistas en el sistema de recomendación que cumplen dos características
    """
    map_pista_cumple = om.newMap(omaptype='RBT',comparefunction=compareIds)

    for pista in lt.iterator(analyzer["eventos"]):
        if float(pista[c1]) <= max_c1 and float(pista[c1]) >= min_c1:
            if float(pista[c2]) <= max_c2 and float(pista[c2]) >= min_c2:
                om.put(map_pista_cumple, pista["track_id"], (pista[c1], pista[c2]))

    num_unicas = om.size(map_pista_cumple)

    if num_unicas == 0:
        return None

    return (num_unicas, map_pista_cumple)

    



    


