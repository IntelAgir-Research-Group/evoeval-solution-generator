def prime_cipher(s: str):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def nth_prime(n):
        count = 0
        num = 2
        while True:
            if is_prime(num):
                count += 1
                if count == n:
                    return num
            num += 1
    primes = {chr(97 + i): nth_prime(i) for i in range(26)}
    return ''.join((str(primes[ch]) if ch in primes else ch for ch in s))