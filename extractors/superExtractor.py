import os

class SuperExtractor:
    def checkCache(self):
        checkDir = os.path.curdir + "/Cache"
        try:
            os.makedirs(checkDir)
        except FileExistsError:
            pass
