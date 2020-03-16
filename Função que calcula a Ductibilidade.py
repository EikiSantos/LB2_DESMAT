# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 21:00:59 2020

@author: eikis
"""

def calcula_duct(Lo, Lf):
    EL = ((Lf - Lo)/Lo) * 100
    return EL

duct1 = calcula_duct(50, 59.4)
duct2 = calcula_duct(50, 65.1)
duct3 = calcula_duct(50, 58.9)

Dic = {}

Dic["Ductibilidade do Material 1"] = duct1
Dic["Ductibilidade do Material 2"] = duct2
Dic["Ductibilidade do Material 3"] = duct3

print(Dic)