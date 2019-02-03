from Utils.ReplicationModule import discoverDirectoryFiles

path = 'Y:\\'
files = discoverDirectoryFiles(path)

print(len(files))

sub = 'java'
print("\n".join(s for s in files if sub.lower() in s.lower()))