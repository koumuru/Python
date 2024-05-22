class Pokemon:
  def __init__(self,entry,name,types,description,is_caught):
    self.entry = int(entry)
    self.name = str(name)
    self.types = list(map(str,types))
    self.description = str(description)
    self.is_caught = bool(is_caught)

  def speak(self):
    print(self.name)
    print(self.name)

  def display_details(self):
    print("Entry Number:",self.entry)
    print("Name:",self.name)
    print("Type:",self.types)
    print("Description:",self.description)
    
    if self.is_caught == True:
      print(self.name,"has already been caught!")
    else:
      print(self.name,"has not been caught!")

pikachu = Pokemon(25,"Pikachu",["Electric","Funny"],
"It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.",True)

bulbasaur = Pokemon(1,"Bulbasaur",["Seed"],
"For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.",False)

beedril = Pokemon(15,"Beedril",["Poison Bee"],
"It has three poisonous stingers on its forelegs and its tail. They are used to jab its enemy repeatedly.",True)

pikachu.speak()
pikachu.display_details()
print()
bulbasaur.speak()
bulbasaur.display_details()
print()
beedril.speak()
beedril.display_details()