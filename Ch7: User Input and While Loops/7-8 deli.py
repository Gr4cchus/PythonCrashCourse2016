
sandwich_orders = ['supreme', 'royalee', '6 inch sub']
finished_sandwichs = []
# active = True

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("Here is you order: " + current_sandwich.title())
    finished_sandwichs.append(current_sandwich)

print("\nThe following orders have been completed:")
for finished_sandwich in finished_sandwichs:
    print(finished_sandwich.title())
