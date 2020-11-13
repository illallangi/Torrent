from loguru import logger

from .torrentinfofile import TorrentInfoFile


class TorrentInfo(object):
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
            b'entropy',
            b'files',
            b'length',
            b'name',
            b'piece length',
            b'pieces',
            b'private',
            b'profiles',
            b'source',
            b'x_cross_seed',
        ]

    @property
    def entropy(self):
        return self.dictionary.get(b'entropy').decode(self.encoding or 'UTF-8') if b'entropy' in self.dictionary else None

    @property
    def files(self):
        return [TorrentInfoFile(x, self.encoding) for x in self.dictionary.get(b'files')] if b'files' in self.dictionary else None

    @property
    def length(self):
        return self.dictionary.get(b'length') if b'length' in self.dictionary else None

    @property
    def name(self):
        return self.dictionary.get(b'name').decode(self.encoding or 'UTF-8') if b'name' in self.dictionary else None

    @property
    def piece_length(self):
        return self.dictionary.get(b'piece length') if b'piece length' in self.dictionary else None

    @property
    def pieces(self):
        return self.dictionary.get(b'pieces').decode(self.encoding or 'UTF-8') if b'pieces' in self.dictionary else None

    @property
    def private(self):
        return self.dictionary.get(b'private').decode(self.encoding or 'UTF-8') if b'private' in self.dictionary else None

    @property
    def profiles(self):
        return self.dictionary.get(b'profiles').decode(self.encoding or 'UTF-8') if b'profiles' in self.dictionary else None

    @property
    def source(self):
        return self.dictionary.get(b'source').decode(self.encoding or 'UTF-8') if b'source' in self.dictionary else None
