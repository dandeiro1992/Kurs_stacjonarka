import os
path=os.getcwd()+'/'
print(path)

files_to_process = [path+"exec.py",path+"exec2.py"]
print(files_to_process)
for i in files_to_process:
    print(os.path.basename(i))
    with open(i,'r') as file:
        source=file.read()
        exec(source)