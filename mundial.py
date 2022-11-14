# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:31:44 2022

@author: saric
"""

def carga_de_datos (archivo)->dict:
    """
    Función 1:
    Recibe el archivo con la info de los jugadores FIFA 2022.
    -------
    Retorno:
        Diccionario de listas de diccionarios. 
        {club1: [{jugador1},{jugador2},...],club2:[{jugador1},{jugador2},...]}
    """
    clubes={}
    archivo=open(archivo, "r", encoding='utf8')
    titulos=archivo.readline().split(",")
    #print(titulos)
    
    linea=archivo.readline()
    while len(linea)>0:
        info_jugador=linea.strip("\n").split(",")
        cual_equipo=info_jugador[0]
        jugador={}
        jugador["name"]=info_jugador[1]
        jugador["wage"]=info_jugador[2]
        jugador["age"]=info_jugador[3]
        jugador["pace"]=info_jugador[4]
        jugador["shooting"]=info_jugador[5]
        jugador["passing"]=info_jugador[6]
        jugador["dribbling"]=info_jugador[7]
        jugador["position"]=info_jugador[8]
        jugador["joined"]=info_jugador[9]
        jugador["contract"]=info_jugador[10]
        jugador["nationality"]=info_jugador[11]
        jugador["preferred_foot"]=info_jugador[12]
        jugador["international_reputation"]=info_jugador[13]
        if not cual_equipo in clubes:
            clubes[cual_equipo]=[jugador]
        else:
            clubes[cual_equipo].append(jugador)
        
        linea=archivo.readline()
        
    archivo.close()
    return clubes

cosito=carga_de_datos("players.csv")
def equipos_con_caracter(caracter:str,dicci)->dict:
    """
    Función 2:
    Recibe una cadena de caracteres.
    -----
    Retorno:
        Diccionario de listas de diccionarios de los clubes que contengan su nombre.
        Filtra el primer diccionario (1° función). 
        Si no hay nada, rta={}
        
    """
    filtrado={}
    for club in dicci:
        if caracter in club:
            filtrado[club]=dicci[club]
            
    return filtrado
#Marvin Olawale Akinlabi Park 

def promedio_salarios(clubes:dict, club:str)->float:
    """
    Función 3:
    Recibe el diccionario con los clubes y un str con el club
    que se quiere analizar.
    ----------
    Retorno:
        Float con el promedio de los salarios de los jugadores
        del equipo dado por parámetro. 

    """
    lista=clubes[club]
    suma=0
    for jugador in lista:
        salario=float(jugador["wage"])
        suma+=salario
        
    promedio=suma/(len(lista))
    return round(promedio,2)


def buscar_jugador(nombre:str,clubes:dict)->dict:
    """
    Me busca un jugador que me dan por str.
    -------
    Retorno:
        Dict con la info de ese jugador. 
        None si no se encuentra.
        
    """
    jugador=None
    for club in clubes:
        for i in clubes[club]:
            if i["name"]==nombre:
                jugador=i
            
    return jugador


def puntaje_jugador(jugador:dict)->float:
    """
    Función 4:
    Recibe el jugador o el diccionario del jugador.
    No estoy segura .-.
    -------
    Retorno:
        float con el puntaje.
        No especifica puntaje máximo ni aproximaciones.

    """
    puntaje=0
    if jugador.get("position")=="SUB" or jugador.get("position")=="RES":
        puntaje+=0
    elif jugador.get("position")=="ST" or jugador.get("position")=="RS" or jugador.get("position")=="LS" or jugador.get("position")=="CF" or jugador.get("position")=="LF" or jugador.get("position")=="RF":
        puntaje+= (float(jugador["pace"])*0.1  +
                   float(jugador["shooting"])*0.45+
                   float(jugador["passing"])*0.05+
                   float(jugador["dribbling"])*0.4
                   )
    else:
        puntaje+=(float(jugador["pace"])*0.3+
                 float(jugador["shooting"])*0.1+
                 float(jugador["passing"])*0.4+
                 float(jugador["dribbling"])*0.2
                             )
    if ("L" in jugador.get("position") and jugador.get("preferred_foot")=="Left") or ("R" in jugador.get("position") and jugador.get("preferred_foot")=="Right"):
        puntaje+=0.05
    return puntaje

def mejor_peor_jugadores(clubes:dict)->dict:
    """
    Función 5.
    Recibo el diccionario completo de clubes.
    -------
    Retorno:
        Dict que tenga como llaves el nombre del club y que el valor sea otro dict 
        con las llaves "mejor" y "peor" y valores los nombres de los pelados.

    """
    equiposs={}
    for club in clubes:
        i=0
        for jugador in range(0,len(clubes[club])):
            if i==0:
                mejor=clubes[club][jugador]
                peor=clubes[club][jugador]
            else:
                i+=1
                if puntaje_jugador(clubes[club][jugador])>puntaje_jugador(mejor):
                    mejor=clubes[club][jugador]
                elif puntaje_jugador(clubes[club][jugador])<puntaje_jugador(peor):
                    peor=clubes[club][jugador]
            i+=1
            
        equiposs[club]={"mejor":mejor["name"],"peor":peor["name"]}
        
    return equiposs


    
def jugadores_de_posicion(clubes:dict, posicion:str)->int:
    """
    Función 6.
    Recibo el diccionario completo de clubes.
    -------
    Retorno:
        Int con la cantidad de jugadores que juegan en esa posición.
        Si no hay ninguno, retorna 0. 

    """
    posicioon=0
    for club in clubes: 
        for jugador in range(0,len(clubes[club])):
            if clubes[club][jugador].get("position")==posicion:
                posicioon+=1
                
    return int(posicioon)


def paises (clubes:dict)->dict:
    """
    Función 7.
    Recibe el diccionario completo de los clubes.
    -------
    Retorno:
        Diccionario con los jugadores de un país en una lista.
    """
    la_sele={}
    #nationality
    for club in clubes:
        for jugador in range(0,len(clubes[club])):
            if clubes[club][jugador].get("nationality") in la_sele.keys():
                la_sele[clubes[club][jugador]["nationality"]].append(clubes[club][jugador]["name"])
                
            else:
                la_sele[clubes[club][jugador].get("nationality")]=[clubes[club][jugador]["name"]]
                
            
    return la_sele


def top_10_paises(clubes:dict)->list:
    """
    Función 8 .
    Recibe los top 10 países según su reputación internacional promedio. 
    -------
    Retorno: 
        La lista tiene como valores los 10 nombres que pertenecen al ranking.
        Están ordenados asendentemente. 
    """
    dicci_paises=paises(clubes)
    dicci_reputacion={}
    for pais in dicci_paises:
        suma=0
        for jugador in dicci_paises[pais]:
            dicci_jugador=buscar_jugador(jugador, clubes)
            suma+=float(dicci_jugador["international_reputation"])
        dicci_reputacion[pais]=suma
    numeros=dicci_reputacion.values()
    numeros.sort()
    mejores_10=numeros[-10:]
    top_10=[]
    for pais in dicci_reputacion:
        for puntaje in mejores_10:
            if dicci_reputacion[pais]==puntaje:
                top_10.append(pais)
    return top_10
    
    
    
    
print(top_10_paises(cosito))
    
    