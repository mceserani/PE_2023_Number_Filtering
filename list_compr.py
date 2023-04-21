"""Esercitazione sulla list comprehension"""

import random

N = int(input("Inserisci la dimensione della lista: "))

num = [random.randint(1, 1000) for i in range(N)]

even = [i for i in num if i % 2 == 0]

div_3 = [i for i in num if i % 3 == 0]

even_div_3 = [i for i in num if i % 2 == 0 and i % 3 == 0]

square = [i**2 for i in num]

cube = [i**3 for i in num]


print("Lista di numeri casuali: ", num)
print("Numeri pari: ", even)
print("Numeri divisibili per 3: ", div_3)
print("Numeri pari e divisibili per 3: ", even_div_3)
print("Quadrati: ", square)
print("Cubi: ", cube)


