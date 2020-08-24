import bencodepy


class BEncodedFile(object):
    def __init__(self, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file

    @property
    def binary(self):
        with open(self.file, "rb") as f:
            binary = f.read()
        return binary

    @property
    def dictionary(self):
        return bencodepy.decode(self.binary)

    @property
    def keys(self):
        return self.dictionary.keys()
