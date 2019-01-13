from os import walk
from distutils.dir_util import copy_tree
import checksumdir
import shutil

print('Files Synchonization Tools is running...')

mypath = 'C:\\Users\\Elias\\Pictures\\'
destPath = 'C:\\Users\\Elias\\Desktop\\testBackUp'
# hash = checksumdir.dirhash(mypath)

# print(hash)

shutil.make_archive('C:\\Users\\Elias\\Desktop\\testBackUp\\testing', 'zip', mypath)
shutil.unpack_archive(str('C:\\Users\\Elias\\Desktop\\testBackUp\\testing.zip'), str(destPath), 'zip')

print('Finished...')

# f = []
# for (dirpath, dirnames, filenames) in walk(mypath):
#     f.extend(filenames)
#     break
#
#     print(f)

# copy_tree(mypath, destPath)
