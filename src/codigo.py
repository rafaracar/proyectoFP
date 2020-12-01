# -*- coding: utf-8 -*-
'''
Created on 10 nov. 2020

@author: Rafael
'''
import csv
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

#######################################################################################################################     
def filtra_tipos ():
    with open("../pokemon.csv", encoding="utf8") as f: 
        tipo_para_buscar= input("Escribe el tipo por el que va a filtrar:")
        reader= csv.reader(f)
        for row in reader:
            if tipo_para_buscar in row[35] or tipo_para_buscar in row[36]:
                print("Su nombre es", row[30], ",y sus tipos son", row[36],"y", row[37])
#######################################################################################################################     

#######################################################################################################################                     
def buscar_por_nombre (): 
        nombre_a_buscar = (input("escribe el nombre del pokemon a buscar:"))
        for pokemon in list:
            if pokemon.nombre.lower() == nombre_a_buscar.lower():
                print("Su numero de la pokedex es:", pokemon.num_pokedex, ".Su nombre es:",pokemon.nombre, ".Sus habilidades pueden ser:", pokemon.habilidad,".Su tipo es:", pokemon.tipo1, pokemon.tipo2, ".Su altura es:", pokemon.altura,"m", ".Su peso es:", pokemon.peso,"Kg")
#######################################################################################################################     

#######################################################################################################################     
def buscar_por_num_pokedex ():
        numero_pokedex= (input("escbribe un numero de la pokedex -del 1 al 801-"))
        for pokemon in list:
            if pokemon.num_pokedex == numero_pokedex:
                    print("Su numero de la pokedex es:", pokemon.num_pokedex, ".Su nombre es:",pokemon.nombre, ".Sus habilidades pueden ser:", pokemon.habilidad,".Su tipo es:", pokemon.tipo1, pokemon.tipo2, ".Su altura es:", pokemon.altura,"m", ".Su peso es:", pokemon.peso,"Kg")
#######################################################################################################################     

#######################################################################################################################     

def ver_todos_los_pokemon ():
    for pokemon in list:
            print(pokemon.nombre, "Tipo:", pokemon.tipo1, pokemon.tipo2, "Su ratio de captura es:", pokemon.ratio_captura, "la curva de experiencia es:", pokemon.exp_nivel, "El porcentaje de que te encuentres a un macho en estado salvaje es:", pokemon.porcentaje_macho, "Es legendario:", pokemon.legendario)

#######################################################################################################################     

#######################################################################################################################     
def tabla_debilidad_fuerza ():
     nombre_a_buscar= input("Escribe el nombre del pokemon del que quieres saber sus debilidades,")
     for pokemon in list:
            if pokemon.nombre.lower()== nombre_a_buscar.lower():
                print("Contra acero", pokemon.contra_acero,"Contra agua", pokemon.contra_agua,"Contra bicho", pokemon.contra_bicho,"Contra dragon", pokemon.contra_dragon,"Contra electrico", pokemon.contra_electrico,"Contra Fantasma", pokemon.contra_fantasma,"Contra Fuego", pokemon.contra_fuego,"Contra Hada", pokemon.contra_hada,"Contra hielo", pokemon.contra_hielo,"Contra lucha", pokemon.contra_lucha,"Contra normal", pokemon.contra_normal,"Contra planta", pokemon.contra_planta,"Contra psiquico", pokemon.contra_psiquico,"Contra roca", pokemon.contra_roca,"Contra siniestro", pokemon.contra_siniestro,"Contra tierra", pokemon.contra_tierra,"Contra veneno", pokemon.contra_veneno,"Contra volador", pokemon.contra_volador)
#######################################################################################################################     


#######################################################################################################################     
def cantidad_total_de_pokemon_segun_tipo ():
    with open("../pokemon.csv", encoding="utf8") as f:
        tipo_para_contar= input("Escribe el tipo para contar la cantidad de pokemon:")
        reader=csv.reader(f)
        cantidad_de_pokemon=0
        for row in reader:
            if tipo_para_contar in row[35] or tipo_para_contar in row[36]:
                cantidad_de_pokemon+=1
                
                
        print("Hay",cantidad_de_pokemon, " pokemons del tipo", tipo_para_contar)
 #######################################################################################################################     
        
 #######################################################################################################################            
def cantidad_de_legendarios():
      with open("../pokemon.csv", encoding="utf8") as f:
          cantidad_legendarios=0
          reader=csv.reader(f)
          for row in reader:
                if row[40]=='1':
                    cantidad_legendarios+=1
            
            
            
            
          print("Hay",cantidad_legendarios, " pokemons legendarios")
#######################################################################################################################       
    
    
#######################################################################################################################         
def ratio_de_legendarios():
    with open("../pokemon.csv", encoding="utf8") as f:
        reader=csv.reader(f)
        cantidad_legendarios=0
        cantidad_no_legendarios=0
        for row in reader:
            if row[40]== '1':
                cantidad_legendarios+=1
            elif row[40]=='0':
                cantidad_no_legendarios+=1
        
        ratio= cantidad_no_legendarios/cantidad_legendarios
        print("Por cada pokemon legendario hay", round(ratio),"pokemon no legendarios")
 #######################################################################################################################            

###########################################################################################################
def media_de_pasos_para_abrir_huevo ():   #que es lo que no funciona de aqui?
    with open("../pokemon.csv", encoding="utf8") as f:
        reader=csv.reader(f)
        cantidad_de_pasos=0
        cantidad_de_pokemon=0
        pasoshuevo=[]
        for row in reader:
            if pokemon in list:
                pasoshuevo.append(row[20])
        pasoshuevo=[float(x)for x in pasoshuevo]
        for i in pasoshuevo:
            media_de_pasos=(media_de_pasos+i)
        media_de_pasos=media_de_pasos/len(pasoshuevo)
            

        print("La media de pasos para abrir un huevo es de", round(media))
#######################################################################################################################     
        
    
#######################################################################################################################     
def cualidad_pokemon ():   #este no se como estructurarlo
    with open("../pokemon.csv",encoding="utf8") as f:
       x=input("elige entre estas cualidades: 1-mas alto, 2- mayor peso, 3-mas vida, 4-mas defensa, 5-mas rapido")
       reader=csv.reader(f)
    for row in reader:
        if x=='1':
            print(max(row[27]))
        elif x=='2':
            print(max(row[38]))
        elif x=='3':
            print(max(row[28]))
        elif x=='4':
            print(max(row[25]))
        elif x=='5':
            print(max(row[35]))
#######################################################################################################################     






#######################################################################################################################     
if primer_input == 'si':
    print("""¿Como desea buscar?
    1- Por nombre
    2- Por numero de pokedex
    3- Por tipo
    4- Quiero ver todos los Pokemon
    5- Quiero saber a que es fuerte y debil un pokemon 
    6- ¿Cuantos pokemon hay de este tipo?
    7- ¿Cuantos lengedarios hay?
    8- Dato sobre los legendarios
    9- Media de pasos por huevo
    10-¿Que pokemon es el mas...?""")
#######################################################################################################################     
    
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
    elif segundo_input== '6':
        cantidad_total_de_pokemon_segun_tipo()
    elif segundo_input== '7':
        cantidad_de_legendarios()
    elif segundo_input== '8':
        ratio_de_legendarios()
    elif segundo_input== '9':
        media_de_pasos_para_abrir_huevo()
    elif segundo_input=='10':
        cualidad_pokemon()





















































elif primer_input == 'no':
    print("Vale, no quieres hacer nada, te entiendo.")
        
        
       
        
       
        
        
        
        
        
        
        
        
        
        