
def atbash(stringy):
    bigAlpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    smallalpha='abcdefghijklmnopqrstuvwxyz'

    resultss=''

    for s in stringy:
        if s in bigAlpha:
            resultss+= bigAlpha[25 - bigAlpha.index(s)]
        elif s in smallalpha:
            resultss+= smallalpha[25 - smallalpha.index(s)]
        else:
            resultss+=s
    print(resultss)


atbash("apple")
atbash("Hello world!")
atbash("Christmas is the 25th of December")


            
        

           
               
