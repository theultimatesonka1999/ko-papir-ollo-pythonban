import random
from os import system, name

def main():
    rnd = random.randint(1, 3)
    valasztas = input("Mit választasz? (1 = kő, 2 = papír, 3 = olló) ")
    if rnd == 1:
        rnd = "kő"
    elif rnd == 2:
        rnd = "papír"
    elif rnd == 3:
        rnd = "olló"
    
    if rnd == "kő":
        print("a robot a követ választotta")
    elif rnd == "papír":
        print("a robot a papírt választotta")
    elif rnd == "olló":
        print("a robot az ollót választotta")

    if valasztas == "1" and rnd == "kő":
        print("senki se nyert")
    elif valasztas == "2" and rnd == "kő":
        print("a robot nyert")
    elif valasztas == "3" and rnd == "kő":
        print("a robot nyert")
    elif valasztas == "1" and rnd == "papír":
        print("a robot nyert")
    elif valasztas == "2" and rnd == "papír":
        print("senki se nyert")
    elif valasztas == "3" and rnd == "papír":
        print("te nyertél")
    elif valasztas == "1" and rnd == "olló":
        print("te nyertél")
    elif valasztas == "2" and rnd == "olló":
        print("a robot nyert")
    elif valasztas == "3" and rnd == "olló":
        print("senki se nyert")
    else:
        print("hibás szám, válassz újat")
        main()
main()