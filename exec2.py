# Να δημιουργηθεί μία λίστα από τους μοναδικούς συνδυασμούς δύο άλλων λιστών.

list1 = ["a", "b", "c"]
list2 = [1, 2, 3, 4]
list3 = []

for letter in list1:
    for num in list2:
        c = letter + str(num)
        list3.append(c)

print(list3)