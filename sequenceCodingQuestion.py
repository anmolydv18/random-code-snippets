T=int(input())


def swap(u,i,newstr):
    if u[i]=='0' and u[i+1]=='0':
        newstr.append("A")
    elif u[i]=='0' and u[i+1]=='1':
        newstr.append("T")
    elif u[i]=='1' and u[i+1]=='0':
        newstr.append("C")
    elif u[i]=='1' and u[i+1]=='1':
        newstr.append("G")
    return newstr   
       


for p in range(T): #run a loop for number of test cases
    strLen=int(input())  #input length of string
    u=input() #input string
    newstr=[]
    #print(u)
     #traverse string
    i=0
    while i < strLen:
        swap(u,i,newstr)
        i+=2
    print("".join(newstr))

