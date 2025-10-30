#Ülesanne 1

# while True:
#     try:
#         num = int(input("Sisesta täisarv: "))
#         if num <= 9 and num >= 1:
#             for i in range(num):
#                 print(  " Ä\n" 
#                        "/ \\\n"
#                        "| |\n"
#                         " __"
#                      )
#                 print('')
#         else:
#             print("Viga: Sisestatud arv ei ole vahemikus 1 kuni 9.")
#     except :
#         print("Viga: Palun sisesta kehtiv täisarv.")

#Ülesanne 2

import random

x = round(random.uniform(1, 20), 2)  # от 1 до 5, два знака после запятой
print(x)

for kuu in range(random.randint(5,8)):
    pass