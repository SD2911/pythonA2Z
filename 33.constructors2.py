class Person:
    def _init_(self, name):
      self.name = name

    def talk(self):
        print("talk")


snow = Person("john snow")
print(snow.name)
snow.talk()
       