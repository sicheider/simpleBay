import os
import requests
import shutil

class SuperExtractor:
    def _checkCache(self):
        self.cacheDir = os.path.curdir + "/Cache"
        try:
            os.makedirs(self.cacheDir)
        except FileExistsError:
            pass

    def _downloadPicture(self, url, fileName):
        r = requests.get(url, stream = True)
        filePath = self.cacheDir + "/" + fileName
        with open(filePath, "wb") as f:
            shutil.copyfileobj(r.raw, f)
        del r
        return filePath
