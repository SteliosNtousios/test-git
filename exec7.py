# Να γράψετε μία αναδρομική συνάρτηση η οποία να υπολογίζει
# τον μέγιστο κοινό διαιρέτη δύο ακεραίων από τον τύπο: 
# ΜΚΔ(x,y)={ x, για y=0  ή
#            @ΜΚΔ(y,υπόλοιπο της διαίρεσης χ δια y),για x≥y και y>0)
# (και το αντίστοιχο πρόγραμμα που την καλεί).

def mkd(x,y):
    if y == 0:
        return x
    else:
        return mkd(y,x%y)

def get_int(ask):
    while True:
        try:
            num = int(input(ask))
            if num >= 0:
                return num
            else:
                print("Θετικό ακέραιο παρακαλώ: ") 
        except ValueError:
                print("Θετικό ακέραιο παρακαλώ: ")

x = int(get_int("\nΔώσε έναν θετικό ακέραιο: "))
y = int(get_int("Δώσε έναν ακόμη: "))

print(f"\nΜΚΔ({x},{y}) = {mkd(max(x,y),min(x,y))}\n")