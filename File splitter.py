print("File splitter, Will split a text file into multiple .txts!")
input_file_path = input("File name: ")
output_file_path = input("File name after splitting: ")
chopped = int(input("How many parts do you want to divide it into?: "))

try:

    with open(input_file_path, 'r') as input_file:
        text = input_file.read()

    text_length = len(text)
    part_size = text_length // chopped

    for i in range(chopped):
        start_index = i * part_size
        end_index = (i + 1) * part_size
        part_text = text[start_index:end_index]

        part_output_file_path = f"{output_file_path}_{i+1}.txt"
        with open(part_output_file_path, 'w') as output_file:
            output_file.write(part_text)
except FileNotFoundError:
    print(f"File '{input_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
