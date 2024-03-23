# Nα γραφεί πρόγραμμα που να αποθηκεύει 
# και στην συνέχεια εκτυπώνει 
# όλους τους πρώτους αριθμούς σε μία λίστα από 1 μέχρι n.
# Τέλος, εκτυπώνει και πόσοι πρώτοι αριθμοί βρέθηκαν.

def get_max_num():
    while True:
        try:
            num = int(input("Δώσε έναν θετικό ακέραιο: "))
            if num > 0:
                return num
            else:
                print("Θετικό ακέραιο παρακαλώ: ") 
        except ValueError:
                print("Θετικό ακέραιο παρακαλώ: ")

n = get_max_num()
list_of_primes = []

for i in range(1,n):
    for j in range(2, int(i+1/2)):
        if i % j == 0:
            prime = False
            break
        else:
            prime = True
    if prime:
        list_of_primes.append(i)
    
print(f"Μέχρι το {n} βρέθηκαν {len(list_of_primes)} πρώτοι αριθμοί.")
print(list_of_primes)