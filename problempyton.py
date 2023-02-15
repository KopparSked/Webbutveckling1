# Villkor
# if - else

'''  
y=4

# med två if - satser

if y > 5: # viktigt att avsluta med kolon, :
    print('y är större än fem')

if y < 5:
    print('y är mindre än fem')
    
  
# samma sak fast med if - else
'''
'''
y=8    
if y > 5:
    print('y är större än fem')
else:
    print('y är mindre än eller lika med fem')
'''

'''    


#Exempel på nästlade if-satser (krånglig kod)


'''
'''
p=int(input('Ange poäng på provet (0 - 100): '))

if p >=90:
    print('Betyg = A')
else:
    if p >= 80:
        print('Betyg = B')
    else: 
        if p >= 70:
            print('Betyg = C')
        else:
            if p >= 60:
                print('Betyg = D')
            else: 
                if p >= 50:
                    print('Betyg = E')
                else:
                    print('Betyg = F')
        


'''


'''

p=int(input('Ange poäng på provet (0 - 100): '))
if p >=90:
    print('Betyg = A')
elif p >= 80:
    print('Betyg = B') 
elif p >= 70:
    print('Betyg = C')
elif p >= 60:
    print('Betyg = D')
elif p >= 50:
    print('Betyg = E')
else:
    print('Betyg = F')


'''
'''

''''''
# and och or
'''
'''
month= int(input('Ange månadsnummer: '))

if month < 1 or month >12:
    print('Felaktig månadsangivelse!')
else:
    print('OK!')
if month >= 1 and month <=12:
    print('OK!')
else:
    print('Felaktig månadsangivelse')
    
    
    
''''''    
'''
#Uppgifter


'''
'''
1
En operatör för mobiltelefoni erbjuder tre olika abonnemang:
Kontant, Normal och Plus. Om man jämför villkoren för abbonemangen visar det sig att
abonnemanget Kontant är billigast om man ringer högst 33 minuter per månad,
Normal lönar sig bäst om man ringer mellan 33 och 66 minuter per månad och
Normal lönar sig bäst om man ringer ännu mer. 
Skriv ett program som läser in antalet minuter och avgör vilket
abonnemang man ska välja.

2. I en tidigare uppgift skulle du skriva ett program som beräknade cirkelns
area och omkrets. Utöka programmet med en if-sats som kontrollerar att den
inlästa radien är större än 0. Om radien är 0 så ska programmet skriva
ett felmeddelande.

3. Skriv ett programm som läser in längderna på två sidor i en triangel och
vinkeln mellan de två sidorna.
Programmet ska avgöra om triangeln är liksidig, likbent eller oliksidig.
Tips: använd c=sqrt(a^2+b^2-2ab*cos(v)), där v är vinkeln mellan sidorna.
'''




    





