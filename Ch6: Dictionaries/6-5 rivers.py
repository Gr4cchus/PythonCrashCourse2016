major_rivers = {"nile": "egypt",
                "yangtze": "china",
                "amazon": "peru"}

for river, country in major_rivers.items():
    print("The", river.title(), "runs through", country.title() + ".")

for river in major_rivers.keys():   # or default major_rivers:
    print(river.title())

for country in major_rivers.values():
    print(country.title())
