from os import walk
from distutils.dir_util import copy_tree
import checksumdir
import shutil
import json

from FilesUtils import zipFiles


def readConfigFile():
    confValues = dict()

    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
        confValues['sourcePath'] = data['files']['host_path']
        confValues['destPath'] = data['files']['dest_path']

    return confValues


def readDirectoryMetadata(directory):
    f = []
    for (dirpath, dirnames, filenames) in walk(directory):
        f.extend(filenames)

    return f

print('Files Synchonization Tools is running...')

conf = readConfigFile()

mypath = conf['sourcePath']
destPath = conf['destPath']

hash = checksumdir.dirhash(mypath)

print(hash)

metadata = readDirectoryMetadata(mypath)

zipFiles(mypath, destPath)

shutil.make_archive('C:\\Users\\HpServer\Pictures', 'zip', str('C:\\Users\\HpServer\\Desktop\\BackupTesting\\'))
# shutil.unpack_archive(str('C:\\Users\\Elias\\Desktop\\testBackUp\\testing.zip'), str(destPath), 'zip')

print('Finished...')

# copy_tree(mypath, destPath)
