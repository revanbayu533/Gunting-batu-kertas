import random

choices = ["batu", "kertas", "gunting"]

running = True

while running:
    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("Masukkan pilihan (batu, kertas, gunting): ").lower()

    print(f"Pemain: {player}")
    print(f"Komputer: {computer}")

    if player == computer:
        print("Ini seri!")
    elif (player == "batu" and computer == "gunting") or \
         (player == "kertas" and computer == "batu") or \
         (player == "gunting" and computer == "kertas"):
        print("Kamu menang!")
    else:
        print("Kamu kalah!")

    if input("Mainkan lagi? (yes/no): ").lower() != "yes":
        running = False

print("Terima kasih sudah bermain!")