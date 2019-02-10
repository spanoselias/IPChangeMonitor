from Utils.FilesUtils import readConfigFile
from Modules.ReplicationModule import replicate

print('Files Synchonization Tools is running...')

conf = readConfigFile()

sourcePath = conf['sourcePath']
destPath = conf['destPath']
copyPath = conf['copyPath']

# Reading metadata of files.
#metadataList = readDirectoryMetadataObj(mypath)

replicate(copyPath, destPath)

print('Finished...')

# copy_tree(mypath, destPath)
