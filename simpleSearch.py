import simpleParser

"""Class wich stores one specific search item"""
class SearchItem():
    def __init__(self):
        self.keyword = None
        self.categoryId = None
        self.minPrice = None
        self.maxPrice = None
        self.action = None
        self.locationStr = None
        self.locationId = None
        self.radius = None
        self.sortingField = None
        self.adType = None
        self.itemsPerRequest = None
        self.posterType = None
        pass

    """getter, setter"""
    def getKeyword(self):
        return self.keyword

    def setKeyword(self, _keyword):
        self.keyword = _keyword
        pass

    def getCategoryId(self):
        return self.categoryId

    def setCategoryId(self, _categoryId):
        self.categoryId = _categoryId
        pass

    def getMaxPrice(self):
        return self.maxPrice

    def setMaxPrice(self, _maxPrice):
        self.maxPrice = _maxPrice
        pass

    def getMinPrice(self):
        return self.minPrice

    def setMinPrice(self, _minPrice):
        self.minPrice = _minPrice
        pass

    def getAction(self):
        return self.action

    def setAction(self, _action):
        self.action = _action
        pass

    def getLocationStr(self):
        return self.locationStr

    def setLocationStr(self, _locationStr):
        self.locationStr = _locationStr
        pass

    def getLocationId(self):
        return self.locationId

    def setLocationId(self, _locationId):
        self.locationId = _locationId
        pass

    def getSortingField(self):
        return self.sortingField

    def setSortingField(self, _sortingField):
        self.sortingField = _sortingField
        pass

    def getRadius(self):
        return self.radius

    def setRadius(self, _radius):
        self.radius = _radius
        pass

    def getAdType(self):
        return self.adType

    def setAdType(self, _adType):
        self.adType = _adType
        pass

    def getItemsPerRequest(self):
        return self.itemsPerRequest

    def setItemsPerRequest(self, _itemsPerRequest):
        self.itemsPerRequest = _itemsPerRequest
        pass

    def getPosterType(self):
        return self.posterType

    def setPosterType(self, _posterType):
        self.posterType = _posterType
        pass

    def getSearchItemDict(self):
        return {'keywords' : self.keyword,
                'categoryId' : self.categoryId,
                'locationStr' : self.locationStr,
                'locationId' : self.locationId,
                'radius' : self.radius,
                'sortingField' : self.sortingField,
                'adType' : self.adType,
                'posterType' : self.posterType,
                'action' : self.action,
                'maxPrice' : self.maxPrice,
                'minPrice' : self.minPrice,
                'itemsPerRequest' : self.itemsPerRequest}


"""Class wich stores specific ads"""
class Ad():
    def __init__(self):
        self.adId = None
        self.adName = None
        self.adUrl = None
        self.adImagePath = None
        self.adPrice = None
        self.adLocationStr = None
        self.adLocationId = None
        self.adRadius = None
        self.adPhone = None
        self.adStatus = None
        pass

    """getter, setter"""
    def getAdId(self):
        return self.adId

    def setAdId(self, _adId):
        self.adId = _adId
        pass

    def getAdName(self):
        return self.adName

    def setAdName(self, _adName):
        self.adName = _adName
        pass

    def getAdUrl(self):
        return self.adUrl

    def setAdUrl(self, _adUrl):
        self.adUrl = _adUrl
        pass

    def getAdImagePath(self):
        return self.adImagePath

    def setAdImagePath(self, _adImagePath):
        self.adImagePath = _adImagePath
        pass

    def getAdPrice(self):
        return self.adPrice

    def setAdPrice(self, _adPrice):
        self.adPrice = _adPrice
        pass

    def getAdLocationStr(self):
        return self.adLocationStr

    def setAdLocationStr(self, _adLocationStr):
        self.adLocationStr = _adLocationStr
        pass

    def getAdLocationId(self):
        return self.adLocationId

    def setAdLocationId(self, _adLocationId):
        self.adLocationId = _adLocationId
        pass

    def getAdPhone(self):
        return self.adPhone

    def setAdPhone(self, _adPhone):
        self.adPhone = _adPhone
        pass

    def getAdRadius(self):
        return self.adRadius

    def setAdRadius(self, _adRadius):
        self.adRadius = _adRadius
        pass

    def getAdStatus(self):
        return self.adStatus

    def setAdStatus(self, _adStatus):
        self.adStatus  = _adStatus
        pass

"""Controller class! Communicates with GUI-, CLI- API"""
class Search():
    def __init__(self):
        self.parser = simpleParser.Parser()
        self.listTempAds = []
        self.listDeletedAds = []
        self.listPassedAds = []
        self.listMarkedAds = []
        self.listNewAds = []
        self.listSearchItems = []
        pass

    def syncAds(self):
        #get all ads from ebay
        self.listTempAds = self.parser.getAllAds()
        #get all new ads and save them in listNewAds
        for i in self.listTempAds:
            if ((i not in self.listMarkedAds) and
                (i not in self.listDeletedAds) and
                (i not in self.listPassedAds)):
                i.setAdStatus('new')
                self.listNewAds.append(i)
        #get all passed ads and save them in listPassedAds
        for i in self.listMarkedAds:
            if i not in self.listTempAds:
                i.setAdStatus('passed')
                self.listPassedAds.append(i)
                self.listMarkedAds.remove(i)
        pass

    def markAd(self, ad):
        if ad.getAdStatus == 'new':
            ad.setAdStatus('marked')
            self.listMarkedAds.append(ad)
            self.listNewAds.remove(ad)
        if ad.getAdStatus == 'deleted':
            ad.setAdStatus('marked')
            self.listMarkedAds.append(ad)
            self.listDeletedAds.remove(ad)
        pass

    def deleteAd(self, ad):
        if ad.getAdStatus == 'new':
            ad.setAdStatus('deleted')
            self.listDeletedAds.append(ad)
            self.listNewAds.remove(ad)
        if ad.getAdStatus == 'marked':
            ad.setAdStatus('deleted')
            self.listDeletedAds.append(ad)
            self.listMarkedAds.remove(ad)
        pass

    def saveSearch(self, fileObject):
        pass

    def loadSearch(self, fileObject):
        pass
