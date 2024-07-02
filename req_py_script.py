import argparse

def create_file(filename):
    with open(filename, 'w') as file:
        lines = file.readlines()

    new_requirement = "new_package/1.0.2/release"
    if new_requirement not in lines:
        lines.append(new_requirement)

    with open(filename, 'w') as file:
        file.writelines(lines)

    with open(filename, 'r') as file:
        modified_file = file.read()

    return modified_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Modify and read the content of a .txt file.')
    parser.add_argument('filename', type=str, help='The path to the .txt file to modify and read.')
    args = parser.parse_args()
    
    file_content = create_file(output_filename)

    print("modified content")
    print(file_content)
    
