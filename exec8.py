# Δημιουργήστε ένα αρχείο με όλους τους πρώτους αριθμούς στο διάστημα 1->Ν.
# Το Ν να εισάγεται από το πληκτρολόγιο.
# Ο έλεγχος του εάν κάποιος αριθμός είναι πρώτος να γίνεται με συνάρτηση.

from mylib import get_pos_int, isPrime

primes = []
N = get_pos_int()

for i in range(2,N):
    if isPrime(i):
        primes.append(i)

print(f"Από 1 έως {N} βρέθηκαν {len(primes)} πρώτοι αριθμοί:", end=" ")

with open("primes.txt", "w") as file:
    for prime in primes:
        print(prime, end=" ")
        file.write(str(prime)+" ")
    file.write("\n")

k=8
print(f"\nO {k}ος πρώτος είναι το {primes[k-1]} ")