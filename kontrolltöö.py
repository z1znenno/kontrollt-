# Ülesanne 1
      
# while True:
#     try:
#         num = int(input("Sisesta täisarv: "))
#         if num <= 9 and num >= 1:
#             for i in range(num):
#                 print(' Ä\t', end=' ')
#             print('')
#             for j in range(num):
#                 print("/ \\\t", end=' ')
#             print('')
#             for k in range(num):
#                 print("| |\t", end=' ')
#             print('')
#             for l in range(num):
#                 print(" __\t", end=' ')
#             print('')
#         else:
#             print("Viga: Sisestatud arv ei ole vahemikus 1 kuni 9.")
#     except :
#         print("Viga: Palun sisesta kehtiv täisarv.")

# Ülesanne 2

# import random

# summa = 0
# kesk_kuus = 0
# for aasta in range(12):
#     kulud = random.randint(5, 8)
#     for kuu in range(kulud): 
#         summa += round(random.randint(50, 100) * 1.11, 2) 
#     summa = round(summa, 2)
#     print('kuus oli: ' + str(summa) + '€')
#     kesk_kuus += summa
#     summa = 0
# print('keskmised kulud aastas on: ' + str(round(kesk_kuus/12, 2)) + '€')

# Ülesanne 3

# from random import randint

# pikk = randint(100, 500)
# lõik = 0
# print(f'Algselt on materjali pikkus {pikk} cm')
# while pikk > lõik:
#     lõik = randint(10, 50)
#     pikk -= lõik
#     print(f'Pikkus on veel {pikk} cm')
# print("Materjali ei ole piisavalt.")

# Ülesanne 4
# import random

# a = int(input("Sisesta täisarv vahemikus 1 kuni 10: "))
# b = int(input("Sisesta täisarv vahemikus 1 kuni 10: "))

# for i in range(b):
#     for u in range(a):
#         print(random.randint(10, 100), end='\t')
#     print('')
        
# Ülesanne 5
import random

tootaajad = int(input("Sisesta töötajate arv: "))
kas_pensionaar = random.randint(0,1)
