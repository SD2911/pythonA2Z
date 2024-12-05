message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😁",
    ":(": "😥"
}
output = ""
for i in words:
    output = emojis.get(i, i) + " "
print(output)    
