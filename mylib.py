import sys

# Θετικό ακέραιο από τον χρήστη
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
                
# Εμαφανίσεις χαρακτήρα σε μια γραμματοσειρά
def timesOf(c, string):
    times = 0
    for i in string:
        if c == i:
            times +=1
    return times

# ΜΚΔ δύο ακεραίων αριθμών x,y
def mkd(x,y):
    a=max(abs(x),abs(y))
    b=min(abs(x),abs(y))
    if b == 0:
        return a
    else:
        return mkd(b,a%b)

#Είναι πρώτος;
def isPrime(n):
    prime = True
    for i in range(2, int(n+1/2)):
        if n % i == 0:
            prime = False
    return prime

#Μιγαδικό από τον χρήστη
def getComplex():
    complex_number_str = input("Δώσε έναν μιγαδικό στη μορφή α+βj: ")
    try:
        return complex(complex_number_str)
    except ValueError:
        print("Μη αποδεκτή μορφή.")
