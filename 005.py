import math


# return dict of prime factor of n
def get_prime_factor_dict(n):
    prime = {}
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i not in prime:
                prime[i] = 0
            while n % i == 0:
                n /= i
                prime[i] += 1
    if len(prime) == 0:  # prime
        prime[n] = 1
    return prime


prime_dict = {}
for p in range(2, 21):
    m = get_prime_factor_dict(p)
    prime_dict.update(dict([(k, m[k]) for k in m
                            if k not in prime_dict or prime_dict[k] < m[k]]))
print reduce(lambda x, y: x * y, [pow(k, prime_dict[k]) for k in prime_dict])
