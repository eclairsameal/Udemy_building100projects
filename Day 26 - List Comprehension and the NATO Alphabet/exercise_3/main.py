with open("file1.txt") as file1:
    file1_data = file1.readlines()
with open("file2.txt") as file2:
    file2_data = file2.readlines()
print(file1_data)
print(file2_data)

result = [int(n) for n in file1_data if n in file2_data]
# Write your code above 👆

print(result)