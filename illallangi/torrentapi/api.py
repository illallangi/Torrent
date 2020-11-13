from fnmatch import translate
from os import makedirs, walk
from os.path import join, splitext
from re import IGNORECASE, compile, match
from shutil import copyfile

from click import get_app_dir

from loguru import logger

from .torrentfile import TorrentFile


class API(object):
    def __init__(self, cache=True, config_path=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_path = get_app_dir(__package__) if not config_path else config_path
        makedirs(self.config_path, exist_ok=True)

    def get_torrent(self, hash):
        return TorrentFile(join(self.config_path, hash + '.torrent'))

    def get_torrents(self):
        reg_expr = compile(translate('*.torrent'), IGNORECASE)
        for _root, _dirs, files in walk(self.config_path, topdown=True):
            for j in [f for f in files if match(reg_expr, f)]:
                yield self.get_torrent(splitext(j)[0])

    def import_torrent(self, path):
        torrent = TorrentFile(path)
        logger.info('Importing {} ({})', path, torrent.hash)
        copyfile(path, join(self.config_path, torrent.hash + '.torrent'))
