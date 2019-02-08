from os import walk

import checksumdir

from Objects.Metadata import Metadata


def readDirectoryMetadata(directory):
    f = []

    for (dirpath, dirnames, filenames) in walk(directory):
        f.extend(filenames)

    return f


def readDirectoryMetadataObj(directory):
    metadataList = []
    for (dirpath, dirnames, filenames) in walk(directory):
        for fileRow in filenames:
            row = Metadata(dirpath, fileRow, -1)
            metadataList.append(row)
        for fileRow in dirnames:
            row = Metadata(dirpath, fileRow, -1)
            metadataList.append(row)

    return metadataList
