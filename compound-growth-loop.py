import time


# ==========================================
# Project: Personal Finance Simulator
# Created by: Hakan Taşar
# Logic: Using 'While Loops' to track compound interest over time.
# ==========================================

def start_simulation():
    print("\n--- Compounding Interest Calculator ---")

    # Getting the inputs.
    # Using float because money needs decimals.
    current_balance = float(input("Starting Amount ($): "))
    annual_rate = float(input("Annual Return Rate (%): "))
    target_goal = float(input("Target Goal ($): "))

    year = 0

    print(f"\nSimulation started... Aiming for ${target_goal:,.2f}\n")

    # Here is the main logic for Day 6.
    # Since I don't know how many years it will take, a 'while' loop is perfect.
    while current_balance < target_goal:
        # Applying the growth formula
        current_balance = current_balance * (1 + annual_rate / 100)
        year += 1

        # Formatting the number to look like real money (e.g. 1,000.50)
        formatted_money = "{:,.2f}".format(current_balance)

        # Adding a small delay to make the output readable
        time.sleep(0.5)
        print(f"Year {year}: ${formatted_money}")

    # Loop finished, goal reached.
    print("-" * 35)
    print(f"Success! Goal reached in {year} years.")


# Run the script
start_simulation()