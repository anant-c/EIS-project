def wrap_lines_with_parentheses(input_file, output_file):
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for line in infile:
                wrapped_line = "(" + line.strip() + ")"
                outfile.write(wrapped_line + '\n')

# Replace 'input_file.txt' and 'output_file.txt' with the appropriate file paths
wrap_lines_with_parentheses('output_file3.txt', 'output_file4.txt')
