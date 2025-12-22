martialarts={"mma":"every martial art","karate":"not the best fighting style","kung fu":"used by ancient Jaoanise during the samurai","wrestling":"great sport for people who enjoy throws and slams","BJJ":"brazilian jujistsu a sport for groundwork"}

print (martialarts)
print (martialarts.keys())

print (martialarts.values())

martialarts["kung fu"]="a chinese sport"

print (martialarts)

martialarts["boxing"]="focoses on footwork and speed agility and punching(moslty)"

del martialarts ["karate"]

print (martialarts)

for key,pair in martialarts.items():
    print(key,pair)

if "kung fu" in martialarts:
    print ("item is present")

else:
    print ("item is not present")

if "dinasaur" in martialarts:
    print ("item is present")

else:
    print("item is not present")

print (type(martialarts))

cars=[]
print (type(cars))