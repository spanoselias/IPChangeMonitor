from os import walk

import checksumdir
from fuzzywuzzy import fuzz

from Modules.ReplicationModule import discoverDirectoryFiles
from Objects.Metadata import Metadata
from Utils.FilesUtils import readConfigFile

def approximationStringMatching(keyword, files):
    f = []

    for filename in files:
        if fuzz.partial_ratio(filename, keyword) >= 85:
            f.append(str(filename))

    return f

def readDirectoryMetadataObj(directory):

    metadataList = []
    for (dirpath, dirnames, filenames) in walk(directory):
        for fileRow in filenames:
            row = Metadata(dirpath, fileRow, checksumdir.dirhash(dirpath))
            metadataList.append(row)

    return metadataList

conf = readConfigFile()

mypath = conf['copyPath']
destPath = conf['destPath']

list = readDirectoryMetadataObj(mypath)
files = discoverDirectoryFiles(mypath)

results = approximationStringMatching('Java 2017', files)

print('Program has finished.')
# print("\n".join(s for s in files if sub.lower() in s.lower()))
