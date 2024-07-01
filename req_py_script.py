import sys

def create_file(filename):
    with open(filename, 'w') as file:
        file.write("Hello, TeamCity!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_file.py <output_filename>")
        sys.exit(1)
    
    output_filename = sys.argv[1]
    create_file(output_filename)
