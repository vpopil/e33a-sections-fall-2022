
def pow(x, y):
    z = 1

    while abs(y) > 0:
        if y < 0:
            z /= x
            y += 1
        else:  # when y is positive
            z *= x
            y -= 1
    return z



assert pow(2,5) == 32

assert pow(2,-2) == 0.25

#assert pow(2,10) == 1024
