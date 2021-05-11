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
from DISClib.ADT import orderedmap as om
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
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
    print("4- Encontrar musica para estudiar. ")
    print("5- Estudiar los generos musicales ")
    print("6- Género musical más escuchado en un horario")
    print("0- Salir")

analyzer = None
"""
Imprime la informacion cargada de los datos.
"""
def printData(eventos,pistas,listaI, listaF):
    print('Total de registros de eventos de escucha cargados: '+ eventos)
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
        print('Caracteristicas de contenido: \n' + 'Instrumentalidad: ' + datosF['instrumentalness'] +'\n'+'Acústica: ' + datosF['acousticness'] +'\n' 
        +'Liveness: ' + datosF['liveness'] +'\n'+'speechiness: ' + datosF['speechiness'] +'\n'+'Energía: ' + datosF['energy'] +'\n'
        +'Capacidad de baile: ' + datosF['danceability'] +'\n'+'Valencia: '  + datosF['valence'] +'\n')
       
        print('Caracteristicas de contexto: \n' + 'Creado en: ' + datosF['created_at'] +'\n'+'Idioma del tweet: ' 
         + datosF['tweet_lang'] +'\n' +'Idioma: '+ datosF['lang'] +'\n'+'Time Zone: '+ datosF['time_zone'] +'\n')
       

        cf += 1

def printReproducciones (respuesta):
    print("\n Total de reproducciones: " + str(respuesta[0])
          + "\n Total de artistas únicos: " + str(respuesta[1]) + "\n")

def printMusicapara(respuesta, c1, c2):
    print("\nTotal de pistas únicas: " + str(respuesta[0]))
    print("\n... Unique track id ...\n")
    cont = 0
    
    lst = om.valueSet(respuesta[1])
    cod = om.keySet(respuesta[1])

    if lt.size(cod) >= 5:
        for id in lt.iterator(cod):
            datos = om.get(respuesta[1],id)
            valor = datos["value"]
            
            cont += 1
            print("Track: "+ str(id) + " with " + str(c1) + " of " + str(valor[0]) + 
                     " and " + str(c2) + " of " + str(valor[1]) + "\n")         
            if cont > 4:
                return
         
    else:
        for id in lt.iterator(cod):
            for pista in lt.iterator(lst):
                while cont <= lt.size(lst):
                    cont += 1
                    print("Track: "+ str(id) + " with " + str(c1) + " of " + str(pista[0]) + 
                      " and " + str(c2) + " of " + str(pista[1]) + "\n")
                
def imprimirEstudio(totalEventos, eventosGenero, numeroArtistas,generos,limitesGenero):
    
    print("") 
    print("Total de reproducciones: " + str(totalEventos))
    print("")

    for n in generos:
        entry1 = mp.get(eventosGenero,n)
        valor = me.getValue(entry1)

        entry2 = mp.get(numeroArtistas,n)
        valorArtista = me.getValue(entry2)

        entry3 = mp.get(limitesGenero,n)
        limites = me.getValue(entry3)
        limite1 = limites['T1']
        limite2 = limites['T2']

        print("============="+ n.upper() + "=============")
        print("Para " + n.upper() + " el tempo es entre " +str(limite1) + " y " + str(limite2) + " BPM")
        print("Reproducciones de "+ n.upper()+": "+ str(valor) + " con "+ str(valorArtista) + " artistas. " )

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
        pistas = controller.tamañoPistas(analyzer)
        printData(str(eventos),str(pistas),listas[0],listas[1])

    elif int(inputs[0]) == 2:
        contenido = input("Característica de contenido buscada: ")
        min = float(input("Valor minimo: "))
        max = float(input("Valor máximo: "))
        respuesta = controller.getReproducciones(analyzer, contenido, min, max)
        print("++++++ Req. No. 1 results ... +++++ \n" + contenido + " is between "
              + str(min) + " and " + str(max))
        if respuesta == None:
            print("\nNo se encontraron reproducciones\n")
        else:
            printReproducciones(respuesta)

    elif int(inputs[0]) == 3:
        min_energy = float(input("Valor minimo de energy: "))
        max_energy = float(input("Valor máximo de energy: "))
        min_dance = float(input("Valor minimo de danceability: "))
        max_dance = float(input("Valor máximo de danceability: "))

        c1 = "energy"
        c2 = "danceability"
        
        respuesta = controller.getMusicapara(analyzer, c1, c2, min_energy, max_energy, min_dance, max_dance)
        print("\n++++++ Req. No. 2 results ... ++++++")
        print("energy is between "+ str(min_energy) + " and " + str(max_energy))
        print("danceability is between "+ str(min_dance) + " and " + str(max_dance))

        if respuesta == None:
            print("No se encontraron pistas que cumplan con los requisitos")
        else:
            printMusicapara(respuesta, c1, c2)

    elif int(inputs[0]) == 4:
        min_inst = float(input("Valor minimo de instrumentalidad: "))
        max_inst = float(input("Valor máximo de instrumentalidad: "))
        min_tempo = float(input("Valor minimo de tempo: "))
        max_tempo = float(input("Valor máximo de tempo: "))

        c1 = "instrumentalness"
        c2 = "tempo"
        
        respuesta = controller.getMusicapara(analyzer, c1, c2, min_inst, max_inst, min_tempo, max_tempo)
        print("\n++++++ Req. No. 3 results ... ++++++")
        print("instrumentalness is between "+ str(min_inst) + " and " + str(max_inst))
        print("tempo is between "+ str(min_tempo) + " and " + str(max_tempo))

        if respuesta == None:
            print("No se encontraron pistas que cumplan con los requisitos")
        else:
            printMusicapara(respuesta, c1, c2)

    elif int(inputs[0]) == 5:
        genero = input("Genero(s) que desea estudiar: ")
        existe = controller.existeGenero(analyzer,genero)
        if(existe[1]):
            rta = controller.estudiarGenerosMusicales(analyzer,genero)
            imprimirEstudio(rta[0],rta[1],rta[2],rta[3],rta[4])

        elif(existe[1]== False):
            noEncontrados = existe[0]
            rest = None
            print("Genero(s) no econtrado(s): ")
            tam = lt.size(noEncontrados)
            pos = 0
            while tam > 0:
                elemento = lt.getElement(noEncontrados,pos)
                print(elemento)
                tam -= 1
                pos += 1
            rta = input("¿desea crearlo(s)?\n1. Si\n2. No\n")
            if(rta == str(1)):
                for i in noEncontrados:
                    T1 = input("Digite el valor minimo para el tempo para " + n +": ") 
                    T2 = input("Digite el valor maximo para el tempo para " + n +": ")
                    controller.crearGenero(analyzer,n,float(T1),float(T2))
            
    elif int(inputs[0]) == 6:
        horaI = input("Valor minimo de hora: ")
        horaF = input("valor maximo de hora: ")
        rta = controller.generoMasEscuchado(analyzer,horaI,horaF)
        print("")
        print("Total de reproducciones entre " + horaI + " & " + horaF + ": " + rta[1])
        print("")
        print("========REPRODUCCIONES DE GENEROS=======")
        lista1 = rta[2] 
        cont = 1
        for n in lista1:
            
            key = me.getKey(n)
            valor = me.getValue(n)
            print("TOP " + str(cont) + ": " + valor + " con " + key + "reproducciones" )
            cont += 1
        print("")
        print("El genero TOP es: " + rta[0] + " con " + rta[1] + " reproducciones.") 

        print("============"+ rta[0] + "SENTIMENTAL VALUES" + +"===========")
        print(rta[0] + " tiene " + rta[3] + " tracks unicos.")
        print("El top 10 de tracks son: ")
        print("")
        con = 1
        lista2 = rta[4]
        for i in lista2:
           key = me.getKey(i)
           valor = me.getValue(i)
           print("TOP " + str(con) + " track: " +  valor + " con " + key + " hashtags")

           if con == 10:
               break
           con +=1
    else:
        sys.exit(0)
sys.exit(0)
