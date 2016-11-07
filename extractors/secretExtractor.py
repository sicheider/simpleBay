from .superExtractor import SuperExtractor
from bs4 import BeautifulSoup

import requests
import os
import time
import datetime

class SecretExtractorIE(SuperExtractor):
    def __init__(self):
        self.getInfoFromSecretFile()
        self.itemsPerSide = 25
        self.checkCache()

    def getInfoFromSecretFile(self):
        try:
            secretfile = open("secretfile.txt", "r")
            info = secretfile.read().splitlines()
            self.name = info[0]
            self.baseUrl = info[1]
            self.sideSplitter = info[2]
            self.urlEnding = info[3]
            secretfile.close()
        except IOError:
            print("Secretfile not found!")
        except IndexError:
            print("Invalid secretfile!")

    def genUrl(self, keyword, sideNumber):
        result = (self.baseUrl +
                self.sideSplitter +
                str(sideNumber) +
                "/" +
                keyword +
                self.urlEnding)
        print("Opening " + result + "!")
        return result

    def getHtmlContent(self, url):
        request = requests.get(url)
        return request.text

    def getDate(self, date):
        now = datetime.datetime.now()
        if "Heute" in date:
            hour = int(date.split(",")[1].split(":")[0])
            minute = int(date.split(",")[1].split(":")[1])
            return datetime.datetime(now.year,
                                     now.month,
                                     now.day,
                                     hour,
                                     minute)
        elif "Gestern" in date:
            hour = int(date.split(",")[1].split(":")[0])
            minute = int(date.split(",")[1].split(":")[1])
            yesterday = now - datetime.timedelta(days=1)
            return datetime.datetime(yesterday.year,
                                    yesterday.month,
                                    yesterday.day,
                                    hour,
                                    minute)
        else:
            year = int(date.split(".")[2])
            month = int(date.split(".")[1])
            day = int(date.split(".")[0])
            return datetime.datetime(year, month, day)


    def getAds(self, htmlContent):
        result = []
        soup = BeautifulSoup(htmlContent, "html.parser")
        articles = soup.find_all("article")
        for article in articles:
            div = article.contents[1].contents[1]
            try:
                url = self.baseUrl + div['data-href']
                imgSrc = div['data-imgsrc']
                title = div['data-imgtitle']
                price = article.contents[5].contents[1].string
                date = article.contents[7].contents[0].string
                if date == "\n":
                    continue
                else:
                    date = self.getDate(str(date))
                if self.downloadPictures:
                    imgPath = self.getPictureFromWeb(imgSrc, self.genPictureName(imgSrc))
                else:
                    imgPath = ""
                if not url in self.extractedAds:
                    result.append({'url' : url,
                                   'imgSrc' : imgSrc,
                                   'title' : title,
                                   'price' : price,
                                   'extractor' : self.name,
                                   'imgPath' : imgPath,
                                   'date' : date,
                                   'keywordID' : self.keywordID,
                                   'keyword' : self.keyword})
                    self.extractedAds.append(url)
                    if len(self.extractedAds) == self.ammount:
                        return result
            except KeyError as e:
                continue
            except IndexError as e:
                continue
        return result

    def genPictureName(self, pictureUrl):
        ext = os.path.splitext(pictureUrl)[1]
        name = pictureUrl.split("/")[7]
        return name + ext

    def extract(self, keyword, ammount, keywordID, downloadPictures):
        result = []
        self.extractedAds = []
        self.ammount = ammount
        self.keywordID = keywordID
        self.keyword = keyword
        pageCount = ammount // self.itemsPerSide
        if pageCount == 0:
            pageCount = 1
        for i in range(1, pageCount + 1):
            htmlContent = self.getHtmlContent(self.genUrl(keyword, i))
            if "Es wurden leider keine Anzeigen" in htmlContent:
                return result
            if len(self.extractedAds) == ammount:
                return result
            result += self.getAds(htmlContent)
            i += 1
        return result
