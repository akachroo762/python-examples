import zipfile
import os
import re

# f = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
# f.extractall('example')
# print(os.getcwd())


pattern = r'\d{3}-\d{3}-\d{4}'
folder_path = os.path.abspath("example\\extracted_content")
folders = os.listdir(folder_path)
folders.pop(2)
print(folders)
for folder in folders:
    # with open("C:\\Users\\akach\\Downloads\\PythonCourse\\challenge_zip\\example\\extracted_content\\folder\\r'*txt$'", 'r') as text_files:
    #     phone_number = text_files.read(re.search(pattern, text_files))
    os.chdir(folder_path + "\\" + folder + "\\")
    files = os.listdir()
    for file in files:
        c = open(file, 'r')
        line = c.readline()
        try:
            phone_number = re.search(pattern, line)
            print(f"A phone number was found in {file}: " + phone_number.group())
            continue
        except:
            pass
        c.close()
