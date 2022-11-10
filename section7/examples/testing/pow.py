# def pow(x, y):
#     z = 1
#     while y > 0:
#         z *= x
#         y -= 1

#     return z



import time

def pow(x, y):
    z = 1
    time.sleep(1)
    while abs(y) > 0:
        
        if y < 0:
            z /= x
            y += 1
        else:
            z *= x
            y -= 1
    return z



















