responses = []
polling_active = True
prompt = "If you could visit one place in the world, where would you go?"

while polling_active:
    # name = input("\nWhat is your name? ")
    response = input(prompt)
    if response == 'quit':
        break
    responses.append(response)
for response in responses:
    print(response)
