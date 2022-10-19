def maxi(numb1, numb2 , numb3):
    if numb1 >= numb2 and numb1 >= numb3:
        return numb1
    elif numb2 >= numb1 and numb2 >= numb3:
        return numb2
    else:
        return numb3

print(maxi(22 ,33 ,11))