def sieve_of_eratosthenes(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False

    p = 2
    while p * p <= n:
        if isPrime[p]:
            for i in range(p * 2, n + 1, p):
                isPrime[i] = False
        p += 1

    return isPrime

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_super_prime(num):
    if is_prime(num):
        while num > 0:
            digit = num % 10
            if not is_prime(digit):
                return False
            num //= 10
        return True
    return False

def superPrimes(n):
    isPrime = sieve_of_eratosthenes(n)
    
    super_primes = [p for p in range(2, n + 1) if isPrime[p] and is_super_prime(p)]

    return super_primes

n = 241
print("Super-Primes less than or equal to", n, "are:", superPrimes(n))
