# -*- coding: utf-8 -*-
'''
Created on 10 nov. 2020

@author: Rafael
'''
import csv
contador=0 
list =[]
nombre_a_buscar = (input("escribe el nombre del pokemon a buscar:"))
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
            
    for pokemon in list:
        if pokemon.nombre.lower() == nombre_a_buscar.lower():
            print(pokemon.nombre)
            
            
            

                
                        
                

