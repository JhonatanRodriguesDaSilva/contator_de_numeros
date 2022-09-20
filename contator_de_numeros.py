def contador (n: int) -> int:
    
    if n == 0:
        return 0
    else:
        print(n)
        return n - contador(n - 1)

contador(int(input('Digite um numero inteiro: ')))