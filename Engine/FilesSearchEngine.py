from fuzzywuzzy import fuzz

from Modules.ReplicationModule import discoverDirectoryFiles
from Utils.FilesUtils import readConfigFile

def approximationStringMatching(keyword, files):
    f = []

    for filename in files:
        if fuzz.partial_ratio(filename, keyword) > 85:
            f.append(str(filename))

    return f

conf = readConfigFile()

mypath = conf['sourcePath']
destPath = conf['destPath']

files = discoverDirectoryFiles(mypath)

results = approximationStringMatching('Java 2017', files)

print('Program has finished.')
# print("\n".join(s for s in files if sub.lower() in s.lower()))
