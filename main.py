from hero import Hero, Tyler

hero1 = Hero("Patrick Bateman", 120, 60, 10, "chainsaw")
hero2 = Tyler("Tyler Durden", 100, 100, 10, 'nunchakus')

hero1.print_info()
hero2.print_info()

print("\n Patrick leaves the house")
print("\n Patric see Tyler")
print("\n Patric:Tyler i kill your mom")
print("\n Tyler:What did you say")

hero2.strike(hero1)

print("\n Patric:Its only your fall")

hero1.strike(hero2)

print("\n Tyler: Ahh no NOOOOO")
print("\n Patric:Yes i kill you and i go eat in restorant")
hero1.strike(hero2)
print("\n Patric:goodbye honey")
hero1.fight(hero2)