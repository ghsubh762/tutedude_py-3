def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    
    return fact

    '''
    # Using recursion:
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
    '''

n = int(input("Enter a number: "))
result = factorial(n)
print('Factorial of', n, 'is:', result)