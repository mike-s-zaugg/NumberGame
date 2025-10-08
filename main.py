import random

def rate_zahl():
    zufall = random.randint(1, 10)
    
    while True:
        user_zahl = int(input("Rate eine Zahl zwischen 1 und 10: ")) 
        
        if user_zahl == zufall:
            print("Richtig! 🎉")
            break 
        else:
            print()
            print("Falsch, versuche erneut.")
            print("\033[34mDie Zahl war " + str(zufall))
            erneut_starten = input("\033[0mErneut Versuchen? [y|n]: ").lower()

            if erneut_starten == "y":
                zufall = random.randint(1, 10)

            elif erneut_starten == "n":
                print("Das Spiel wird beendet.")
                break

            else:
                print("Falsche Eingabe.")
                print()

rate_zahl()
