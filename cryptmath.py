def gcd(a, b):
    """
    最大公約数(gratest common diviser)を求める
    """
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    """
    eucrid互除法を使ってモジュラーmにおけるaのモジュラー逆数を求める
    """
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
