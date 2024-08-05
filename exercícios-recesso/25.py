a, b = 0, 1
while a <= 2000:
    print(a)
    next_fib = a + b
    a = b
    b = next_fib
