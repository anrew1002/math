def __factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


def Exponential(x, n):
    output = 1
    for i in range(1, n+1):
        output += x**i / __factorial(i)
    return output


def sin_f(x, n):
    output = 0
    for i in range(n+1):
        output += ((-1)**i * x**(2*i+1)) / __factorial(2*i+1)
    return output


def cos_f(x, n):
    output = 0
    for i in range(n+1):
        output += ((-1)**i * x**(2*i)) / __factorial(2*i)
    return output


def arcsin_f(x, n):
    output = 0
    for i in range(n+1):
        output += __factorial(2*i) * x**(2*i+1) / \
            (4**i * (__factorial(i)**2)*(2*i+1))
    return output


def arccos_f(x, n):
    pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233
    output = 0
    for i in range(n+1):
        output += __factorial(2*i) * x**(2*i+1) / \
            (4**i * (__factorial(i)**2)*(2*i+1))
    return pi/2 - output
