import uuid
import random

def cr_200_code():
    st= 'qwertyuiopasdfghjklzxcvbnm0123456789'
    arr = []
    for i in range(0,200):
        y = ''
        for j in range(0,10):
             y += random.choice(st)
        if y not in arr:
            arr.append(y)
    return arr