def power(num, power):
    val = 1
    for i in range(power):
        val *= num
    return val


print(power(2, 5))
