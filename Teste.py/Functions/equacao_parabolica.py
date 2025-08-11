import cmath

def equacao_parabolica(a ,b ,c):
    d = (b**2) - (4*a*c)
    x0 = (-b + cmath.sqrt(d)) / (2*a)
    x1 = (-b - cmath.sqrt(d)) / (2*a)

    return x0, x1
