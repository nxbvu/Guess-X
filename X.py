for z in range(1111):
    import random
    import pygame
    import time

    runde = 0
    win = 0
    session = input("Wollen sie eine Session spielen?: ")
    versuche = 0
    tippsn = 0
    e = None

    if session == "ja":
        wiev = int(input("Wieviele Runden soll die Session dauern?: "))
        for l in range(wiev):
            runde += 1
            print(f"Runde {runde} von {wiev}")
            pygame.init()
            pygame.display.set_mode((2, 1))

            print("Dies ist das Ratespiel, sie haben 3 Tipps und müssen innerhalb von 7 Versuchen eine Zahl zwischen 0 und 100 erraten.")

            x = random.randint(0,100)
            i = 1
            tippcount = 0
            tippcountbig = 0
            v1 = -142354
            korrekt = False
            suo = 0  
            for i in range(7):

         
                try:
                    v1 = int(input("\033[93mRate: \033[0m"))
                except ValueError:
                    print("\033[91mNicht unterstützte Eingabe\033[0m")

                tipp = ""

                if v1 == x:
                    print("Richtig, sie haben gewonnen!")
                    win += 1
                    time.sleep(2)
                    break
                elif v1 == -142354:
                    break
                elif v1 > 100 or v1 < 0:
                    print("\033[91mDiese Zahl liegt nicht zwischen 0 und Hundert!\033[0m")
                else:
                    i += 1
                    print("\033[92m", 7 - i, "Versuche verbleibend.\033[0m")
                    if i == 7:
                        print(f"\033[95mSie habend verloren, die gesuchte Zahl war {x}\033[0m")
                        time.sleep(4.5)
                        break
                    print("\033[93mFalsch\033[0m")
                    versuche += 1

                    time.sleep(1.85)
                    if tippcount < 3:
                        tipp = input("\033[93mWollen sie einen Tipp haben?: \033[0m")

                if tipp == "ja" and tippcount == 2:

                    time.sleep(0.5)
                    tippcount += 1
                    if suo == 3:
                        if x < 20:
                            print("\033[93mDie gesuchte Zahl liegt zwischen 5 und 20\033[0m")
                        else:
                            print("\033[93mDie gesuchte Zahl liegt zwischen 20 und 50\033[0m")
                    if suo == -1:
                        if x < 65:
                            print("\033[93mDie gesuchte Zahl liegt zwischen 50 und 65\033[0m")
                        else:
                            print("\033[93mDie gesuchte Zahl liegt zwischen 65 und 80\033[0m")
                    if suo == 1:
                        if x != 2:
                            print("\033[93mDie gesuchte Zahl ist nicht 2\033[0m")
                        else:
                            print("\033[93mDie gesuchte Zahl ist 2\033[0m")
                    if suo == -3:
                        if x < 90:
                            print("\033[93mDie gesuchte Zahl ist kleiner als 90\033[0m")
                        else:
                            print("\033[93mDie gesuchte Zahl ist größer als 90\033[0m")

                if tipp == "ja" and tippcount == 1:
                    time.sleep(0.5)
                    tippcount += 1
                    if x < 50:
                        print("\033[93mDie gesuchte Zahl ist kleiner als 50\033[0m")
                        print("\033[92m", 3 - tippcount, "Tipps verbleibend.\033[0m")
                        suo += 2
                    else:
                        print("\033[93mDie gesuchte Zahl ist größer als 50\033[0m")
                        suo -= 2

                if tipp == "ja" and tippcount == 0:
                    time.sleep(0.5)
                    tippcount += 1
                    if x < 80 and x > 5:
                        print("\033[93mDie gesuchte Zahl liegt zwischen 5 und 80\033[0m")
                        print("\033[92m", 3 - tippcount, "Tipps verbleibend.\033[0m")
                        suo += 1
                    else:
                        print("\033[93mDie Zahl liegt nicht zwischen 5 und 80\033[0m")
                        suo -= 1
                if tipp == "gorti":
                    print(x)
                    print("Cheat benutzt")
            tippcountbig += tippcount
            if runde == wiev:
                statsq = input("Ihre Session ist vorbei, wollen sie ihre statistik sehen?: ")
                if win == 0:
                    e = 0
                e = round(wiev / win, 1)

                def stats():
                    print("Statistik:")
                    print(f"Wins: {win}")
                    print(f"Versuche von maximal {wiev * 7}: {versuche}")
                    print(f"Verbrauchte Tipps von maximal {wiev * 3}: {tippcount}")
                    print(f"Punkte von maximal 100: {e + round(wiev * 3 / tippcount, 1) + round(wiev * 7 / versuche, 1) * 10}")

                if statsq == "ja":
                    stats()
            pygame.quit()
    else:
            pygame.init()
            pygame.display.set_mode((2, 1))


            print("Dies ist das Ratespiel, sie haben 3 Tipps und müssen innerhalb von 7 Versuchen eine Zahl zwischen 0 und 100 erraten.")

            x = random.randint(0,100)
            i = 1
            tippcount = 0
            v1 = -142354
            korrekt = False
            suo = 0

            for i in range(7):

                try:
                    v1 = int(input("\033[93mRate: \033[0m"))
                except ValueError:
                    print("\033[91mNicht unterstützte Eingabe\033[0m")

                tipp = ""

                if v1 == x:
                    print("Richtig, sie haben gewonnen!")
                    time.sleep(2)
                    break
                elif v1 == -142354:
                    break
                elif v1 > 100 or v1 < 0:
                    print("\033[91mDiese Zahl liegt nicht zwischen 0 und Hundert!\033[0m")
                else:
                    i += 1
                    print("\033[92m", 7 - i, "Versuche verbleibend.\033[0m")
                    if i == 7:
                        print(f"\033[95mSie habend verloren, die gesuchte Zahl war {x}\033[0m")
                        time.sleep(4.5)
                        break
                    print("\033[93mFalsch\033[0m")
                    time.sleep(1.85)
                    if tippcount < 3:
                        tipp = input("\033[93mWollen sie einen Tipp haben?: \033[0m")

                if tipp == "ja" and tippcount == 2:
                    time.sleep(0.5)
                    tippcount += 1
                    if suo == 3:
                        if x < 20:
                            print("\033[93mDie gesuchte Zahl liegt zwischen 5 und 20\033[0m")
                        else:
                            print("\033[93mDie gesuchte Zahl liegt zwischen 20 und 50\033[0m")
                    if suo == -1:
                        if x < 65:
                            print("\033[93mDie gesuchte Zahl liegt zwischen 50 und 65\033[0m")
                        else:
                            print("\033[93mDie gesuchte Zahl liegt zwischen 65 und 80\033[0m")
                    if suo == 1:
                        if x != 2:
                            print("\033[93mDie gesuchte Zahl ist nicht 2\033[0m")
                        else:
                            print("\033[93mDie gesuchte Zahl ist 2\033[0m")
                    if suo == -3:
                        if x < 90:
                            print("\033[93mDie gesuchte Zahl ist kleiner als 90\033[0m")
                        else:
                            print("\033[93mDie gesuchte Zahl ist größer als 90\033[0m")

                if tipp == "ja" and tippcount == 1:
                    time.sleep(0.5)
                    tippcount += 1
                    if x < 50:
                        print("\033[93mDie gesuchte Zahl ist kleiner als 50\033[0m")
                        print("\033[92m", 3 - tippcount, "Tipps verbleibend.\033[0m")
                        suo += 2
                    else:
                        print("\033[93mDie gesuchte Zahl ist größer als 50\033[0m")
                        suo -= 2

                if tipp == "ja" and tippcount == 0:
                    time.sleep(0.5)
                    tippcount += 1
                    if x < 80 and x > 5:
                        print("\033[93mDie gesuchte Zahl liegt zwischen 5 und 80\033[0m")
                        print("\033[92m", 3 - tippcount, "Tipps verbleibend.\033[0m")
                        suo += 1
                    else:
                        print("\033[93mDie Zahl liegt nicht zwischen 5 und 80\033[0m")
                        suo -= 1
                if tipp == "gorti":
                    print(x)

            pygame.quit()       