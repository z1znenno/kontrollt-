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
#             break
#         else:
#             print("Viga: Sisestatud arv ei ole vahemikus 1 kuni 9.")
#     except :
#         print("Viga: Palun sisesta kehtiv täisarv.")

# Ülesanne 2

# import random

# summa = 0
# kuus_summa = 0
# for aasta in range(12):
#     kulud = random.randint(5, 8)
#     for kuus in range(kulud): 
#         summa += round(random.randint(50, 100) * 1.11, 2) 
#     summa = round(summa, 2)
#     print('kuus oli: ' + str(summa) + '€')
#     kuus_summa += summa
#     summa = 0
# print('keskmised kulud aastas on: ' + str(round(kuus_summa/12, 2)) + '€')

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
# while True:
#     try:
#         a = int(input("Sisesta täisarv vahemikus 1 kuni 10: "))
#         b = int(input("Sisesta täisarv vahemikus 1 kuni 10: "))

#         for i in range(b):
#             for u in range(a):
#                 print(random.randint(10, 100), end='\t')
#             print('')
#             break
#     except:
#         print("Valed andmed")
        
# Ülesanne 5
# import random
# while True:
#     kui_palju = 0
#     a = random.randint(1400, 1700)
#     try:
#         tootaajad = int(input("Sisesta töötajate arv: "))
#         for i in range(tootaajad):
#             kas_pensionaar = random.randint(0,1)
#             palk = random.randint(1200, 3000)
#             if kas_pensionaar == 1 and palk>a:
#                 kui_palju += 1
#         print(f'Kokku on {kui_palju} töötajat, kes on pensionär ja kelle palk on suurem kui {a}€')
#         break
#     except:
#         print("Viga: Palun sisesta kehtiv täisarv.")
