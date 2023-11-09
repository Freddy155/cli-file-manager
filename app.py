import os

class FileManager:
    def __init__(self, current_directory="."):
        self.current_directory = current_directory

    def list_files(self):
        files = os.listdir(self.current_directory)
        return files

    def create_file(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        with open(file_path, 'w'):
            pass
        return f"File created: {file_name}"

    def delete_file(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            return f"File deleted: {file_name}"
        else:
            return f"File not found: {file_name}"

    def create_folder(self, folder_name):
        folder_path = os.path.join(self.current_directory, folder_name)
        os.makedirs(folder_path)
        return f"Folder created: {folder_name}"

    def delete_folder(self, folder_name):
        folder_path = os.path.join(self.current_directory, folder_name)
        if os.path.exists(folder_path):
            os.rmdir(folder_path)
            return f"Folder deleted: {folder_name}"
        else:
            return f"Folder not found: {folder_name}"

    def navigate(self, new_directory):
        new_path = os.path.join(self.current_directory, new_directory)
        if os.path.exists(new_path) and os.path.isdir(new_path):
            self.current_directory = new_path
            return f"Current directory changed to: {new_directory}"
        else:
            return f"Directory not found: {new_directory}"

def file_operations():
    file_manager = FileManager()

    while True:
        print("\nChoose an operation:")
        print("1. List Files")
        print("2. Create File")
        print("3. Delete File")
        print("4. Create Folder")
        print("5. Delete Folder")
        print("6. Navigate")
        print("7. Exit")

        choice = input("Enter the operation number: ")

        if choice == '1':
            print(file_manager.list_files())
        elif choice == '2':
            file_name = input("Enter the file name: ")
            print(file_manager.create_file(file_name))
        elif choice == '3':
            file_name = input("Enter the file name: ")
            print(file_manager.delete_file(file_name))
        elif choice == '4':
            folder_name = input("Enter the folder name: ")
            print(file_manager.create_folder(folder_name))
        elif choice == '5':
            folder_name = input("Enter the folder name: ")
            print(file_manager.delete_folder(folder_name))
        elif choice == '6':
            new_directory = input("Enter the new directory: ")
            print(file_manager.navigate(new_directory))
        elif choice == '7':
            print("Exiting the file management system. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid operation number.")

file_operations()
