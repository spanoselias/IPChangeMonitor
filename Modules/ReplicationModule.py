import datetime

import checksumdir

from Utils import DirectoryUtils
from Utils.FilesUtils import zipFiles

def replicate(mypath, destPath):
    # Hash code for the files to be copied in order to verify
    # that
    # hash = checksumdir.dirhash(mypath)

    print(hash)
    metadata = DirectoryUtils.readDirectoryMetadataObj(mypath)

    zipFiles(destPath, mypath, datetime.datetime.now().isoformat())

    return metadata

def discoverDirectoryFiles(directoryPath):
    metadata = DirectoryUtils.readDirectoryMetadata(directoryPath)

    return metadata

