from utils import plugins

PLUGIN_NAME = 'Adverts Plugin'
DISPLAY_NAME = 'Adverts'
DESCRIPTION = 'Uses hooks to display adverts in Janeway sites.'
AUTHOR = 'Andy Byers'
VERSION = '0.2'
SHORT_NAME = 'adverts'
MANAGER_URL = 'adverts_manager'
JANEWAY_VERSION = "1.7.0"


class AdvertsPlugin(plugins.Plugin):
    plugin_name = PLUGIN_NAME
    display_name = DISPLAY_NAME
    description = DESCRIPTION
    author = AUTHOR
    short_name = SHORT_NAME
    manager_url = MANAGER_URL

    version = VERSION
    janeway_version = JANEWAY_VERSION


def install():
    AdvertsPlugin.install()


def hook_registry():
    AdvertsPlugin.hook_registry()


def register_for_events():
    pass
