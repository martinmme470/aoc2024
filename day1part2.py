array1 = []
array2 = []

with open("inputday1.txt", "r") as file:
    for line in file:
        column1, column2 = map(int, line.split()) 
        array1.append(column1)
        array2.append(column2)

array1.sort()
array2.sort()

similarity_score = []

for element in array1:
    count_in_array2 = array2.count(element)  
    similarity_score.append(element * count_in_array2)


print(sum(similarity_score))
