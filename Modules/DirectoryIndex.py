import json
import os
import pickle

from Objects.Metadata import Metadata
from Utils import DirectoryUtils, IOUtils


# Write to the disk the structure such that will be
# persistent.
def writePersistentStructure(filename, structure):
    writeSerializer = open(filename, "wb")
    pickle.dump(structure, writeSerializer)
    writeSerializer.close()
    return


# Load a persistent data structure into memory.
def readPersistentStructure(filename):
    readSerializer = open("C:\\Users\\Elias\\Desktop\\RealTimeReplicationTool\\Indexes\\directoriesIdx.idx", "rb")
    inMemoryStructure = pickle.load(readSerializer)
    return inMemoryStructure



list = DirectoryUtils.readDirectoryMetadataObj("\\DataServer")

print(len(list))

path = "C:\\Users\\Elias\\Desktop\\RealTimeReplicationTool\\Indexes\\directoriesIdx.idx"

entry = pickle.dumps(list)
writePersistentStructure(path, entry)

memoryStructure = readPersistentStructure(path)
newObj = pickle.loads(memoryStructure)

print(len(newObj))
# IOUtils.write("C:\\Users\\Elias\\Desktop\\RealTimeReplicationTool\\Indexes\\directoriesIdx.idx", str(entry))
