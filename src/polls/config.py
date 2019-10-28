import os

from simple_settings import settings


def db_provider_config():
    config = {'provider': settings.provider}
    if settings.provider == 'sqlite':
        config.update({
            'filename': os.environ['SQLITE_FILENAME'],
            'create_db': True,
        })
    return config
