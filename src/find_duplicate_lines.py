def find_duplicate_lines(file_path_arg):
    seen_lines = set()
    duplicate_lines = []

    with open(file_path_arg, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if line in seen_lines:
                duplicate_lines.append((line_number, line))
            seen_lines.add(line)

    if duplicate_lines:
        print("Duplicate lines found:")
        for line_number, line in duplicate_lines:
            print(f"  Line {line_number}: {line}")
        print(f"Total duplicates found: {len(duplicate_lines)}")
    else:
        print("No duplicate lines found.")


if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")

    try:
        find_duplicate_lines(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
