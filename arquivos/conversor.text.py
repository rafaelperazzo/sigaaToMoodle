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
from funcoes import *
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

curso = str(config['DEFAULT']['curso'])
grupo = str(config['DEFAULT']['grupo'])
csv = str(config['DEFAULT']['csv'])
arquivo = str(config['DEFAULT']['arquivo'])
html = file2string(str(arquivo))
tabela = string2tabela(html,curso,"student",grupo)
tabela2csv(tabela,csv)
print("CSV exportado para: " + csv)