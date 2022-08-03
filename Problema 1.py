#Primer punto
def xepelinNumber(number):
    if(number %3 ==0 and number %5==0):
        print("Xepelin")
    elif(number %3 ==0):
        print("Xepe")
    elif(number %5==0):
        print("Lin")

number = input("Ingrese un numero ")
xepelinNumber(int(number))