import checksumdir

from Utils.FilesUtils import readDirectoryMetadata, zipFiles


def replicate(mypath, destPath):
    # Hash code for the files to be copied in order to verify
    # that
    hash = checksumdir.dirhash(mypath)
    print(hash)
    metadata = readDirectoryMetadata(mypath)
    zipFiles(destPath, mypath)

    return metadata


def discoverDirectoryFiles(directoryPath):
    metadata = readDirectoryMetadata(directoryPath)

    return metadata
