# Read the input from the file
with open("inputday2.txt", "r") as file:
    # Parse the file into a list of lists of integers
    rows = [list(map(int, line.split())) for line in file]

# Initialize the list to store rows meeting all criteria
list_after_criteria_3 = []

# Function to check criteria 1
def meets_criteria_1(row):
    return all(abs(row[i] - row[i + 1]) <= 3 for i in range(len(row) - 1)) and \
           all(abs(row[i] - row[i + 1]) != 0 for i in range(len(row) - 1))

# Function to check criteria 2
def meets_criteria_2(row):
    return all(row[i] <= row[i + 1] for i in range(len(row) - 1)) or \
           all(row[i] >= row[i + 1] for i in range(len(row) - 1))

# Loop through each row
for row in rows:
    if meets_criteria_1(row) and meets_criteria_2(row):
        # If row meets both criteria, append directly
        list_after_criteria_3.append(row)
    else:
        # If not, check if removing one element allows the row to pass
        for i in range(len(row)):
            modified_row = row[:i] + row[i+1:]  # Remove the ith element
            if meets_criteria_1(modified_row) and meets_criteria_2(modified_row):
                list_after_criteria_3.append(row)  # Add original row if it can pass after removing one element
                break  # No need to check further modifications for this row

# Print the count of rows meeting all criteria (with or without modifications)
print(len(list_after_criteria_3))
