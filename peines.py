
import xlrd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl

filePath = r'C:\Users\apb19\Documents\PAE Peines.xlsx'
openFile = xlrd.open_workbook(filePath)
sheet = openFile.sheet_by_name("59")

#print("Num de filas", sheet.nrows)
#print("Num de columnas",sheet.ncols)

def getZ(number):
    if number == 1:
     Z = sheet.col_values(2,415,616)
     print(Z)
    elif number == 2:
     Z = sheet.col_values(9,415,616) 
    
    elif number == 3:
     Z = sheet.col_values(15,415,616)
    else:
     print ("Vaya puta mierda de numero macho")

    return Z
         

def getPh(number):
    if number == 1:
     Ph = sheet.col_values(3,415,616)
     
    elif number == 2:
     Ph = sheet.col_values(10,415,616) 
    
    elif number == 3:
     Ph = sheet.col_values(16,415,616)
    else:
     print ("Vaya puta mierda de numero macho")
        
    return Ph 

def getZ1(number):
    if number == 1:
     Z1 = sheet.col_values(4,415,616)
    elif number == 2:
     Z1 = sheet.col_values(11,415,616) 
    
    elif number == 3:
     Z1 = sheet.col_values(17,415,616)
    else:
        print ("Vaya puta mierda de numero macho")
        
    return Z1

def getZ2(number):
    if number == 1:
     Z2 = sheet.col_values(5,415,616)
    elif number == 2:
     Z2 = sheet.col_values(12,415,616) 
    
    elif number == 3:
     Z2 = sheet.col_values(18,415,616)
    else:
        print ("Vaya puta mierda de numero macho")
        
    return Z2 

def getF(number):
    if number == 1:
     f = sheet.col_values(1,415,616)
     
    elif number == 2:
     f = sheet.col_values(8,415,616) 
    
    elif number == 3:
     f = sheet.col_values(14,415,616)
    else:
        print ("Vaya puta mierda de numero macho")
        
    return f 

def getC(number):
    if number == 1:
     C = sheet.col_values(6,415,616)
     
    elif number == 2:
     C = sheet.col_values(13,415,616) 
    
    elif number == 3:
     C = sheet.col_values(19,415,616)
    else:
        print ("Vaya puta mierda de numero macho")
        
    return C 
   
#fa = sheet.col_values(8,415,616)
#Za = sheet.col_values(9,415,616)
#Pha = sheet.col_values(10,415,616)
#Z1a = sheet.col_values(11,415,616)
#Z2a = sheet.col_values(12,415,616)
#Ca = sheet.col_values(13,415,616)

#faa = sheet.col_values(14,415,616)
#Zaa = sheet.col_values(15,415,616)
#Phaa = sheet.col_values(16,415,616)
#Z1aa = sheet.col_values(17,415,616)
#Z2aa = sheet.col_values(18,415,616)
#Caa = sheet.col_values(19,415,616)


#print(f)
#for i in range(sheet.nrows):
 #               print(sheet.cell_value(i,1),"    ",sheet.cell_value(i,2))