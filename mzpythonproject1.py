print("hello world")
x = [1, 2, 3]
print(x)
print("Ala ma kota")
print(10*"x,")
x = 5.1234567890
print('%.5f' % x)
print("witaj" * 10)
imie = "Zosia"
print("Witaj, %s!" % imie)
dane = ("Juliusz", 45)
print("%s ma %d lat." % dane)
x = 2
print(x == 2)
print(x != 3)
print(x > 6)
imie = "Dariusz"
wiek = 35
if imie == "Dariusz" and wiek == 35:
    print("Na imie Ci Dariusz i masz 35 lat.")

wartosc = 5
if wartosc >= 50:
    print("wartosc wysoka")

elif wartosc >= 49:
    print("wartosc srednia")

elif wartosc >= 25:
    print("wartosc niska")

else:
    print("nieklasyfikowane")


def change_velocity_in_metres_per_seconds_into_velocity_in_kilometres_per_hours(value):
    result = value * 3.6
    return result


print(change_velocity_in_metres_per_seconds_into_velocity_in_kilometres_per_hours(500))


class Player:
    pass


player = Player()
player.points = 0
print(player.points)


class Dog:
    pass


dog = Dog()
dog.breed = "beagle"
print(dog.breed)


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car = Car("Ferrari", "Enzo")
print(car.model)

sekwencja = "AAAAAGGAATTCCCCTAGAATTAAAAACCAGGTTACTG"
odcinki = ["AAA", "ATT", "GGG", "AGG"]
wynik = [[o, o in sekwencja] for o in odcinki]

for s, t in wynik:
    print(f'{s}: {t}')

import re

wynik = re.match("Python", "Python jest jezykiem czasochlonnym do nauczenia")
print(wynik)
print(f"Dopasowano: '{wynik.group()}', początek: {wynik.span()[0]}, koniec: {wynik.span()[1]}")


import re
tekst = "Python jest jezykiem czasochlonnym do nauczenia"
wzorzec = re.compile(r'.?')
print(wzorzec.findall(tekst))


A = {"Jake", "John", "Eric"}
B = {"John", "Jill"}

print(A.intersection(B))
print(A.symmetric_difference(B))
print(A.difference(B))
print(A.union(B))




