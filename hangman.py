import random as rnd
import requests
passwords_lifeline = ["dupa","ser","krew","banan","kotek","twojastara"]
try:
    response = requests.get('http://random-word-api.herokuapp.com/home')
    response_json = response.json()
    word = rnd.choice(response_json)
except:
    word = rnd.choice(passwords_lifeline)

'''
word = rnd.choice(password)
attempts = 11
new = "_" * len(word)
print(f"masz {attempts} prób")
funny_counter = 0
repeated = []


while new != word:
    li = [i for i in new]
    print(new)
    char = input("podaj literę: ").lower()
    if funny_counter == 3:
        print("nie wiem czy można ci pomóc.")
    if funny_counter > 4:
        print("Nie będę się nad tobą pastwić.")
        break
    if len(char) > 1:
        print("podaj jeden znak")
        funny_counter += 1
        continue
    if char.isnumeric():
        print("trzeba było podać literę.")
        funny_counter += 1
        continue
    if char in word:
        for i in range(len(word)):
            if word[i] == char:
                li[i] = char
                new = "".join(li)
        print("dobrze!")
        if new == word:
            print("zajebiście! wygrałeś/aś! NIC!")
            break
    else:
        if char not in repeated:
            attempts -= 1
            if attempts > 0:
                print(f"ty ofiaro! zostało ci {attempts} prób! {char} nie ma w słowie")
                repeated.append(char)
            else:
                print("Game Over, ofiaro!")
                break
        else:
            print(">:(")

'''
def hangman(word):
    attempts = 11
    new = "_" * len(word)
    print(f"masz {attempts} prób")
    funny_counter = 0
    repeated = []
    while new != word:
        li = [i for i in new]
        print(new)
        char = input("podaj literę: ").lower()
        if funny_counter == 3:
            print("nie wiem czy można ci pomóc.")
        if funny_counter > 4:
            print("Nie będę się nad tobą pastwić.")
            break
        if len(char) > 1:
            print("podaj jeden znak")
            funny_counter += 1
            continue
        if char.isnumeric():
            print("trzeba było podać literę.")
            funny_counter += 1
            continue
        if char in word:
            if char in repeated:
                print("...")
            else:
                repeated.append(char)
                for i in range(len(word)):
                    if word[i] == char:
                        li[i] = char
                        new = "".join(li)
                print("dobrze!")
                if new == word:
                    print("zajebiście! wygrałeś/aś! NIC!")
                    break
        else:
            if char not in repeated:
                attempts -= 1
                if attempts > 0:
                    print(f"ty ofiaro! zostało ci {attempts} prób! {char} nie ma w słowie")
                    repeated.append(char)
                else:
                    print("Game Over, ofiaro!")
                    break
            else:
                print(">:(")
    again = input("Play Again? y/n ")
    if again == "y":
        hangman(word)


hangman(word)
