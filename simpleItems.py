class SimpleItem:
  def __init__(self):
    self.keyword = None
    self.categoryId = None
    self.locationStr = None
    self.locationId = None
    self.adType = None
    self.radius = None

    """getter, setter"""
    def getKeyword(self):
      return self.keyword

    def setKeyword(self, _keyword):
      self.keyword = _keyword

    def getCategoryId(self):
      return self.categoryId

    def setCategoryId(self, _categoryId):
      self.categoryId = _categoryId

    def getLocationStr(self):
      return self.locationStr

    def setLocationStr(self, _locationStr):
      self.locationStr = _locationStr

    def getLocationId(self):
      return self.locationId

    def setLocationId(self, _locationId):
      self.locationId = _locationId

    def getAdType(self):
      return self.adType

    def setAdType(self, _adType):
      self.adType = _adType

    def getRadius(self):
      return self.radius

    def setRadius(self, _radius):
      self.radius = _radius

class SearchItem(SimpleItem):
  def __init__(self):
    super().__init__()
    self.minPrice = None
    self.maxPrice = None
    self.action = None
    self.sortingField = None
    self.itemsPerRequest = None
    self.posterType = None

    def getMaxPrice(self):
      return self.maxPrice

    def setMaxPrice(self, _maxPrice):
      self.maxPrice = _maxPrice

    def getMinPrice(self):
      return self.minPrice

    def setMinPrice(self, _minPrice):
      self.minPrice = _minPrice

    def getAction(self):
      return self.action

    def setAction(self, _action):
      self.action = _action

    def getSortingField(self):
      return self.sortingField

    def setSortingField(self, _sortingField):
      self.sortingField = _sortingField

    def getItemsPerRequest(self):
      return self.itemsPerRequest

    def setItemsPerRequest(self, _itemsPerRequest):
      self.itemsPerRequest = _itemsPerRequest

    def getPosterType(self):
      return self.posterType

    def setPosterType(self, _posterType):
      self.posterType = _posterType

class Ad(SimpleItem):
  def __init__(self):
    super().__init__()
    self.adId = None
    self.adUrl = None
    self.adImagePath = None
    self.adPrice = None
    self.adPhone = None
    self.adStatus = None

    def getAdId(self):
      return self.adId

    def setAdId(self, _adId):
      self.adId = _adId

    def getAdUrl(self):
      return self.adUrl

    def setAdUrl(self, _adUrl):
      self.adUrl = _adUrl

    def getAdImagePath(self):
      return self.adImagePath

    def setAdImagePath(self, _adImagePath):
      self.adImagePath = _adImagePath

    def getAdPrice(self):
      return self.adPrice

    def setAdPrice(self, _adPrice):
      self.adPrice = _adPrice

    def getAdPhone(self):
      return self.adPhone

    def setAdPhone(self, _adPhone):
      self.adPhone = _adPhone

    def getAdStatus(self):
      return self.adStatus

    def setAdStatus(self, _adStatus):
      self.adStatus  = _adStatus
