# import os

# dir=("AI")

# try:
#     os.makedirs(dir)
#     print(f'Folder Created : {dir}')
# except FileExistsError:
#     print(f"Folder already exits.")
# finally:
#     print("Code is Exicuted")

# cur_name="abc"
# new_name= "xyz"
# try:
#     os.rename(cur_name,new_name)
# except FileExistsError:
#     print("Folder not found")



# import shutil

# dir_del=("xyz")

# try:
#     shutil.rmtree(dir_del)
#     print("directory deleted")
# except FileNotFoundError:
#     print("File does not exist")
# except PermissionError:
#     print("Permission Denied")
# except Exception as e:
#     print(f'"An Error Occured" {e}')


# import os

# dir="adit"
# try:
#     os.makedirs(dir, exist_ok=True)

#     file_name="aadil.txt"

#     file_path=os.path.join(dir,file_name)

#     with open(file_path, "w") as file:
#         file.write("Hi,AADIL")
#         print(f"File: ' {file_name}' created sucessfully in '{dir}'")

# except Exception as e:
#     print(f'"An Error Occured" {e}')


# import os

# dir="."

# with os.scandir(dir) as entries:
#     print(f"contents of the folder are : '{dir}'")
#     for entry in entries:
#         print(entry.name)

                # OR
# import os
# dir=os.listdir()
# print("Content in folder : ",dir)


# import os
# dir=os.getcwd()
# print("Workimg folder is :" ,dir)


import shutil

# dir_copy=("adit")

# try:
#     shutil.copytree(dir_copy, "xyz")
#     print("Directory copied successfully")
# except Exception as e:
#     print(f'"An Error Occured" {e}')


# shutil.move()

# dir_move=("adit")

# try:
#     shutil.move(dir_move, "xyz")
#     print("Moved Successfully")
# except Exception as e:
#     print(f'"An Error Occured" {e}')



# shutil.rmtree()

dir_del=("xyz")

try:
    shutil.rmtree(dir_del, "xyz")
    print("directory deleted")
except Exception as e:
    print(f'"An Error Occured" {e}')