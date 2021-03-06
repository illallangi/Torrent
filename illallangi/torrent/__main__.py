from sys import stderr

from click import Choice as CHOICE, Path as PATH, STRING, argument, group, option

from illallangi.torrentapi import API as TORRENT_API

from loguru import logger

from notifiers.logging import NotificationHandler


@group()
@option('--log-level',
        type=CHOICE(['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'SUCCESS', 'TRACE'],
                    case_sensitive=False),
        envvar='HARVESTR_LOG_LEVEL',
        default='DEBUG')
@option('--slack-webhook',
        type=STRING,
        envvar='SLACK_WEBHOOK',
        default=None)
@option('--slack-username',
        type=STRING,
        envvar='SLACK_USERNAME',
        default='Harvestr')
@option('--slack-format',
        type=STRING,
        envvar='SLACK_FORMAT',
        default='{message}')
def cli(log_level, slack_webhook, slack_username, slack_format):
    logger.remove()
    logger.add(stderr, level=log_level)

    if slack_webhook:
        params = {
            "username": slack_username,
            "webhook_url": slack_webhook
        }
        slack = NotificationHandler("slack", defaults=params)
        logger.add(slack, format=slack_format, level="SUCCESS")


@cli.command(name='import')
@argument('paths',
          type=PATH(exists=True,
                    file_okay=True,
                    dir_okay=False,
                    writable=False,
                    readable=True,
                    resolve_path=True,
                    allow_dash=False),
          required=True,
          nargs=-1)
def import_torrents(paths):
    api = TORRENT_API()
    for path in paths:
        api.import_torrent(path)


@cli.command(name='list')
def list_torrents():
    api = TORRENT_API()
    for torrent_file in api.get_torrents():
        logger.info('{}: {}', torrent_file.hash, torrent_file.announce_list)


if __name__ == "__main__":
    cli()
