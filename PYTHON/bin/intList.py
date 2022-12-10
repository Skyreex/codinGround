list1 = [42, "fdf", 5, "fzgrge", "fefsf", 1, 7, 33.44, "frfefr", 0, "zfzefrgr", "zefz", 43, 6]
list2 = []
for i in list1:
    if isinstance(i, int):
        list2.append(i)
    elif isinstance(i, float):
        list2.append(i)
print(list1)
print(list2)
