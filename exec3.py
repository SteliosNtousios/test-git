# Να γραφεί πρόγραμμα που να ελέγχει εάν ένας θετικός ακέραιος είναι πρώτος αριθμός.

def get_pos_int():
    while True:
        try:
            num = int(input("Δώσε έναν θετικό ακέραιο: "))
            if num > 0:
                return num
            else:
                print("Θετικό ακέραιο παρακαλώ: ") 
        except ValueError:
                print("Θετικό ακέραιο παρακαλώ: ")

n = get_pos_int()
prime = True

for i in range(2, int(n+1/2)):
    if n % i == 0:
        prime = False
        print(f"Ο {n} είναι σύνθετος. Διαιρείται με το {i}.")
        exit()

print(f"Ο {n} είναι πρώτος.")