def is_happy(n):
    if n == 1:
        return True
    while n > 6:
        n = sum([int(i)**2 for i in str(n)])
        if n == 1:
            return True
    return False