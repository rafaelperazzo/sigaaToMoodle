#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
sigaa2Moodle: Exportador de usuários SIGAA para Moodle
    Copyright (C) 2020  Rafael Perazzo Barbosa Mota

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
from bs4 import BeautifulSoup
import csv

def get_first_name(fullname):
    firstname = ''
    try:
        firstname = fullname.split()[0] 
    except Exception as e:
        print (str(e))
    return firstname

def get_last_name(fullname):
    lastname = ''
    try:
        index=0
        for part in fullname.split():
            if index > 0:
                if index > 1:
                    lastname += ' ' 
                lastname +=  part
            index += 1
    except Exception as e:
            print (str(e))
    return lastname

def mostrar_tabela(tabela):
    for i in range(0,len(tabela),1):
        print (tabela[i])
            
def ajustar_tabela(tabela):
    final = []
    for i in range(0,len(tabela),1):
        if len(tabela[i])>0:
            final.append(tabela[i])
    return (final)

def file2string(arquivo):
    html = ''
    f = open(arquivo,'r',encoding = "ISO-8859-1")
    j = 0
    for line in f:
        if line!='':
            if ("<table class=\"participantes\">" in line) and (j==0):
                line = line.replace("participantes","professores")
                j = j + 1
            
        html = html + line + '\n'
    return (html)

def string2tabela(html,curso,papel,grupo):
    soup = BeautifulSoup(html,"html.parser")
    table = soup.find("table", attrs={"class":"participantes"})

    rows = table.findAll('tr')
    tabela = []
    linha1 = ['firstname','lastname','username','email','course1','role1','group1']
    tabela.append(linha1)

    for tr in rows:
        cols = tr.findAll('td')
    
        for td in cols:
            ems = td.findAll('em')
            nomes = td.findAll('strong')
            linha = []
            for nome in nomes:
                sNome = str(nome)
                sNome = sNome.replace("\t","")
                sNome = sNome.replace("\n","")
                sNome = sNome.replace("<strong>","")
                posicaoInicial = sNome.find("<a")
                posicaoFinal = sNome.find("</strong>")+9
                sNome = sNome[:posicaoInicial-posicaoFinal]
                #print(get_first_name(sNome) + " " + get_last_name(sNome))
                linha.append(get_first_name(sNome))
                #linha.append(",")
                linha.append(get_last_name(sNome))
            i = 0
            for em in ems:
                #print (i)
                dados = str(em)
                dados = dados.replace("<em>","")
                dados = dados.replace("</em>","")
                if i==1 or i==3:
                    linha.append(dados)
                    if i==3:
                        linha.append(curso)
                        linha.append(papel)
                        linha.append(grupo)
                '''elif i>3:
                    linha.append(curso)
                    linha.append(papel)
                    linha.append(grupo)'''
                i = i + 1
        
            tabela.append(linha)
    
    tabela = ajustar_tabela(tabela)
    return (tabela)


def tabela2csv(tabela,arquivo):
    with open(arquivo, "w") as f:
        writer = csv.writer(f)
        writer.writerows(tabela)

'''
ENTRADA: 
    - Arquivo html dos participantes
    - Arquivo csv de saida
    - id do curso
    - Papel do participante
    - Grupo do participante

html = file2string("participantes.em0006.html")
tabela = string2tabela(html,"progcomp2017.2","student","eci0007.1")
tabela2csv(tabela,"participantes.csv")
'''


