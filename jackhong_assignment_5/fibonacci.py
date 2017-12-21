def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print('The 21st fibonacci number is: {:d}'.format(fibonacci(21)))

# Used to check my code
#for i in range(1,25):
#    print(fibonacci(i))
