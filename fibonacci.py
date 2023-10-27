# f0=0 f1=1 f2=1 f3=2 f4=3 f5=5
# fn=f(n-1)+f(n-2)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print( fib(35))