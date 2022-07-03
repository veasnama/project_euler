# If the complete prime factorization is sought, this is the brute-force algorithm:
# This function copied from stackoverflow and then learn from it.
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
result = prime_factors(600851475143)
print(result)
# I do it myself. Since i used to do it multiple times. 
current_largest_number = result[0]

for i in result:
    if i > current_largest_number:
        current_largest_number = i
    else:
        current_largest_number = current_largest_number
print(f"The largeest prime factors =  {current_largest_number}")

