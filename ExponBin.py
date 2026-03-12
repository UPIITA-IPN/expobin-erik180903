def exponenciacion_binaria(M, e, n):
    bits = bin(e)[2:]
    k = len(bits)
    if bits[0] == '1':
        C = M % n
    else:
        C = 1
    for i in range(1, k):
        ei = bits[i]
        C = (C ** 2) % n
        if ei == '1':
            C = (C * M) % n
    return C
M_val = 2
e_val = 1234
n_val = 789
resultado = exponenciacion_binaria(M_val, e_val, n_val)

print(f"{resultado}")
