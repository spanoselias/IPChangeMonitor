import os
import pickle

from Utils import DirectoryUtils, IOUtils, LoggingUtils


# Write to the disk the structure such that will be
# persistent.
from Utils.FilesUtils import readConfigFile


def writePersistentStructure(filename, structure):
    try:
        writeSerializer = open(filename, "wb")
        pickle.dump(structure, writeSerializer)
    except:
        print("Unable to write persistent data structure in the following location: {}".format(filename))

    writeSerializer.close()
    return


# Load a persistent data structure into memory.
def readPersistentStructure(filename):
    dirname = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Indexes'))
    path = os.path.join(dirname, filename)

    try:
        readSerializer = open(path, "rb")
        inMemoryStructure = pickle.load(readSerializer)
    except:
        print("Unable to read persistent data structure in the following location: {}".format(path))

    return inMemoryStructure

shouldRead = True

if shouldRead:

    conf = readConfigFile()
    readPath = conf['copyPath']

    destPath = conf['destPath']
    LoggingUtils.log('Start reading the following directory: {}'.format(readPath))
    list = DirectoryUtils.readDirectoryMetadataObj(readPath)
    print(len(list))

    # Retrieve the current path.
    dirname = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Indexes'))
    path = os.path.join(dirname, 'directoriesIdx.idx')

    entry = pickle.dumps(list)
    writePersistentStructure(path, entry)

else:
    memoryStructure = readPersistentStructure('directoriesIdx.idx')
    newObj = pickle.loads(memoryStructure)
    print(len(newObj))
