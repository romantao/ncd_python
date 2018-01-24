# Change nameplaces for Phylip with species Real Name 
# Last modified by: 
# Romulo Antao
# 4 January 2018

import sys

f = open('outtree','r')

data = f.read()
data_mod = data.replace('A'*9,"Baboon")
data_mod = data_mod.replace('B'*9,"Brown Bear")
data_mod = data_mod.replace('C'*9,"Cat")
data_mod = data_mod.replace('D'*9,"Chimpanzee")
data_mod = data_mod.replace('E'*9,"Dog")
data_mod = data_mod.replace('F'*9,"Donkey")
data_mod = data_mod.replace('G'*9,"Fat Dormouse")
data_mod = data_mod.replace('H'*9,"Gorilla")
data_mod = data_mod.replace('I'*9,"Horse")
data_mod = data_mod.replace('J'*9,"Human")
data_mod = data_mod.replace('K'*9,"Indian Rhinoceros")
data_mod = data_mod.replace('L'*9,"Mouse")
data_mod = data_mod.replace('M'*9,"Orangutan")
data_mod = data_mod.replace('N'*9,"Polar Bear")
data_mod = data_mod.replace('O'*9,"Rabbit")
data_mod = data_mod.replace('P'*9,"Rat")
data_mod = data_mod.replace('Q'*9,"Squirrel")
data_mod = data_mod.replace('R'*9,"White Rhinoceros")

f = open('outtree','w')
f.write(data_mod)
f.close()
