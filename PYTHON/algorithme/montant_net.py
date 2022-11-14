montant = int(input("Veuillez entrer le montant : "))
if montant >= 2000 and montant <= 5000:
    net = montant*0.99
elif montant > 5000:
    net = montant*0.98
else:
    net = montant

print(net)