import hashlib
import os
from os import walk


from Objects.Metadata import Metadata


def readDirectoryMetadata(directory):
    f = []

    for (dirpath, dirnames, filenames) in walk(directory):
        f.extend(filenames)

    return f


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def readDirectoryMetadataObj(directory):
    metadataList = []
    for (dirpath, dirnames, filenames) in walk(directory):
        for filename in filenames:
            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(dirpath + '\\' + filename)

            row = Metadata(filename, dirpath, mtime)
            metadataList.append(row)
        # for filename in dirnames:
        #     row = Metadata(dirpath, filename, -1)
        #     metadataList.append(row)

    return metadataList
