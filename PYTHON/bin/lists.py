SAMCRO = ["Jax", "Opie", "Clay", "Bobby", "Chibs", "Happy", "Tig", "Juice", "Piney"]
PROSPECTS = ["Half-sack"]
MC = ("Sons of anarchy", "Mayans") # This is a tuple. you can't modify its element
coordinates = [(4, 5), (6, 7), (80, 34)] # tuples inside of a list which means it can't be modified

# ['Jax', 'Opie', 'Clay', 'Bobby', 'Chibs', 'Happy', 'Tig', 'Juice', 'Piney']
SAMCRO.append("FF")
# ['Jax', 'Opie', 'Clay', 'Bobby', 'Chibs', 'Happy', 'Tig', 'Juice', 'Piney', 'FF']
SAMCRO.extend(PROSPECTS)
# ['Jax', 'Opie', 'Clay', 'Bobby', 'Chibs', 'Happy', 'Tig', 'Juice', 'Piney', 'FF', 'Half-sack']
SAMCRO.insert(0, "Otto")
# ['Otto' , 'Jax', 'Opie', 'Clay', 'Bobby', 'Chibs', 'Happy', 'Tig', 'Juice', 'Piney', 'FF', 'Hal-sack']
SAMCRO.remove("FF")
# ['Otto', 'Jax', 'Opie', 'Clay', 'Bobby', 'Chibs', 'Happy', 'Tig', 'Juice', 'Piney', 'Half-sack']
SAMCRO.extend("FF") # .extends adds FF as a list FF = ['F', 'F']
# ['Otto', 'Jax', 'Opie', 'Clay', 'Bobby', 'Chibs', 'Happy', 'Tig', 'Juice', 'Piney', 'Half-sack', 'F', 'F']
SAMCRO.pop(11)
# ['Otto', 'Jax', 'Opie', 'Clay', 'Bobby', 'Chibs', 'Happy', 'Tig', 'Juice', 'Piney', 'Half-sack', 'F']
SAMCRO.pop() # .pop() deletes the last element on the list
# ['Otto', 'Jax', 'Opie', 'Clay', 'Bobby', 'Chibs', 'Happy', 'Tig', 'Juice', 'Piney', 'Half-sack']
pos = SAMCRO.index("Jax")
print(f"Sa position est : {pos}")
SAMCRO2 = SAMCRO.copy()
SAMCRO.append("Bobby")
SAMCRO.sort()
SAMCRO.reverse()
print(SAMCRO.count("Bobby"))


print(MC[0])
print(SAMCRO2)
print(SAMCRO)
print(MC)
print(coordinates)
