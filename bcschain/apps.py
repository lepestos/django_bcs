from django.apps import AppConfig


class BcschainConfig(AppConfig):
    name = 'bcschain'

    def ready(self):
        from blockUpdater import updater
        updater.start()
