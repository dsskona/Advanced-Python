input_file = open("input.txt", "r")

lines = input_file.readlines()

print("Number of lines:", len(lines))

first_two_lines = lines[:2]

input_file.close()

output_file = open("output.txt", "w")

output_file.writelines(first_two_lines)

output_file.close()

print("First two lines have been written to output.txt")