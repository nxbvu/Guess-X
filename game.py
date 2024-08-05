import random
import pygame
import time

def play_game():
    pygame.init()
    pygame.display.set_mode((200, 100))  # Slightly larger window for visibility

    print("Dies ist das Ratespiel. Sie haben 3 Tipps und müssen innerhalb von 7 Versuchen eine Zahl zwischen 0 und 100 erraten.")

    x = random.randint(0, 100)
    attempts = 7
    hints = 3
    suo = 0

    for attempt in range(attempts):
        try:
            guess = int(input("\033[93mRate: \033[0m"))
        except ValueError:
            print("\033[91mNicht unterstützte Eingabe\033[0m")
            continue

        if guess == x:
            print("Richtig, Sie haben gewonnen!")
            time.sleep(2)
            return True  # Player won

        elif guess > 100 or guess < 0:
            print("\033[91mDiese Zahl liegt nicht zwischen 0 und 100!\033[0m")

        else:
            print(f"\033[92m{attempts - (attempt + 1)} Versuche verbleibend.\033[0m")

            if attempt == attempts - 1:
                print(f"\033[95mSie haben verloren. Die gesuchte Zahl war {x}\033[0m")
                time.sleep(4.5)
                return False  # Player lost

            print("\033[93mFalsch\033[0m")
            time.sleep(1.85)

            if hints > 0:
                want_hint = input("\033[93mWollen Sie einen Tipp haben? (ja/nein): \033[0m")
                if want_hint.lower() == "ja":
                    hints -= 1
                    give_hint(x, suo)
                    suo += 1

        time.sleep(1)

    pygame.quit()
    return False  # If all attempts are used

def give_hint(number, hint_level):
    if hint_level == 0:
        if number < 50:
            print("\033[93mDie gesuchte Zahl ist kleiner als 50\033[0m")
        else:
            print("\033[93mDie gesuchte Zahl ist größer als 50\033[0m")
    elif hint_level == 1:
        if 5 < number < 80:
            print("\033[93mDie gesuchte Zahl liegt zwischen 5 und 80\033[0m")
        else:
            print("\033[93mDie Zahl liegt nicht zwischen 5 und 80\033[0m")
    elif hint_level == 2:
        if number < 20:
            print("\033[93mDie gesuchte Zahl liegt zwischen 5 und 20\033[0m")
        elif number < 50:
            print("\033[93mDie gesuchte Zahl liegt zwischen 20 und 50\033[0m")
        elif number < 65:
            print("\033[93mDie gesuchte Zahl liegt zwischen 50 und 65\033[0m")
        else:
            print("\033[93mDie gesuchte Zahl liegt zwischen 65 und 80\033[0m")
    else:
        if number < 90:
            print("\033[93mDie gesuchte Zahl ist kleiner als 90\033[0m")
        else:
            print("\033[93mDie gesuchte Zahl ist größer als 90\033[0m")

def main():
    while True:
        session = input("Wollen Sie eine Session spielen? (ja/nein): ").strip().lower()
        if session != "ja":
            break

        try:
            rounds = int(input("Wieviele Runden soll die Session dauern?: "))
        except ValueError:
            print("\033[91mBitte geben Sie eine gültige Zahl ein.\033[0m")
            continue

        wins = 0

        for round_num in range(1, rounds + 1):
            print(f"\nRunde {round_num} von {rounds}")
            if play_game():
                wins += 1

        stats = input("Ihre Session ist vorbei. Wollen Sie Ihre Statistik sehen? (ja/nein): ").strip().lower()
        if stats == "ja":
            print("Statistik:")
            print(f"Wins: {wins}")
            print(f"Total Rounds: {rounds}")
            win_rate = (wins / rounds) * 100 if rounds > 0 else 0
            print(f"Win Rate: {win_rate:.2f}%")

if __name__ == "__main__":
    main()
