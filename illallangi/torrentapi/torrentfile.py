import datetime
import hashlib

import bencodepy

from loguru import logger

from .bencodedfile import BEncodedFile
from .torrentinfo import TorrentInfo


class TorrentFile(BEncodedFile):
    def __init__(self, file, *args, **kwargs):
        super().__init__(file, *args, **kwargs)
        for key in self.dictionary.keys():
            if key not in self.keys:
                logger.warning(f'Unhandled key in TorrentFile: {key}')

    def __str__(self):
        return f'{self.info.name}'

    def __repr__(self):
        return f'Torrent.TorrentFile("{self.file}")'

    @property
    def json(self):
        return {
            k: v
            for k, v in {
                'hash': self.hash,
                'announce-list': self.announce_list
            }.items()
            if v is not None
        }

    @property
    def keys(self):
        return [
            b'announce',
            b'announce-list',
            b'comment',
            b'created by',
            b'creation date',
            b'duration',
            b'encoded rate',
            b'encoding',
            b'err_callback',
            b'errors',
            b'height',
            b'info',
            b'log_callback',
            b'url-list',
            b'width',
            b'azureus_properties',
            b'comment.utf-8',
        ]

    @property
    def hash(self):
        return hashlib.sha1(bencodepy.encode(self.dictionary.get(b'info'))).hexdigest() if b'info' in self.dictionary else None

    @property
    def announce(self):
        return self.dictionary.get(b'announce').decode(self.encoding or 'UTF-8') if b'announce' in self.dictionary else None

    @property
    def announce_list(self):
        return [
            [
                url.decode(self.encoding or 'UTF-8')
                for url in tier
            ]
            for tier in self.dictionary.get(b'announce-list')
        ] if b'announce-list' in self.dictionary else [[self.announce]]

    @property
    def comment(self):
        return self.dictionary.get(b'comment').decode(self.encoding or 'UTF-8') if b'comment' in self.dictionary else None

    @property
    def created_by(self):
        return self.dictionary.get(b'created by').decode(self.encoding or 'UTF-8') if b'created by' in self.dictionary else None

    @property
    def creation_date(self):
        return datetime.datetime.utcfromtimestamp(self.dictionary.get(b'creation date')) if b'creation date' in self.dictionary else None

    @property
    def duration(self):
        return datetime.timedelta(seconds=self.dictionary.get(b'duration')) if b'duration' in self.dictionary else None

    @property
    def encoded_rate(self):
        return self.dictionary.get(b'encoded rate') if b'encoded rate' in self.dictionary else None

    @property
    def encoding(self):
        return self.dictionary.get(b'encoding').decode() if b'encoding' in self.dictionary else None

    @property
    def err_callback(self):
        return self.dictionary.get(b'err_callback').decode(self.encoding or 'UTF-8') if b'err_callback' in self.dictionary else None

    @property
    def errors(self):
        return [x.decode(self.encoding or 'UTF-8') for x in self.dictionary.get(b'errors')] if b'errors' in self.dictionary else None

    @property
    def height(self):
        return self.dictionary.get(b'height') if b'height' in self.dictionary else None

    @property
    def info(self):
        return TorrentInfo(self.dictionary.get(b'info'), self.encoding) if b'info' in self.dictionary else None

    @property
    def log_callback(self):
        return self.dictionary.get(b'log_callback').decode(self.encoding or 'UTF-8') if b'log_callback' in self.dictionary else None

    @property
    def url_list(self):
        return self.dictionary.get(b'url-list').decode(self.encoding or 'UTF-8') if b'url-list' in self.dictionary else None

    @property
    def width(self):
        return self.dictionary.get(b'width') if b'width' in self.dictionary else None
