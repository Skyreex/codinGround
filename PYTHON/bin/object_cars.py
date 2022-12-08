from class_cars import cars

car1 = cars("Benz", "Velo", 1894, "20 Km/h", "single-cylinder 1.1 kW (1.5 PS; 1.5 bhp)", "1,045 cm3", 1200)
car2 = cars("Jaguar", "XK120", 1949, "200.5 km/h", "inline-6 119 kW (162 PS; 160 hp)", "3,442 cm3", 12000)

data = open("cars.txt", "r+")
lines = data.readlines()
line = lines[0]
print(line[0:4])
print(line)
print(car1)
print(car1.make)