def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEUIOYaeyuio":
            translation += "f"
        else:
            translation += letter
    return translation

phrase = input("phrase : ")

print(translate(phrase))
