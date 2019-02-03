import checksumdir

from FilesUtils import zipFiles, readConfigFile, readDirectoryMetadata

print('Files Synchonization Tools is running...')

conf = readConfigFile()

mypath = conf['sourcePath']
destPath = conf['destPath']

# Hash code for the files to be copied in order to verify
# that
hash = checksumdir.dirhash(mypath)
print(hash)

metadata = readDirectoryMetadata(mypath)

zipFiles(destPath, mypath)

print('Finished...')

# copy_tree(mypath, destPath)
