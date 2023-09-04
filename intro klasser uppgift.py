import random

class teknikare:
    def __init__(self, name, age, bodycount, caffine_count_today, dicord_mod_count, boner_count_today) -> None:
        self.name = name
        self.age = age
        self.bodycount = bodycount
        self.caffine_count_today = caffine_count_today
        self.dicord_mod_count = dicord_mod_count
        self.boner_count_today = boner_count_today

    def __str__ (self) -> str:
        return_string = f"{self.name} är {self.age} och har knullat med {self.bodycount} , samt har intagit  {self.caffine_count_today} mg caffine today"
        return_string += f" är även mod i {self.dicord_mod_count} antal servrar\n, fått en sten hård dari {self.boner_count_today} antal gånger idag"
        return return_string

def visa_namn_eller_kör(teknikarna):
    while True:
        val = input("Välj ett alternativ skriv in den siffran som står brevid:\n1. Visa alla som är med\n2. Kör programmet som vanligt\n3. Se vem som är riktigt kått på dig niklas\n4. Se hur många gånger en elev fick en hård dari påväg till skola på tunnelbanan och bussen\nSkriv här:" )
        if val == "1":
            for namn in Namn:
                print(namn)
        elif val == "2":
            for teknikare in teknikarna:
                print(teknikare)
        elif val == "3":
            random_teknikare=random.choice(Namn)
            print("Oj du va så kattig niklas att", random_teknikare, "fick en riktigt hård dari")
        elif val == "4":
            random_teknikare=random.choice(Namn)
            hård_dari=random.randrange(20)
            print("På väg till kolan fick",random_teknikare," en riktigt ",hård_dari,"antal gånger på bussen och tunnelbanan")
        else:
            print("Oj, nu blev det fel här. Är du dum eller jag skrev ju hur man väljer och du skriver nåt annat jävla mongo.")

        while True:
            fortsätt = input("Vill du fortsätta? (ja/nej): ")
            if fortsätt.lower() == "ja":
                break
            elif fortsätt.lower() == "nej":
                exit()
            else:
                print("Oj, nu blev det fel här. Är du dum eller jag skrev ju hur man väljer och du skriver nåt annat jävla mongo.")
                continue 



if __name__ == "__main__":
    daniel_intance = teknikare("Daniel", 18, 1, 500, 4, 20)
    amos_intance = teknikare("Amos", 17, "-3", 250, 10, 35)
    max_intance = teknikare("Max", 18, 0, 1500, 23, 76)
    dexter_intance = teknikare("Dexter", 17, "killar 2, tjejer 0", 75, 2, 150)
    aron_intance = teknikare("Aron", 18, 4, 0, 12, 35)

    teknikarna = [daniel_intance, amos_intance, max_intance, dexter_intance, aron_intance]
    
    Namn = ["Daniel", "Amos", "Max", "Dexter", "Aron"]

    visa_namn_eller_kör(teknikarna)

