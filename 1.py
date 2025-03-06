from collections import Counter  # Import Counter to count occurrences

# Read and process input file
with open("input.txt", "r", encoding="UTF8") as file:
    lines = file.readlines()

# Extract numbers into two lists
list1, list2 = zip(*[map(int, line.strip().split('   ')) for line in lines])

# Sort both lists
list1, list2 = sorted(list1), sorted(list2)

# Calculate total absolute difference
total_difference = sum(abs(a - b) for a, b in zip(list1, list2))
print("Total Difference:", total_difference)

# Count occurrences in list2 and compute weighted sum for matching elements in list1
count_list2 = Counter(list2)
total_occur = sum(num * count_list2[num] for num in list1 if num in count_list2)

print("Weighted Sum:", total_occur)
