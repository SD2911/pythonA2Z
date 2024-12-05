customer = {
    "name": "subrata das",
    "age": 21,
    "is_verified": True
}
print(customer.get("name"))

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for c in phone:
    output += digits_mapping.get(c, "!") + " "
print(output)    


