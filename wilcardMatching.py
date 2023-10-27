t=int(input())

for q in range(t):
    X=input()
    Y= input()

    flag="no"
    i=0
# loop for checking string values starts here
    while i<len(X):
        if X[i]==Y[i]:
            flag="yes"
            i+=1
        elif X[i]=="?" or Y[i]=="?":
            flag="yes"
            i+=1
        elif X[i]=="?" and Y[i]=="?":
            flag="yes"
            i+=1
        else:
            flag="no"
            break
#  loop ends here   # 
    print(flag)


