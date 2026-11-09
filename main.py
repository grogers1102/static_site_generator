import os
import shutil

def copy_dir_to_other(source_dir, target_dir):
    try:
        if not os.path.isdir(target_dir):
            os.mkdir(target_dir, mode=0o744)
        print(source_dir)
        print(target_dir)
        if os.listdir(target_dir):
            print("Cleaning target directory")
            shutil.rmtree(target_dir)
            os.mkdir(target_dir, mode=0o744)
        source_content = os.listdir(source_dir)
        print(source_content)
        for file in source_content:
            print(f"Checking {file}")
            file_path = os.path.join(source_dir, file)
            print(file_path)
            if os.path.isfile(file_path):
                print("Attempting to copy")
                shutil.copy(file_path, target_dir)
                print(f"{file} copied to {target_dir}")
            elif os.path.isdir(file_path):
                print(f"{file} is a directory")
                copy_dir_to_other(file_path, f"{target_dir}/{file}")
    except Exception as e:
        print(f'Error: {e}')
def main():
    copy_dir_to_other("./static", "./public")
main()