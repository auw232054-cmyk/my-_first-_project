uniqe=[]
def numbers_list(a):
    #uniqe=[]
    for i in a:
        if i!=None:
            if type(i) !=str:
              if 0<=i<=100:
                uniqe.append(i)
              else:
                continue  
    return uniqe  
print(numbers_list([1,2,3,None,4,None,-2,-5,"hi"]))
print(uniqe)
