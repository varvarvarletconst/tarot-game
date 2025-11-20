import random
from oracle import cards

print('let me guess your card')
print("choose your card by number:\n")
for card in cards:
    print(f"{card['number']}: {card['name']}")


users_card = input('insert the number of your card (I won’t peek) 👉 ')
users_card = int(users_card)

available_cards = cards.copy()

while available_cards:
    current_card = random.choice(available_cards)
    print(f'ur card is {current_card['name']}')

    guess = input('did I guess your card? (y/n) 👉 ').lower()

    if guess == 'y':
            print(f"yay! I guessed your card: {current_card['name']} 🎉")
            break
    else: 
        available_cards.remove(current_card)


