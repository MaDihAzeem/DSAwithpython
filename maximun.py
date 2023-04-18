def max_of_two(x,):
    if x > y :
        return x
    return y
def max_of_three(x,y,a):
   return max_of_two(x , max_of_two(y,a))
def max_of_four(x,y,a,t):
    return max_of_two(x,max_of_three(y,a,t))
def max_of_five(x,y,a,t,f):
    return max_of_two(x,max_of_four(y,a,t,f))
def max_of_six(x,y,a,t,f,v):
    return max_of_three(x,y,max_of_four(a,t,f,v))
print (max_of_two(3,10))
print (max_of_three(4,8,9))
print (max_of_four(30,20,70,10))
print (max_of_five(20,12,56,45,78)) 
print(max_of_six(23,70,100,24,45,90))



    


