from . import config
import pickle

class Settings():
    path = "config/settings.pckl"
    def loadSettings(self):
        try:
            with open(Settings.path,"rb")as f:
                try:
                    settings = pickle.load(f)
                except (EOFError,pickle.UnpicklingError):
                    self.saveSettings()
                else:
                    try:
                        config.volume.volume = settings["volumeValue"]
                    except KeyError:
                        pass
                    try:
                        config.autostart = settings["autostart"]
                    except KeyError:
                        pass
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
