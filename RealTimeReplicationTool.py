import checksumdir

from Utils.FilesUtils import readConfigFile
from Utils.ReplicationModule import replicate

print('Files Synchonization Tools is running...')

conf = readConfigFile()

mypath = conf['sourcePath']
destPath = conf['destPath']

replicate(mypath, destPath)

print('Finished...')

# copy_tree(mypath, destPath)
