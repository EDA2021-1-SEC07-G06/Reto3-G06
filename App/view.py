"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Reproducciones dada una caracteristica y rango. ")
    print("3- Encontrar musica para festejar. ")
    print("4- Encontrar muscia para estudiar. ")
    print("5- Estudiar los generos musicales ")

analyzer = None
"""
Imprime la informacion cargada de los datos.
"""
def printData(eventos,artistas,pistas,listaI, listaF):
    print('Total de registros de eventos de escucha cargados: '+ eventos)
    print('Total de artistas únicos cargados: ' + artistas)
    print('Total de pistas de audio únicas cargadas: ' + pistas + '\n')

    tamañoI = lt.size(listaI)
    tamañoF = lt.size(listaF)
    ci = 0
    cf = 0

    print('***************************************************\n')

    print('PRIMEROS 5 ELEMENTOS CARGADOS')
    print('')

    while ci < tamañoI:

        datos = lt.getElement(listaI,ci)
        
      
        print('***************************************************\n')
        print('Id del evento: ' + datos['id'])
        print('')
        print('Caracteristicas de contenido: \n' + 'Instrumentalidad: ' + datos['instrumentalness'] +'\n'+'Acústica' + datos['acousticness'] +'\n' 
        +'Liveness: ' + datos['liveness'] +'\n'+'speechiness: ' + datos['speechiness'] +'\n'+'Energía: ' + datos['energy'] +'\n'
        +'Capacidad de baile: ' + datos['danceability'] +'\n'+'Valencia'  + datos['valence'] +'\n')
        
        print('Caracteristicas de contexto: \n' + 'Creado en: ' + datos['created_at'] +'\n'+'Idioma del tweet: ' 
         + datos['tweet_lang'] +'\n' +'Idioma: '+ datos['lang'] +'\n'+'Time Zone: '+ datos['time_zone'] +'\n')
       
        
        ci += 1
    print('***************************************************\n')
    print('ULTIMOS 5 ELEMENTOS CARGADOS')
    print('')
    while cf < tamañoF:

        datosF = lt.getElement(listaF,cf)

    
        print('***************************************************\n')
        print('Id del evento: ' + datosF['id'])
        print('')
        print('Caracteristicas de contenido: \n' + 'Instrumentalidad: ' + datosF['instrumentalness'] +'\n'+'Acústica' + datosF['acousticness'] +'\n' 
        +'Liveness: ' + datosF['liveness'] +'\n'+'speechiness: ' + datosF['speechiness'] +'\n'+'Energía: ' + datosF['energy'] +'\n'
        +'Capacidad de baile: ' + datosF['danceability'] +'\n'+'Valencia'  + datosF['valence'] +'\n')
       
        print('Caracteristicas de contexto: \n' + 'Creado en: ' + datosF['created_at'] +'\n'+'Idioma del tweet: ' 
         + datosF['tweet_lang'] +'\n' +'Idioma: '+ datosF['lang'] +'\n'+'Time Zone: '+ datosF['time_zone'] +'\n')
       

        cf += 1
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        analyzer = controller.init()
        listas = controller.loadData(analyzer)
        eventos = controller.tamañoEventos(analyzer)
        artistas = controller.tamañoArtistas(analyzer)
        pistas = controller.tamañoPistas(analyzer)
        printData(str(eventos),str(artistas),str(pistas),listas[0],listas[1])

    elif int(inputs[0]) == 2:
        pass
    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass

    else:
        sys.exit(0)
sys.exit(0)
