import ConfigParser


class ConfigItems:
    "Helper to load config values from config file"

    _cfg = None

    def __init__(self, appPath, configName):
        # load config file
        self._cfg = ConfigParser.ConfigParser()
        self._cfg.read("%s/%s.ini" % ((appPath), (configName),) )

    def get(self, section, key):
        return self._cfg.get(section, key)
