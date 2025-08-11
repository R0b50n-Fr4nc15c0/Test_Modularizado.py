def soma(a:int,b:int)->int:
    if type(a) == str:
        if("." in a): a = float(a)
        else: a = int(a)
    if type(b) == str:
        if("." in b): b = float(b)
        else: b = int(b)

    a = round(a)
    b = round(b)

    return a + b