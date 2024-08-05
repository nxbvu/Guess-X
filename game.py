import random
import pygame
import time

def play_game():
    pygame.init()
    pygame.display.set_mode((200, 100))  # Slightly larger window for visibility

    print("Dies ist das Ratespiel. Sie haben 3 Tipps und müssen innerhalb von 7 Versuchen eine Zahl zwischen 0 und 100 erraten.")
    print("This is the guessing game. You have 3 hints and must guess a number between 0 and 100 within 7 attempts.")

    x = random.randint(0, 100)
    attempts = 7
    hints = 3
    suo = 0

    for attempt in range(attempts):
        try:
            guess = int(input("\033[93mRate / Guess: \033[0m"))
        except ValueError:
            print("\033[91mNicht unterstützte Eingabe / Unsupported input\033[0m")
            continue

        if guess == x:
            print("Richtig, Sie haben gewonnen! / Correct, you have won!")
            time.sleep(2)
            return True  # Player won

        elif guess > 100 or guess < 0:
            print("\033[91mDiese Zahl liegt nicht zwischen 0 und 100! / This number is not between 0 and 100!\033[0m")

        else:
            print(f"\033[92m{attempts - (attempt + 1)} Versuche verbleibend. / {attempts - (attempt + 1)} attempts remaining.\033[0m")

            if attempt == attempts - 1:
                print(f"\033[95mSie haben verloren. Die gesuchte Zahl war {x} / You lost. The correct number was {x}\033[0m")
                time.sleep(4.5)
                return False  # Player lost

            print("\033[93mFalsch / Wrong\033[0m")
            time.sleep(1.85)

            if hints > 0:
                want_hint = input("\033[93mWollen Sie einen Tipp haben? (ja/nein) / Do you want a hint? (yes/no): \033[0m")
                if want_hint.lower() in ["ja", "yes"]:
                    hints -= 1
                    give_hint(x, suo)
                    suo += 1

        time.sleep(1)

    pygame.quit()
    return False  # If all attempts are used

def give_hint(number, hint_level):
    if hint_level == 0:
        if number < 50:
            print("\033[93mDie gesuchte Zahl ist kleiner als 50 / The number is less than 50\033[0m")
        else:
            print("\033[93mDie gesuchte Zahl ist größer als 50 / The number is greater than 50\033[0m")
    elif hint_level == 1:
        if 5 < number < 80:
            print("\033[93mDie gesuchte Zahl liegt zwischen 5 und 80 / The number is between 5 and 80\033[0m")
        else:
            print("\033[93mDie Zahl liegt nicht zwischen 5 und 80 / The number is not between 5 and 80\033[0m")
    elif hint_level == 2:
        if number < 20:
            print("\033[93mDie gesuchte Zahl liegt zwischen 5 und 20 / The number is between 5 and 20\033[0m")
        elif number < 50:
            print("\033[93mDie gesuchte Zahl liegt zwischen 20 und 50 / The number is between 20 and 50\033[0m")
        elif number < 65:
            print("\033[93mDie gesuchte Zahl liegt zwischen 50 und 65 / The number is between 50 and 65\033[0m")
        else:
            print("\033[93mDie gesuchte Zahl liegt zwischen 65 und 80 / The number is between 65 and 80\033[0m")
    else:
        if number < 90:
            print("\033[93mDie gesuchte Zahl ist kleiner als 90 / The number is less than 90\033[0m")
        else:
            print("\033[93mDie gesuchte Zahl ist größer als 90 / The number is greater than 90\033[0m")

def main():
    while True:
        session = input("Wollen Sie eine Session spielen? (ja/nein) / Do you want to play a session? (yes/no): ").strip().lower()
        if session not in ["ja", "yes"]:
            break

        try:
            rounds = int(input("Wieviele Runden soll die Session dauern? / How many rounds should the session last?: "))
        except ValueError:
            print("\033[91mBitte geben Sie eine gültige Zahl ein. / Please enter a valid number.\033[0m")
            continue

        wins = 0

        for round_num in range(1, rounds + 1):
            print(f"\nRunde {round_num} von {rounds} / Round {round_num} of {rounds}")
            if play_game():
                wins += 1

        stats = input("Ihre Session ist vorbei. Wollen Sie Ihre Statistik sehen? (ja/nein) / Your session is over. Do you want to see your statistics? (yes/no): ").strip().lower()
        if stats in ["ja", "yes"]:
            print("Statistik / Statistics:")
            print(f"Wins: {wins}")
            print(f"Total Rounds: {rounds}")
            win_rate = (wins / rounds) * 100 if rounds > 0 else 0
            print(f"Win Rate: {win_rate:.2f}%")

if __name__ == "__main__":
    main()
