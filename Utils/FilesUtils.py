import shutil
import json
from os import walk


def zipFiles(sourcePath, destPath, currentTimestap):
    finalSourcePath = str(sourcePath) + '_' + str(currentTimestap).replace(':', '_')

    shutil.make_archive(finalSourcePath, 'zip', str(destPath))
    return


def unzipFiles(sourcePath, destPath):
    shutil.unpack_archive(str(sourcePath), str(destPath), 'zip')
    return


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
