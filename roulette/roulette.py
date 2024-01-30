import random
import os
import sys
import threading
import time

# Function to simulate CPU player's turn
def cpu_player():
    time.sleep(5)  # Simulate 5 seconds delay
    cpu_bullet = random.randint(1, int(chambers))
    print("CPU Player's turn...")
    if cpu_bullet == fatal_bullet:
        print("CPU Player hit the bullet! You win!")
    else:
        print("CPU Player survived.")

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main game loop
while True:
    clear_screen()
    print(""" || RUSSIAN ROULETTE GAME ||
                    ________. 
                ~(_]-------'  
                /_(U 
    """)

    chambers = input("Please enter the number of chambers (default = 6): ")

    if not chambers:
        chambers = 6
    elif not chambers.isdigit():
        quit("Invalid number of chambers!")

    fatal_bullet = random.randint(1, int(chambers))

    # Start the CPU player thread
    cpu_thread = threading.Thread(target=cpu_player)
    cpu_thread.start()

    for x in range(1, int(chambers) + 1):
        input("Press enter to pull the trigger! ")
        if x == fatal_bullet:
            print("Game Over - You hit the bullet!")
            start_again = input("Do you want to start again? (y/n): ")
            if start_again and start_again.lower()[0] == "y":
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:
                sys.exit(0)
    
    # Wait for the CPU player thread to finish before restarting
    cpu_thread.join()

    print("You survived! The chambers were empty.")

    start_again = input("Do you want to start again? (y/n): ")
    if start_again and start_again.lower()[0] != "y":
        sys.exit(0)