import math

#Segundo punto
def listProduct(list):
    #list = [1,2,3,4]
    resultList = []
    if(len(list)>0):
        prodTotal = math.prod(list)
        for number in list:
            resultList.append(int(prodTotal/number))  
    return resultList

# creating an empty list
lst = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) # adding the element
      
print(lst)

print(listProduct(lst))