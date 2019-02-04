import datetime

from Utils.FilesUtils import readConfigFile, readDirectoryMetadata, readDirectoryMetadataObj
from Modules.ReplicationModule import replicate

print('Files Synchonization Tools is running...')

conf = readConfigFile()

mypath = conf['sourcePath']
destPath = conf['destPath']

# Reading metadata of files.
metadataList = readDirectoryMetadataObj(mypath)

replicate(mypath, destPath)

print('Finished...')

# copy_tree(mypath, destPath)
