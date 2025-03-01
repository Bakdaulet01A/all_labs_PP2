import os

def directories(path):
    dirs = [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))]
    for d in dirs:
        print(d)
    return dirs  # Вернём список директорий

def files(path):
    fls = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))]
    for f in fls:
        print(f)
    return fls  # Вернём список файлов

def all_items(path):
    return os.listdir(path)

specified_path = "C:/Users/huawei/Desktop/new_folder/labs/lab6/dir and files"

print("Directories:")
print(directories(specified_path))

print("\nFiles:")
print(files(specified_path))

print("\nAll Directories and Files:")
print(all_items(specified_path))
