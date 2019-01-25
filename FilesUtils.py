import shutil

def zipFiles(sourcePath, destPath):
    shutil.make_archive(str(sourcePath), 'zip', str(destPath))
    return

def unzipFiles(sourcePath, destPath):
    shutil.unpack_archive(str(sourcePath), str(destPath), 'zip')
    return
