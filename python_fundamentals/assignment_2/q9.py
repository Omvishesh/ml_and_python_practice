def is_prime(n):
    if n == 2:
        return True
    else:
        for i in range(2, n):
            div = n % i 
            if div == 0:
                return False
        return True

result = is_prime(5)
print(result)                
                