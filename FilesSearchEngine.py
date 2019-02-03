from Utils.ReplicationModule import discoverDirectoryFiles


def approximationStringMatching():
    f = []
    f.extend("\n".join(s for s in files if sub.lower() in s.lower()))
    return f


path = 'X:\\'
files = discoverDirectoryFiles(path)

print(len(files))

sub = 'java'
