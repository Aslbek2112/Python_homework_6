list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_2 = []
for i in range(len(list_1)):
        if list_1[i] > 4 and list_1[i] < 15:
            list_2.append(i)

print(list_2)