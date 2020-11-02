import zipfile
import os

dir = # your dir here
already = set() # saving previous files to eco mem
for i in range(1000):
    for root, dirs, files in os.walk(dir):
        # os.remove(dir + 'direction.txt') here you can delete garbadge files
        for file in files:
            if file[-3:] == 'zip' and file not in already:
                z = zipfile.ZipFile(dir + file, 'r')
                z.extractall(dir)
                z.close()
                already.add(file)
