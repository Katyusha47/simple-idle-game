import time

class Player:
    def __init__(self):
        self.gold = 0
        self.gold_per_second = 1
        self.click_gold = 1
        self.upgrades = {
            'Clicking Power': {'cost': 10, 'increment': 1},
            'Gold Per Second': {'cost': 100, 'increment': 1},
            'Auto Clicker': {'cost': 500, 'increment': 2},
            'Gold Rush': {'cost': 1000, 'increment': 5}
        }
        self.autoclickers = 0
        self.gold_rush_active = False
        self.gold_rush_time = 0

    def update(self, dt):
        # Calculate the amount of gold gained in the current tick
        gold_gain = self.gold_per_second * dt

        # Update the gold value
        self.gold += gold_gain

        # Check if Gold Rush is active
        if self.gold_rush_active:
            self.gold += gold_gain * 5

        # Display the current state of the game
        print(f"Gold: {self.gold}")
        print(f"Gold per second: {self.gold_per_second}")
        print(f"Clicking Power: {self.click_gold}")
        print(f"Auto Clickers: {self.autoclickers}")
        print(f"Gold Rush Time Left: {self.gold_rush_time}")

    def click(self):
        # Add gold from clicking
        self.gold += self.click_gold

    def buy_upgrade(self, upgrade_name):
        # Check if the player has enough gold to purchase the upgrade
        if self.gold < self.upgrades[upgrade_name]['cost']:
            print("Not enough gold to purchase upgrade.")
            return

        # Deduct the cost of the upgrade from the player's gold
        self.gold -= self.upgrades[upgrade_name]['cost']

        # Increment the relevant stat by the upgrade increment
        if upgrade_name == 'Clicking Power':
            self.click_gold += self.upgrades[upgrade_name]['increment']
        elif upgrade_name == 'Gold Per Second':
            self.gold_per_second += self.upgrades[upgrade_name]['increment']
        elif upgrade_name == 'Auto Clicker':
            self.autoclickers += 1
        elif upgrade_name == 'Gold Rush':
            self.gold_rush_active = True
            self.gold_rush_time = 10

        # Increment the cost of the upgrade for the next purchase
        self.upgrades[upgrade_name]['cost'] += int(self.upgrades[upgrade_name]['cost'] * 0.1)

    def activate_gold_rush(self):
        # Check if Gold Rush is already active
        if self.gold_rush_active:
            print("Gold Rush is already active.")
            return

        # Check if the player has enough gold to activate Gold Rush
        if self.gold < self.upgrades['Gold Rush']['cost']:
            print("Not enough gold to activate Gold Rush. You can purchase Gold Rush in the shop.")
            return

        # Deduct the cost of Gold Rush from the player's gold
        self.gold -= self.upgrades['Gold Rush']['cost']

        # Activate Gold Rush
        self.gold_rush_active = True
        self.gold_rush_time = 10
    


    def buy_menu(self):
        print("1. Buy Autoclicker (costs 500 gold)")
        print("2. Upgrade Clicking Power (costs 10 gold)")
        print("3. Upgrade Gold Per Second (costs 100 gold)")
        print("4. Activate Gold Rush (costs 1000 gold)")
        print("5. Exit Buy Menu")
        action = input("Your choice: ")

        if action == '1':
            self.buy_autoclicker()
        elif action == '2':
            self.buy_upgrade('Clicking Power')
        elif action == '3':
            self.buy_upgrade('Gold Per Second')
        elif action == '4':
            self.activate_gold_rush()
        elif action == '5':
            return
        else:
            print("Invalid choice. Please try again.")
            self.buy_menu()

    def run(self):
        last_time = time.time()

        # Define the main game loop
        while True:
            current_time = time.time()
            dt = current_time - last_time
            last_time = current_time

            # Handle input from the player
            print("1. Click (just click enter :)")
            print("2. Buy")
            print("3. Activate Gold Rush")
            print("4. Quit")
            action = input("Your choice:")

            if action == '1':
                self.click()
            elif action == '2':
                self.buy_menu()
            elif action == '3':
                self.activate_gold_rush()
            elif action == '4':
                break

            # Update the game state
            self.update(dt)

            # Check if Gold Rush is active
            if self.gold_rush_active:
                self.gold_rush_time -= dt

                if self.gold_rush_time <= 0:
                    self.gold_rush_active = False

            # Wait for 0.1 seconds before continuing to the next tick
            time.sleep(0.1)

# Create a new instance of the Player class
player = Player()

# Start the game
player.run()

