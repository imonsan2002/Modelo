def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input('Dime el número para saber a que número de la sucesión de fibonacci pertenece:'))

print(fib(n))