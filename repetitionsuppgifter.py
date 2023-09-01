
#1. Skriv ett program som tar in en mening från användaren och räkna sedan antalet vokaler i meningen. Skriv ut antalet.

str=input(print("Skriv ett ord: "))

def vokaler(ch):
    if ch == 'a' or \
       ch == 'A' or \
       ch == 'o' or \
       ch == 'O' or \
       ch == 'u' or \
       ch == 'U' or \
       ch == 'å' or \
       ch == 'Å' or \
       ch =='e' or \
       ch =='E' or \
       ch == 'i' or \
       ch == 'I' or \
       ch =='y' or \
       ch =='Y' or \
       ch =='ä' or \
       ch =='Ä' or \
       ch =='ö' or \
       ch == 'Ö':
        return True
    return False


def räkna_vokaler(str):
    i = 0
    for ch in str:
        if vokaler(ch):
            i = i + 1
    return i

antal_vokaler = räkna_vokaler(str)
print("i denna text/ord" ,str, "är det så här många vokaler",antal_vokaler)




#2. Skriv ett program som utför en bubbelsortering på en lista med värden. (https://en.wikipedia.org/wiki/Bubble_sort)


#3. Skriv ett program som kontrollerar ifall ett ord är en palindrom, dvs är likadant framlänges som baklänges.
#4. Skapa Eratosthenes såll. (https://sv.wikipedia.org/wiki/Eratosthenes_s%C3%A5ll)
#5. Lösenordscheck - be användaren mata in ett lösenord och kontrollera hur "starkt" det är beroende på vissa kriterium (ex. längd, antal olika tecken, nummer, specialtecken osv.)
