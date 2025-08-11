def produto(a:int, b:int)->float:
    if type(a) == str:
        if("." in a): a = float(a)
        else: a = int(a)
    if type(b) == str:
        if("." in b): b = float(b)
        else: b = int(b)

    return a * b