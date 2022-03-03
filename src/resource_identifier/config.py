from singleton_decorator import singleton
from pathlib import Path


@singleton
class ZamResourceIdentifierConfig(object):
    def __init__(self, config=None) -> None:
        import json

        default_config_path = Path(__file__).parent / 'default_config.json'
        with open(default_config_path, 'r') as f:
            self.config = json.load(f)


def load_config(config):
    return ZamResourceIdentifierConfig(config)


ZAM_CORE_CONFIG = load_config(None)
