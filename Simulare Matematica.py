# importam random penru generarea unui numar aleatoriu
import random

#probabilitatea ca un utilaj care are mai putin de 5 ani/mai mult de 5 ani sa se strice
#probabilitate teoretica

#x= varsta, y=numar aleator
def probabilitateTractor(x,y):
    if x<5:
        if y<0.15:
            return 1
        else:
            return 0
    else:
        if y<0.25:
            return 1
        else:
            return 0    

 #x= varsta, y=numar aleator
def probabilitateTractorFendt(x,y):
    if x<5:
        if y<0.15:
            return 1
        else:
            return 0
    else:
        if y<0.25:
            return 1
        else:
            return 0  

#x= varsta, y=numar aleator
def probabilitateDrujba(x,y):
    if x<5:
        if y<0.15:
            return 1
        else:
            return 0
    else:
        if y<0.30:
            return 1
        else:
            return 0  
        
#x= varsta, y=numar aleator
def probabilitateGater(x,y):
    if x<5:
        if y<0.1:
            return 1
        else:
            return 0
    else:
        if y<0.30:
            return 1
        else:
            return 0  
        

 #x= varsta, y=numar aleator       
def probabilitateMacara(x,y):
    if x<5:
        if y<0.15:
            return 1
        else:
            return 0
    else:
        if y<0.25:
            return 1
        else:
            return 0  
        
 #x= varsta, y=numar aleator       
def probabilitateIfron(x,y):
    if x<5:
        if y<0.1:
            return 1
        else:
            return 0
    else:
        if y<0.25:
            return 1
        else:
            return 0  
        
'''
n=random.random()
print(n)
print(probabilitateTractor(7,n))
print(probabilitateMacara(n))
'''
#in urma discutiilor cu firma, s-a constatat ca toate utilajele au mai mult de 5 ani, 
# deci pentru nu a modifica codul, voi initializa variabila x cu 5
x=5

#suma costurilor daca se face revizia si intretinere anuala
sumaRevizie=7000

#de cate ori se doreste realizarea simularii, cate iteratii
nrIterat=int(input("De cate ori doriti sa se realizeze simularea?"))
#variabila contor, numara de cate ori situatia ITP este benefica fata de cealalta
k=0

for i in range(0,nrIterat):
    #suma costurilor pe un an daca nu se face revizia tehnica, initializare
    suma=0
    for i in range(1,366):
            suma=suma+probabilitateDrujba(x,random.random())*83
            +probabilitateDrujba(x,random.random())*83+probabilitateTractor(x,random.random())*477
            +probabilitateTractorFendt(x,random.random())*500+probabilitateGater(x,random.random())*125
            +probabilitateIfron(x,random.random())*170+probabilitateMacara(x,random.random())*230
    if suma>sumaRevizie:
        k=k+1

print(f"In urma simularii, situatia in care se realizeaza revizia tehnica anuala a iesit mai buna fata de situatia in care se asteapta defectarea apoi se realizeaza reparatia de {k} din {nrIterat} cazuri totale ")


