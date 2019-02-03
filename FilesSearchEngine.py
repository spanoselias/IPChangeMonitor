from Utils.ReplicationModule import discoverDirectoryFiles
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def approximationStringMatching(search, files):
    f = []
    f.extend("\n".join(s for s in files if search.lower() in s.lower()))
    return f

path = 'Y:\\'

print(fuzz.partial_ratio("Catherine M. Gitau", "Catherine Gitau"))
# files = discoverDirectoryFiles(path)

# print(len(files))

# results = approximationStringMatching('Java', files)

sub = 'Java'
# print("\n".join(s for s in files if sub.lower() in s.lower()))
