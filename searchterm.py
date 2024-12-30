import os

def search_string_in_files(root_folder, search_string):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if search_string in file_path:
                print("FILE:", file_path)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_number, line in enumerate(f, start=1):
                        if search_string in line:
                            print(line)
                            print(f"Found in file: {file_path}, Line: {line_number}")
                            
            except Exception as e:
                print(f"Could not read file {file_path}. Error: {e}")


if __name__ == "__main__":
    folder_path = "UNION_BANK_V1.0"
    search_term = input("Enter the string to search: ")
    search_string_in_files(folder_path, search_term)
