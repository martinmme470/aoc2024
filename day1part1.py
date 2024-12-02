array1 = []
array2 = []

with open("inputday1.txt", "r") as file:
    for line in file:
        column1, column2 = map(int, line.split()) 
        array1.append(column1)
        array2.append(column2)

array1.sort()
array2.sort()

differences = [abs(array1[i] - array2[i]) for i in range(len(array1))]

total_sum = sum(differences)

print(total_sum)
