from datetime import datetime

def has_friday_13(month,year):
    dt = datetime(year,month,13)
    dow=dt.weekday()

    if dow == 4:
        print ("True") 
    else:
        print ("False") 
    

has_friday_13(3, 2020)
has_friday_13(10, 2017) 
has_friday_13(1, 1985)


def pluralize(listy):
    sety=set(listy)

    resulty=[]
    
    for s in sety:
        if listy.count(s) > 1:
            resulty.append(s + 's')
        else:
            resulty.append(s)
    print (resulty)    


pluralize(["cow", "pig", "cow", "cow"])
pluralize(["chair", "pencil", "arm"])


def pentagonal(num):
    pentagonalnum=0

    for i in range (1,num+1):

        if i == 1:
            pentagonalnum=1
        else:
            pentagonalnum+= (i-1)*5
    print( pentagonalnum)

    
    
pentagonal(1) 
pentagonal(2)
pentagonal(0)
pentagonal(8)



