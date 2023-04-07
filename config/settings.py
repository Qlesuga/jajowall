from . import config
import pickle

class Settings():
    path = "config/settings.pckl"
    def loadSettings(self):
        try:
            with open(Settings.path,"rb")as f:
                settings = pickle.load(f)
            config.volume.volume = settings["volumeValue"]
            config.autostart = settings["autostart"]
        except FileNotFoundError:
            self.saveSettings()
            self.loadSettings()

    def saveSettings(self):
        settings = {
            "volumeValue": config.volumeValue,
            "autostart": config.autostart
        }
        with open(Settings.path,"wb")as f:
            settings = pickle.dump(settings,f)
