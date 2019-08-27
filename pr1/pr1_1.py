print("otwarcie pliku /home/zgm/Pulpit/Bogusia/marked_dup_metrics_N.txt do odczytu")

with open('/home/zgm/Pulpit/Bogusia/marked_dup_metrics_N.txt') as f:
    start_reading = False
    read_lines_counter = 0
    for line in f.readlines():
        if line.startswith("## METRICS CLASS"):
            print('ok')
            start_reading = True
        if start_reading and read_lines_counter <= 2:

            if read_lines_counter == 1:
                print("Pierwsza linia do zapisu")
                klucz = line.replace('\n', '').split('\t')

            if read_lines_counter == 2:
                print("druga linia do zapisu")
                wartosc = line.replace('\n', '').split('\t')

            read_lines_counter = read_lines_counter + 1

print("klucze=", klucz)
print("")
print("wartosci=", wartosc)
print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
slownik = {}

for i in range(0, len(klucz), 1):
    slownik[klucz[i]] = wartosc[i]
    print(klucz[i], wartosc[i])
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

print('')
print(slownik.items())

print("///////////////////////////////////////////")

print("wybranie danych do zapisu")
ilo=int(slownik['READ_PAIR_DUPLICATES'])+int(slownik['UNPAIRED_READ_DUPLICATES'])
proc=float(slownik['PERCENT_DUPLICATION'].replace(',','.'))

print("proc przed przemnozeniem")
print (proc)
proc=round(proc*100, 4)
print("proc po przemnozeniu")
print(proc)

print("///////////////////////////////////////////")
print("zapis do pliku")

pli=open("/home/zgm/Pulpit/Bogusia/raport.csv",'a')
pli.write("raport z marked_dup_metrics_N.txt,\n")
pli.write("Duplikatow jest, ")
pli.write(str(ilo))
pli.write(",\n")
pli.write("Procentowy udznial duplikatow,")
pli.write(str(proc))
pli.write(",\n")
pli.close()

print("zapisano do pliku")








"""
plik = open('/home/zgm/Pulpit/Bogusia/marked_dup_metrics_T.txt')

lini = plik.readline()

print("*******************************************")
while lini != '':

    ini = lini.split()

    if ini[0:3] == ['##', 'METRICS', 'CLASS']:
        print('ok')
        a = plik.readline().replace('\n','')
        k = a.split('\t')
        b = plik.readline().replace('\n','')
        v = b.split('\t')
        print("k=", k)
        print("")
        print("v=", v)
        print("")
        slownik={}
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        #slownik=slownik.fromkeys(k,0)
        for i in range(0, len(k), 1):
            slownik[k[i]]=v[i]
            print(k[i], v[i])
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print('')
        print(slownik.items())

        break
    lini = plik.readline()
    ini=[]
plik.close()

print("///////////////////////////////////////////")

print("wybranie danych do zapisu")
ilo=int(slownik['READ_PAIR_DUPLICATES'])+int(slownik['UNPAIRED_READ_DUPLICATES'])
proc=float(slownik['PERCENT_DUPLICATION'].replace(',','.'))

print("proc przed przemnozeniem")
print (proc)
proc=proc*100
print("proc po przemnozeniu")
print(proc * 100)

print("///////////////////////////////////////////")
print("zapis do pliku")

pli=open("/home/zgm/Pulpit/Bogusia/raport.csv",'a')
pli.write("raport z marked_dup_metrics_T.txt,\n")
pli.write("Duplikatow jest, ")
pli.write(str(ilo))
pli.write(",\n")
pli.write("Procentowy udznial duplikatow,")
pli.write(str(proc))
pli.write(",\n")
pli.close()

print("zapisano do pliku")
"""