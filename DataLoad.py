"""
Created on Monday March 24 16:09:19 2025

@author: ashtondunn
"""

import pandas as pd
f = open("INSERT_FILE.dat", "w")
fin = " ; \n"
# READ SHEETS
p = pd.read_excel("INSERT_FILE.xlsx", "Prices")
pen = pd.read_excel("INSERT_FILE.xlsx", "Penalties")
d = pd.read_excel("INSERT_FILE.xlsx", "Forecast")
LT = pd.read_excel("INSERT_FILE.xlsx", "LowerTrInt")
UT = pd.read_excel("INSERT_FILE.xlsx", "UpperTrInt")
LB = pd.read_excel("INSERT_FILE.xlsx", "LowerBoundCap")
UB = pd.read_excel("INSERT_FILE.xlsx", "UpperBoundCap")

# PARAMETERS

f.write("param p:= \n")
p.to_csv(f, sep = " ", header = False, index= False)
f.write(fin)

f.write("param pen:= \n")
pen.to_csv(f, sep = " ", header = False, index= False)
f.write(fin)

f.write("param d:= \n")
d.to_csv(f, sep = " ", header = False, index= False)
f.write(fin)

f.write("param LT:= \n")
LT.to_csv(f, sep = " ", header = False, index= False)
f.write(fin)

f.write("param UT:= \n")
UT.to_csv(f, sep = " ", header = False, index= False)
f.write(fin)

f.write("param LB:= \n")
LB.to_csv(f, sep = " ", header = False, index= False)
f.write(fin)

f.write("param UB:= \n")
UB.to_csv(f, sep = " ", header = False, index= False)
f.write(fin)

f.close()