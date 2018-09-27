import os

### python ChangeFolderContents.py

### change folders ###
os.chdir("C:\\Users\\Dennis\\Documents\\Python")

for filename in os.listdir("."):
    if filename.startswith("cheese_"):
        os.rename(filename, filename[7:])

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    f_one, f_two, f_three = file_name.split('_AreaTable')
    print(f_one)

print(os.getcwd())

### show contents of folder ###
# for f in os.listdir():
#     print (f)

### Split up file names and extentions into tuples ###
# for f in os.listdir():
#     print(os.path.splitext(f))

#### Print out only file name ###
# for f in os.listdir():
#     file_name, file_ext = os.path.splitext(f)
#     print(file_name)

### print file name section that's split up by - ###
# for f in os.listdir():
#     file_name, file_ext = os.path.splitext(f)
#     f_one, f_two, f_three = file_name.split('-')
#     print(f_one)
