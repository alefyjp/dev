#!/usr/bin/python3
# ===========================================================================================
# Projeto
# Autor: Alefy, Rick
# ===========================================================================================

import random
import os
import sys

# Usuario
sair = "nao"
tk_usuario = ""
nome_oponente = "Sem oponente"
tk_oponente = ""
rodada=0
tem_oponente=0
pasta = "/opt/cards/"
nome_usuario = ""
conf_usuario = ""
candidatos = []

# Configuracoes
carta1 = 0
carta2 = 0
carta3 = 0

# Usuario
while sair == "nao":
    # Definindo informacoes do usuario
    if nome_usuario == "":
        nome_usuario = str(input("Informe o seu nome: "))

    if nome_usuario != "" and tk_usuario =="":
        tk_usuario = nome_usuario + str(random.randint(0,9)) + "abc" + str(random.randint(0,9))
        print("Usuario: " + nome_usuario)
        print("Token : " + tk_usuario)
        sys.stdout.flush()

        #Criando arquivo de configuracao do usuario
        conf_usuario = open(pasta+"/"+tk_usuario+".txt", "w")

        # Salvando informações do usuario
        conf_usuario = open(pasta+"/"+tk_usuario+".txt", "a")

        conf_usuario.write(pasta+"/"+tk_usuario+"\n")
        conf_usuario.write(nome_usuario)
        conf_usuario.close()

    # Carregando configuracoes
    if tk_oponente =="":
        for diretorio, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                candidatos.append(arquivo)
                #print(arquivo)

        #Elegendo oponente
        for c in candidatos :
            if c != tk_usuario+".txt" :
                print("oponente: "+ c)
                tk_oponente = c
                break
            else:
                print("aguardando oponente")
            sys.stdout.flush()