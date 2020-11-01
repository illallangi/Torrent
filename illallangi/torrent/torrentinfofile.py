from loguru import logger


class TorrentInfoFile(object):
    def __init__(self, dictionary, encoding, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dictionary = dictionary
        self.encoding = encoding
        for key in self.dictionary.keys():
            if key not in self.keys:
                logger.warning(f'Unhandled key in {__name__}: {key}')

    @property
    def keys(self):
        return [
            b'path',
            b'length'
        ]

    @property
    def path(self):
        return self.dictionary.get(b'path').decode(self.encoding or 'UTF-8') if b'path' in self.dictionary else None

    @property
    def length(self):
        return self.dictionary.get(b'length') if b'length' in self.dictionary else None
