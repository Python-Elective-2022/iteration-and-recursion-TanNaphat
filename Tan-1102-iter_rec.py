'''
1st program iterative way.
Define the function iterative power
set the result equal to 1
for every i in the range of the exponent:
    result is the product of itself and the base
return the result.

print the iterative_power of whatever base and exponent you want.
'''

def iterative_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    result = 1
    for i in range(exp):
        result *= base
    return result

print(iterative_power(6, 3))
#print(iterative_power(2, 9))
#print(iterative_power(3, 7))
'''
for i in range (0, 5):
    n = iterative_power(3.3, i)
    print("n", n)
'''

'''
2nd program, recursive way
define the function recursive_power with the 1st variable being the base and the second being the exponent.
If the exponent equals to 0:
    return 1 
else:
    return the base times the result of the function with the original base and the exponent subtracted by 1.

print the function with the base and exponent you want.
'''
def recursive_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recursive_power(base, exp - 1)

print(recursive_power(5, 3))
#print(recursive_power(7, 2))
#print(recursive_power(9, 7))
'''
for i in range (0, 5):
    n = recursive_power(3.3, i)
    print("n", n)
'''