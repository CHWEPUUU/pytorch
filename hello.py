list = [1, 2, 3]

test = iter(list)
print(test)

for i in range(len(list)):
    print(next(test))