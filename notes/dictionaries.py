# GNB - 1st - ☑️Dictionaries Notes

#Key: value pairs

person = {
    #Key: value,
    "name": "Kratos",
    "age": 243,
    "occupation": "God of War",
    "sibling": ["Zeus", "Athena", "Haesphaestus", "Ares"]
}

print(person["name"])
print(f"Name is {person["name"]}")
print(person.keys())
for key in person.keys():
    if key == "sibling":
        for name in person[key]:
            print(f"{person['name']} has a sibling named {name}")
    print(f"{key} is {person[key]}")

print(person.values())
person["age"] -= 1

person["food"] = "Monkey soup"


for key in person.keys():
    print(f"{key} is {person[key]}")
