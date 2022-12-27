print("Hello world!")
print("I LOVE CODING")

# ------------------------------
# DATA
# ------------------------------
k9 = "----------------------------"
print(type("Hello"))  # STRING
print(type(17))  # INTEGER
print(type(10.30))  # FLOATING
print(type([1, 2, 3, 4, ]))  # LIST
print(type((1, 2, 3, 4,)))  # TUPLE
print(type({"One": 1, "Two": 2, "Three": 3, "Four": 4}))  # Dictionary
print(type(4 == 2 + 2))  # BOOLEAN

# ------------------------------
Myvariable = "Username"
print(Myvariable)

My_variable = "Password"
print(My_variable)

My_var89998iable = "Phone number"
print(My_var89998iable)

Address = "Address"
print(Address)

# help("keywords")                                        # KEYWORDS

a, b, c, d = 1, 2, 3, 4
print(a)
print(b)
print(c)
print(d)

# escape new line

print("Wsp \
bitch\
!")

# Escape quotes
print("I love coding \"bruuuh\"")

# line feed
print("Hello \nworld! ")

# Carriage Return
print("12345YT\rHELLO")

# Horizontal Tab
print("HELLO\tWORLD")

# Hex Value
print("\x48")

# Concatenation
msg1 = "I Love"
msg2 = "Python"
print(msg1 + " " + msg2)

msg3 = "WA TA SEEEEER"
msg4 = "VAR??????"

print(msg4 + "\n" + msg3)

haga = """NO
ARAB
!"""

print(haga)

# -----------------------------------------------------------

# Indexing ( Access Single Item )
myString1 = "I Love Python"
print(myString1[0])  # Index |0  => I|
print(myString1[3])  # Index |3  => o|
print(myString1[5])  # Index |5  => e|
print(myString1[11])  # Index |11 => o|
print(myString1[-2])  # Index |-2 => o|

# Slicing ( Access Multiple Sequence Items )
# [Start:End]
print(myString1[7:14])
print(myString1[:14])  # If no start it starts from 0
print(myString1[2:])  # If no end it goes to the end

print(myString1[:])  # Full data
print(myString1[::3])  # Steps

# Strings Methods
a1 = "I Love Python"
a2 = "        I Love Python         "
a3 = "#@#@#@#@#@I Love Python#@#@#@#@#@"
print(len(a1))
print(len(a2))

# Full Strip
print(a2.strip())
print(k9)
# Left Strip
print(a2.lstrip())
print('=')
print(len(a2.lstrip()))
print(k9)
# -----------------------------------------------------------------
print(a2.rstrip())
print(k9)
# -------------------------------------------------------------------
print(a3.strip("#@"))
print(a3.rstrip("#@"))
print(a3.lstrip("#@"))

# title ()

a5 = "I Love 3d 3gg 4g+ 2d."
print(a5.title())
print(k9)

# Capitalize ()

print(a5.capitalize())

# ZFill

c, f, k = "2", "97", "85807644"
print(c.zfill(8))
print(f.zfill(8))
print(k.zfill(8))

# Upper

G = "aKram"
print(G.upper())

G = "AKRaM"
print(G.lower())

# ---------------------------------------------------------

# Split() rsplit()

a865 = "I love Python and Myself"
print(a865.split())

a145 = "I/love/Python/and/Myself"
print(a145.split("/"))

a44 = "I/love/Python/and/Myself"
print(a44.split("/", 2))

a45 = "I/love/Python/and/Myself"
print(a45.rsplit("/", 2))

# Center ()

a8 = "Akram"
print(a8.center(9))  # Spaces
print(a8.center(11, '#'))  # Hashes
print(a8.center(15, '_'))  # ______

# count ()

f = "I love Python and css css CsS css"
print(f.count("css"))
print(f.count("css", 0, 21))

# swapcase()
bb = "bAbY"
print(bb.swapcase())
bb = "BaBy"
print(bb.swapcase())

# startswith()
g = 'BABABA'
print(g.startswith("B", 4, 6))

# endswith()
g = 'BABABA'
print(g.startswith("1", 4, 6))
