sandwich_orders = ['supreme', 'royalee', 'pastrami', 'pastrami', '6 inch sub', 'pastrami']
finished_sandwichs = []
# active = True

print("The deli has run out of pastrami!")
# another way to filter out/remove specific values than continue.
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        continue
    print("Here is you order: " + current_sandwich.title())
    finished_sandwichs.append(current_sandwich)

print("\nThe following orders have been completed:")
for finished_sandwich in finished_sandwichs:
    print(finished_sandwich.title())

