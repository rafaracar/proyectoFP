# -*- coding: utf-8 -*-
'''
Created on 10 nov. 2020

@author: Rafael
'''
import csv
from builtins import set
from _ast import If, Or
from Pokemon import  Pokemon
contador=0 
list =[]


with open("../pokemon.csv", encoding="utf8") as f:
    reader= csv.reader(f)
    for row in reader:
        if contador==0:
            contador+=1
        else:
            pokemon = Pokemon(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40])
            list.append(pokemon)
            
            
                   
print("¿Desea realizar una busqueda en la base de datos?")



primer_input= input("Escriba 'si' o 'no':")
def filtra_tipos ():
    with open("../pokemon.csv", encoding="utf8") as f: 
        tipo_para_buscar= input("Escribe el tipo por el que va a filtrar:")
        reader= csv.reader(f)
        for row in reader:
            if tipo_para_buscar in row[35] or tipo_para_buscar in row[36]:
                print("Su nombre es", row[30], ",y sus tipos son", row[36],"y", row[37])
def buscar_por_nombre (): 
        nombre_a_buscar = (input("escribe el nombre del pokemon a buscar:"))
        for pokemon in list:
            if pokemon.nombre.lower() == nombre_a_buscar.lower():
                print("Su numero de la pokedex es:", pokemon.num_pokedex, ".Su nombre es:",pokemon.nombre, ".Sus habilidades pueden ser:", pokemon.habilidad,".Su tipo es:", pokemon.tipo1, pokemon.tipo2, ".Su altura es:", pokemon.altura,"m", ".Su peso es:", pokemon.peso,"Kg")

def buscar_por_num_pokedex ():
        numero_pokedex= (input("escbribe un numero de la pokedex -del 1 al 801-"))
        for pokemon in list:
            if pokemon.num_pokedex == numero_pokedex:
                    print("Su numero de la pokedex es:", pokemon.num_pokedex, ".Su nombre es:",pokemon.nombre, ".Sus habilidades pueden ser:", pokemon.habilidad,".Su tipo es:", pokemon.tipo1, pokemon.tipo2, ".Su altura es:", pokemon.altura,"m", ".Su peso es:", pokemon.peso,"Kg")


def ver_todos_los_pokemon ():
    for pokemon in list:
            print(pokemon.nombre, "Tipo:", pokemon.tipo1, pokemon.tipo2, "Su ratio de captura es:", pokemon.ratio_captura, "la curva de experiencia es:", pokemon.exp_nivel, "El porcentaje de que te encuentres a un macho en estado salvaje es:", pokemon.porcentaje_macho, "Es legendario:", pokemon.legendario)


def tabla_debilidad_fuerza ():
     nombre_a_buscar= input("Escribe el nombre del pokemon del que quieres saber sus debilidades,")
     for pokemon in list:
            if pokemon.nombre.lower()== nombre_a_buscar.lower():
                print("Contra acero", pokemon.contra_acero,"Contra agua", pokemon.contra_agua,"Contra bicho", pokemon.contra_bicho,"Contra dragon", pokemon.contra_dragon,"Contra electrico", pokemon.contra_electrico,"Contra Fantasma", pokemon.contra_fantasma,"Contra Fuego", pokemon.contra_fuego,"Contra Hada", pokemon.contra_hada,"Contra hielo", pokemon.contra_hielo,"Contra lucha", pokemon.contra_lucha,"Contra normal", pokemon.contra_normal,"Contra planta", pokemon.contra_planta,"Contra psiquico", pokemon.contra_psiquico,"Contra roca", pokemon.contra_roca,"Contra siniestro", pokemon.contra_siniestro,"Contra tierra", pokemon.contra_tierra,"Contra veneno", pokemon.contra_veneno,"Contra volador", pokemon.contra_volador)
if primer_input == 'si':
    print("""¿Como desea buscar?
    1- Por nombre
    2- Por numero de pokedex
    3- Por tipo
    4- Quiero ver todos los Pokemon
    5- Quiero saber a que es fuerte y debil un pokemon 
    6- proximamente
    7- proximamente
    8- proximamente""")

    
    segundo_input= input()    
    if segundo_input== '1':
        buscar_por_nombre()
    elif segundo_input== '2':
        buscar_por_num_pokedex()
    elif segundo_input== '3':
        filtra_tipos()          
    elif segundo_input== '4':
        ver_todos_los_pokemon()
    elif segundo_input== '5':
        tabla_debilidad_fuerza()     























































elif primer_input == 'no':
    print("Vale, no quieres hacer nada, te entiendo.")
        
        
       
        
       
        
        
        
        
        
        
        
        
        
        