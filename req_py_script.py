import argparse

def create_file(filename, package_name):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith(package_name):
            return True
    return False
    # new_requirement = "new_package/1.0.2/release"
    # if new_requirement not in lines:
    #     lines.append(new_requirement)

    # with open(filename, 'w') as file:
    #     file.writelines(lines)

    # with open(filename, 'r') as file:
    #     modified_file = file.read()

    # return modified_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Modify and read the content of a .txt file.')
    parser.add_argument("--filename", required=True , help='The path to the .txt file to modify and read.')
    parser.add_argument("--package_name", required=True , help='The path to the .txt file to modify and read.')
    args = parser.parse_args()
    
    file_content = create_file(args.filename, args.package_name)

    print("modified content")
    print(file_content)
    
