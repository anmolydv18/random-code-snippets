len=int(input('enter the lenth'))
bred=int(input('enter the breadth'))
for i in range(0, bred):
    print("*\t"*len)
    print("\n")

print("\n\nhollow rectangle:\n\n")

for i in range(0,bred):
    if i == 0 or i ==(bred-1):
        print("*\t"*len)
    else:
        print("*\t","\t"*(len-2),"*")
    print("\n")
    
