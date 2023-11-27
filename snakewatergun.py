import random
comp= random.randint(0,2)
you=int(input("press 0 for snake, 1 for water, 2 for gun\n"))
def check(comp,you):
    if comp ==you:
        return 0
    elif comp ==0 and you ==1:
        return -1
    elif comp ==1 and you ==2:
        return -1
    elif comp ==2 and you ==0:
        return -1
    return 1
    
score=check(comp,you)
print("\nyou:",you )
print("computer:", comp)
if score==-1:
    print("computer wins")
elif score==1:
    print("you win")
else:
    print("draw")

