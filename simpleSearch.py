import simpleParser
import simpleItems
import simpleTranslator

class Search():
    def __init__(self):
        self.parser = simpleParser.Parser()
        self.translator = simpleTranslator.Translator()
        self.tempSearchItem = simpleItems.SearchItem()
        self.tempAd = simpleItems.Ad()
        self.listTempDicts = []
        self.listTempAds = []
        self.listDeletedAds = []
        self.listPassedAds = []
        self.listMarkedAds = []
        self.listNewAds = []
        self.listSearchItems = []
        pass

    def syncAds(self):
        """gets all ads for all searchItems from Ebay -->
        compares all ads with past marked and deleted ads """
        #get all ads from ebay
        #store them in self.listTempAds
        for i in self.listSearchItems:
            self.listTempDicts = self.parser.getAllAds(self.translator.searchItemToSearchItemDict(i))
            for j in self.listTempDicts:
                self.tempAd = self.translator.adDictToAd(j)
                self.listTempAds.append(self.tempAd)
        #get all new ads and store them in listNewAds
        for i in self.listTempAds:
            if ((i not in self.listMarkedAds) and
                (i not in self.listDeletedAds) and
                (i not in self.listPassedAds)):
                i.setAdStatus('new')
                self.listNewAds.append(i)
        #get all passed ads and store them in listPassedAds
        for i in self.listMarkedAds:
            if i not in self.listTempAds:
                i.setAdStatus('passed')
                self.listPassedAds.append(i)
                self.listMarkedAds.remove(i)
        pass

    def markAd(self, _adDict):
        """removes an ad from current list and appends it to listMarkedAds"""
        self.tempAd = self.translator.adDictToAd(_adDict)
        if self.tempAd.getAdStatus == 'new':
            self.tempAd.setAdStatus('marked')
            self.listMarkedAds.append(self.tempAd)
            self.listNewAds.remove(self.tempAd)
        if self.tempAd.getAdStatus == 'deleted':
            self.tempAd.setAdStatus('marked')
            self.listMarkedAds.append(self.tempAd)
            self.listDeletedAds.remove(self.tempAd)
        pass

    def deleteAd(self, _adDict):
        """removes an ad from current list and appends it to listDeletedAds"""
        self.tempAd = self.translator.adDictToAd(_adDict)
        if self.tempAd.getAdStatus == 'new':
            self.tempAd.setAdStatus('deleted')
            self.listDeletedAds.append(self.tempAd)
            self.listNewAds.remove(self.tempAd)
        if self.tempAd.getAdStatus == 'marked':
            self.tempAd.setAdStatus('deleted')
            self.listDeletedAds.append(self.tempAd)
            self.listMarkedAds.remove(self.tempAd)
        pass

    def addSearchItem(self, _searchItemDict):
        """adds a searchItem to listSearchItems"""
        self.tempSearchItem = self.translator.searchItemDictToSearchItem(_searchItemDict)
        self.listSearchItems.append(self.tempSearchItem)
        pass

    def removeSearchItem(self, _searchItemDict):
        """removes a searchItem from listSearchItems"""
        self.tempSearchItem = self.translator.searchItemDictToSearchItem(_searchItemDict)
        self.listSearchItems.remove(self.tempSearchItem)
        pass

    def saveSearch(self, fileObject):
        """saves the search in fileObject"""
        pass

    def loadSearch(self, fileObject):
        """loades a search from fileObject"""
        pass
