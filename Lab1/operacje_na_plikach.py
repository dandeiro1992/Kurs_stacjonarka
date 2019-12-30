import os


def funkcja(path):
    with open(path,'r', encoding='utf-8') as f:
        line = f.read()
        print(len(line.split()))
        f.close()


path = os.getcwd() + "/mydata.txt"

print(path)

if os.path.isfile(path):
    print('File %s exists' % path)
else:
    print("Creating a file %s" % path)
    open(path, 'x').close()
    print("file %s created" % path)

funkcja(path)
