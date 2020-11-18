# -*- coding: utf-8 -*-
'''
Created on 10 nov. 2020

@author: Rafael
'''
import csv
from builtins import set
from _ast import If
contador=0 
list =[]

class Pokemon:
    num_pokedex = ""
    nombre =  ""
    nombre_japones =  ""
    tipo1 = ""
    tipo2 = ""
    habilidad =  ""
    altura = ""
    peso = ""
    contra_bicho =  ""
    contra_siniestro =  ""
    contra_dragon =  ""
    contra_electrico =  ""
    contra_hada =  ""
    contra_acero =  ""
    contra_lucha =  ""
    contra_fuego =  ""
    contra_volador =  ""
    contra_fantasma =  "" 
    contra_planta =  ""
    contra_tierra =  ""
    contra_hielo =  ""
    contra_normal =  ""
    contra_veneno =   ""
    contra_psiquico =  ""
    contra_roca =  ""
    contra_agua =  ""
    exp_nivel =  ""
    ataque =  ""
    ataque_especial =  ""
    defensa =  ""
    defensa_especial =  ""
    vida =  ""
    velocidad =  ""
    pasos_huevo =  ""
    ratio_captura =  ""
    felicidad_base =  ""
    legendario =   ""
    total_estadisticas_base =  ""
    porcentaje_macho = ""
    clasificacion = ""
    generacion = ""
    
    
    def __init__(self, habilidad,contra_bicho,contra_siniestro,contra_dragon,contra_electrico,contra_hada,contra_lucha,contra_fuego,contra_volador,contra_fantasma,contra_planta,contra_tierra,contra_hielo,contra_normal,contra_veneno,contra_psiquico,contra_roca,contra_acero,contra_agua,ataque,pasos_huevo,felicidad_base,total_estadisticas_base,ratio_captura,clasificacion,defensa,exp_nivel,altura,vida,nombre_japones,nombre,porcentaje_macho,num_pokedex,ataque_especial,defensa_especial,velocidad,tipo1,tipo2,peso,generacion,legendario):
        self.num_pokedex = num_pokedex
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.habilidad = habilidad
        self.altura = altura
        self.peso = peso
        self.contra_bicho = contra_bicho
        self.contra_siniestro = contra_siniestro
        self.contra_dragon = contra_dragon
        self.contra_electrico = contra_electrico
        self.contra_hada =  contra_hada
        self.contra_acero =  contra_acero
        self.contra_lucha =  contra_lucha
        self.contra_fuego =  contra_fuego
        self.contra_volador =  contra_volador
        self.contra_fantasma =   contra_fantasma
        self.contra_planta =  contra_planta
        self.contra_tierra =  contra_tierra
        self.contra_hielo =  contra_hielo
        self.contra_normal =  contra_normal
        self.contra_veneno =   contra_veneno
        self.contra_psiquico =  contra_psiquico
        self.contra_roca =  contra_roca
        self.contra_agua =  contra_agua
        self.exp_nivel =  exp_nivel
        self.ataque =  ataque
        self.ataque_especial =  ataque_especial
        self.defensa =  defensa
        self.defensa_especial =  defensa_especial
        self.vida =  vida
        self.velocidad =  velocidad
        self.pasos_huevo =  pasos_huevo
        self.ratio_captura =  ratio_captura
        self.felicidad_base =  felicidad_base
        self.legendario =   legendario
        self.total_estadisticas_base =  total_estadisticas_base
        self.porcentaje_macho = porcentaje_macho
        self.clasificacion = clasificacion
        self.generacion = generacion
        

with open("../pokemon.csv", encoding="utf8") as f:
    reader= csv.reader(f)
    for row in reader:
        if contador==0:
            contador+=1
        else:
            pokemon = Pokemon(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40])
            list.append(pokemon)
            
            
                   
print("¿Desea realizar una busqueda en la base de datos?")



primer_input= input("Escriba 'Si' o 'No':")
def filtra_tipos (pokemon):
    return pokemon.tipo1 or pokemon.tipo2 == tipo_para_buscar
if primer_input == 'Si':
    print("""¿Como desea buscar?
    1- Por nombre
    2- Por numero de pokedex
    3- Por tipo
    4- Quiero ver todos los Pokemon""")
    segundo_input= input()    
    if segundo_input== '1':
        nombre_a_buscar = (input("escribe el nombre del pokemon a buscar:"))
        for pokemon in list:
            if pokemon.nombre.lower() == nombre_a_buscar.lower():
                print("Su numero de la pokedex es:", pokemon.num_pokedex, ".Su nombre es:",pokemon.nombre, ".Sus habilidades pueden ser:", pokemon.habilidad,".Su tipo es:", pokemon.tipo1, pokemon.tipo2, ".Su altura es:", pokemon.altura,"m", ".Su peso es:", pokemon.peso,"Kg")
    elif segundo_input== '2':
        for pokemon in list:
            numero_pokedex= (input("escbribe un numero de la pokedex -del 1 al 801-"))
            if pokemon.num_pokedex == numero_pokedex:
                print("Su numero de la pokedex es:", pokemon.num_pokedex, ".Su nombre es:",pokemon.nombre, ".Sus habilidades pueden ser:", pokemon.habilidad,".Su tipo es:", pokemon.tipo1, pokemon.tipo2, ".Su altura es:", pokemon.altura,"m", ".Su peso es:", pokemon.peso,"Kg")
    elif segundo_input== '3':
        tipo_para_buscar= input("Escribe el tipo por el que va a filtrar:")
        for pokemon in list:
            tipos= filter(filtra_tipos(pokemon),)
            pokemon_filtrados= list(tipos)
            print(pokemon_filtrados)
                
    elif segundo_input== '3':
        for pokemon in list:
            print("Su numero de la pokedex es:", pokemon.num_pokedex, ".Su nombre es:",pokemon.nombre, ".Sus habilidades pueden ser:", pokemon.habilidad,".Su tipo es:", pokemon.tipo1, pokemon.tipo2, ".Su altura es:", pokemon.altura,"m", ".Su peso es:", pokemon.peso,"Kg")
    elif segundo_input== '4':
        for pokemon in list:
            print(pokemon.nombre, "Tipo:", pokemon.tipo1, pokemon.tipo2, "Su ratio de captura es:", pokemon.ratio_captura, "la curva de experiencia es:", pokemon.exp_nivel, "El porcentaje de que te encuentres a un macho en estado salvaje es:", pokemon.porcentaje_macho, "Es legendario:", pokemon.legendario )
            
            
            
            
            
            
            
            
            