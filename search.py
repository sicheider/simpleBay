class Search():
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

        pass

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

class Search():
    def __init__(self):
        self.listDeletedAds = []
        self.listMarkedAds = []
        self.listNewAds = []
        self.listSearchItems = []
        pass

    def syncAds(self):
        pass

    def markAd(self, ad):
        pass

    def delteAd(self, ad):
        pass

    def saveSearch(self):
        pass

    def loadSearch(self, fileObject):
        pass
