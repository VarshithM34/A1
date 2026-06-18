import random

colors = ["yellow", "red", "green", "blue", "orange"]
tries = 10

for attempt in range(1, tries + 1):
    picked = [random.choice(colors) for _ in range(3)]
    print(f"Attempt {attempt}: {picked}")

    if picked[0] == picked[1] == picked[2]:
        print("Win! All three colors match.")
        break
    else:
        print("Try again.")
else:
    print("Game over. You used all 10 chances.")
