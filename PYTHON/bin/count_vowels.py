phrase = input("Phrase : ")
vowels = 0
for letter in phrase:
    if letter in "AEUIOaeuio":
        vowels += 1

print(f"This phrase contains {vowels} vowels")
