temperature = 30

if(temperature > 30): 
    print("It's a hot day")
else:
    print("It's not a hot day")


#name = "jack"
name = input()
if len(name) < 6:
    print("short name")
elif len(name) > 11:
    print("long name")
else:
    print("good name")
