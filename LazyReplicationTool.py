from os import walk
from distutils.dir_util import copy_tree
import checksumdir
import shutil
import json

def readConfigFile():
    confValues = dict()

    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
        confValues['sourcePath'] = data['files']['host_path']
        confValues['destPath'] = data['files']['dest_path']

    return confValues

print('Files Synchonization Tools is running...')

conf = readConfigFile()

mypath = conf['sourcePath']
destPath = conf['destPath']
hash = checksumdir.dirhash(mypath)
print(hash)
# shutil.make_archive('C:\\Users\\Elias\\Desktop\\testBackUp\\testing', 'zip', mypath)
# shutil.unpack_archive(str('C:\\Users\\Elias\\Desktop\\testBackUp\\testing.zip'), str(destPath), 'zip')

print('Finished...')

# f = []
# for (dirpath, dirnames, filenames) in walk(mypath):
#     f.extend(filenames)
#     break
#
#     print(f)

# copy_tree(mypath, destPath)
