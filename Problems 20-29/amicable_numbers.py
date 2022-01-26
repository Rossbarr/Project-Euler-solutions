def proper_divisors(n: int):
    divisors = [1]
    i = 1
    while i*i <= n:
        i += 1
        if n % i == 0:
            divisors.append(i)
            if n/i != i:
                divisors.append(int(n/i))
    return divisors

def amicable_numbers(n: int = 10000):
    i = 0
    amicable_numbers = []
    while i < n:
        i += 1
        j = sum(proper_divisors(i))
        if i < j and sum(proper_divisors(j)) == i:
            amicable_numbers.append([i, j])
    return amicable_numbers

amicable_numbers = amicable_numbers()
print(amicable_numbers)

summ = 0
for pair in amicable_numbers:
    summ += sum(pair)

print(summ)
