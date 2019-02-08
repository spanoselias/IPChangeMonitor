class Metadata:
    def __init__(self, filename, path, hashcode):
        self.filename = filename
        self.path = path
        self.hashcode = hashcode

        def __get_filename(self):
            return self.filename

        def __get_path(self):
            return self.path

        def __get_hashcode(self):
            return self.hashcode
