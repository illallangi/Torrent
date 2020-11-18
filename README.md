# TorrentAPI
[![Docker Pulls](https://img.shields.io/docker/pulls/illallangi/torrentapi.svg)](https://hub.docker.com/r/illallangi/torrentapi)
[![Image Size](https://images.microbadger.com/badges/image/illallangi/torrentapi.svg)](https://microbadger.com/images/illallangi/torrentapi)
![Build](https://github.com/illallangi/TorrentAPI/workflows/Build/badge.svg)

Tool and Python bindings to collect and manage .torrent files

## Installation

```shell
pip install git+git://github.com/illallangi/TorrentAPI.git
```

## Usage

```shell
$ torrent-tool --help
Usage: torrent-tool [OPTIONS] COMMAND [ARGS]...

Options:
  --log-level [CRITICAL|ERROR|WARNING|INFO|DEBUG|SUCCESS|TRACE]
  --slack-webhook TEXT
  --slack-username TEXT
  --slack-format TEXT
  --help                          Show this message and exit.

Commands:
  import
  list
```
