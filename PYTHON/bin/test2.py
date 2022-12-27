def counter(start, stop):
    x = start
    if start < stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x -= 1
    else:
        print("up")

    return return_string

b = counter(2,5)
c = counter(5,2)
print(b,c)
