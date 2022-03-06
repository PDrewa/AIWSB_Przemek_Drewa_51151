# Assignment 1a
def prime(n):
    if n < 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


# Tests function prime:

shouldBeTrue = prime(3)
print("Result: " + str(shouldBeTrue))

shouldBeFalse = prime(4)
print("Result: " + str(shouldBeFalse))

shouldBeFalse = prime(49)
print("Result: " + str(shouldBeFalse))


# Assignment 1b
def select_primes(x):
    z = []
    for i in x:
        if prime(i):
            z.append(i)

    return z


# Tests function select_primes:
result = select_primes([3, 6, 11, 25, 19])
print("Result: " + str(result))
