import os
import datetime

def manageDirectoryFiles():
    currentDate = datetime.datetime.now().strftime("%Y-%m-%d")
    firstDir = os.path.join(os.getcwd(), currentDate)
    os.makedirs(firstDir, exist_ok=True)
    
    file_path = os.path.join(firstDir, "empty_file.txt")
    with open(file_path, 'w') as file:
        pass 
    
    secondDir = os.path.join(firstDir, "sub_directory")
    os.mkdir(secondDir)
    
    new_file_path = os.path.join(secondDir, "primer.txt")
    os.rename(file_path, new_file_path)

manageDirectoryFiles()
