l = []
print(f'Listi algseis: {l}')
while True:
    print(
    '1. Lisa elmente\n'
    '2. Lisa elemente pos-le\n'
    '3. Eemalda elemente pos järgi\n'
    '4. Eemalda element nime järgi\n'
    '5. Näita list\n'
    '6. Lisa listile teise listi elementid\n'
    '7. Sorteeri tähestiku järgi\n'
    '8. Ümber keerata list\n'
    '9. Eemalda kõik elemente\n'  
    )
    while True:
        try:
            valik = int(input('Valik: '))
            break
        except:
            print('Arvud: 1... n')
    print('Töö listiga...')
    if valik == 1:
        while True:
            try:
                i = int(input('Mitu elementi soovid lisada? '))
                if i > 0:
                    break
                else:
                    print('Sisestage arvud rohkem kui 0')
            except:
                print('Palun sisesta täisarv.')
        for element_id in range(i):
            element = input(f'Sisesta {element_id + 1}. element: ')
            l.append(element)
        print(f'Uuendatud list: {l}')
    elif valik == 2:
        while True:
            try:
                pos = int(input(f'Sisesta positsioon, kuhu soovid lisada (0 - {len(l)}): '))
                if 0 <= pos <= len(l):
                    break
                else:
                    print(f'Sisesta positsioon vahemikus 0 kuni {len(l)}')
            except:
                print('Palun sisesta täisarv.')
        element = input('Sisesta element, mida soovid lisada: ')
        l.insert(pos, element)
        print(f'Uuendatud list: {l}')
    elif valik == 3 :
        while True:
            try:
                pos = int(input(f'Sisesta positsioon, kust soovid eemaldada (0 - {len(l)-1}): '))
                if 0 <= pos < len(l) - 1:
                    break
                else:
                    print(f'Sisesta positsioon vahemikus 0 kuni {len(l)-1}')
            except:
                print('Palun sisesta täisarv.')
        removed_element = l.pop(pos)
        print(f'Eemaldatud element: {removed_element}')
        print(f'Uuendatud list: {l}')
    elif valik == 4:
        element = input('Sisesta element, mida soovid eemaldada: ')
        mitu = l.count(element)
        if mitu == 0:
            print('Elementi ei leitud')
        else:
            for e in range(mitu):
                print(f'Eemaldatud element "{element}" {l.index(element)} positsioonilt.')
                l.remove(element)
            print(f'Eemaldatud {mitu} elementi!')
    elif valik == 5:
        print(f'Listi sisu: {l}')
    elif valik == 6:
        element = list(input('Sisetage sõnu, mille tähed soovite lisada listile: '))
        l.extend(element)
        print(f'Uuendatud list: {l}')
    elif valik == 7:
        print('Sorteerin listi...')
        l.sort()
        print(f'Sorteeritud list: {l}')
    elif valik == 8:
        print(f'Pööratud list: {l.reverse()}')
    elif valik ==9:
        print('Eemaldan kõik elemendid listist...')
        l.clear()
        print('Kõik elemendid on eemaldatud.')