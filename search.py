import os

def search_files(directory, target):
    for root, _, files in os.walk(directory):
        for file in files:
            if target in file:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path)
                print(relative_path)

def main():
    current_directory = os.getcwd()
    print("検索する文字列を入力してください:")
    search_string = input()
    print("------検索結果--------")
    search_files(current_directory, search_string)

if __name__ == "__main__":
    main()
