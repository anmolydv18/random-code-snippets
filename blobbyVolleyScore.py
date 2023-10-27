T=int(input())

for q in range(T):
    N=int(input())  # number of turns
    S=input()
    alice=0
    bob=0
    flag=0

    for i in range(N):
                         ########flag 0 alice----flag 1 bob########
 
        if S[i]=='A' and flag==0:
            alice+=1
        elif S[i]=='A' and flag==1:
            flag=0
        elif S[i]=='B' and flag==0:
            flag=1
        elif S[i]=='B' and flag==1:
            bob+=1
        else:
            print("some error")
            break

    print(alice, bob)


        


      