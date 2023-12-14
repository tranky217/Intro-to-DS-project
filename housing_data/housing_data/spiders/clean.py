input_file_path = 'data.json'
output_file_path = 'data.json'

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        # Remove trailing commas from each line
        modified_line = line.rstrip(',')
        # Write the modified line to the output file
        output_file.write(modified_line + '\n')

print(f"Trailing commas removed from {input_file_path}. Output written to {output_file_path}.")
