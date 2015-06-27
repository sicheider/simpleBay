import simpleItems

class Translator:
    """Translator translates ad dictionaries in ad objects and vice versa;
    Translator translates searchItem dictionaries in searchItem objects and vice versa"""
    def __init(self):
        self.ad = simpleItems.Ad()
        self.searchItem = simpleItems.SearchItem()
        self.adDict = {}
        self.searchItemDict = {}
        pass

    def adToAdDict(self, _ad):
        self.ad = _ad
        self.adDict = {'keyword' : self.ad.getKeyword(),
                        'categoryId' : self.ad.getCategoryId(),
                        'locationStr' : self.ad.getLocationStr(),
                        'locationId' : self.ad.getLocationId(),
                        'adType' : self.ad.getAdType(),
                        'radius' : self.ad.getRadius(),
                        'adId' : self.ad.getAdId(),
                        'adUrl' : self.ad.getAdUrl(),
                        'adImagePath' : self.ad.getAdImagePath(),
                        'adPrice' : self.ad.getAdPrice(),
                        'adPhone' : self.ad.getAdPhone(),
                        'adStatus' : self.ad.getAdStatus()}
        return self.adDict

    def adDictToAd(self, _adDict):
        self.adDict = _adDict
        self.ad.setKeyword(self.adDict['keyword'])
        self.ad.setCategoryId(self.adDict['categoryId'])
        self.ad.setLocationStr(self.adDict['locationStr'])
        self.ad.setLocationId(self.adDict['locationId'])
        self.ad.setAdType(self.adDict['adType'])
        self.ad.setRadius(self.adDict['radius'])
        self.ad.setAdId(self.adDict['adId'])
        self.ad.setAdUrl(self.adDict['adUrl'])
        self.ad.setAdImagePath(self.adDict['adImagePath'])
        self.ad.setAdPrice(self.adDict['adPrice'])
        self.ad.setAdPhone(self.adDict['adPhone'])
        self.ad.setAdStatus(self.adDict['adStatus'])
        return self.ad
        
    def searchItemToSearchItemDict(self, _searchItem):
        self.searchItem = _searchItem
        self.searchItemDict = {'keyword' : self.searchItem.getKeyword(),
                                'categoryId' : self.searchItem.getCategoryId(),
                                'locationStr' : self.searchItem.getLocationStr(),
                                'locationId' : self.searchItem.getLocationId(),
                                'radius' : self.searchItem.getRadius(),
                                'adType' : self.searchItem.getAdType(),
                                'minPrice' : self.searchItem.getMinPrice(),
                                'maxPrice' : self.searchItem.getMaxPrice(),
                                'action' : self.searchItem.getAction(),
                                'sortingField' : self.searchItem.getSortingField(),
                                'itemsPerRequest' : self.searchItem.getItemsPerRequest(),
                                'posterType' : self.searchItem.getPosterType()}
        return self.searchItemDict

    def searchItemDictToSearchItem(self, _searchItemDict):
        self.searchItemDict = _searchItemDict
        self.searchItem.setKeyword(self.searchItemDict['keyword'])
        self.searchItem.setCategoryId(self.searchItemDict['categoryId'])
        self.searchItem.setLocationId(self.searchItemDict['locationId'])
        self.searchItem.setLocationStr(self.searchItemDict['locationStr'])
        self.searchItem.setAdType(self.searchItemDict['adType'])
        self.searchItem.radius(self.searchItemDict['radius'])
        self.searchItem.setMinPrice(self.searchItemDict['minPrice'])
        self.searchItem.setMaxPrice(self.searchItemDict['maxPrice'])
        self.searchItem.setAction(self.searchItemDict['action'])
        self.searchItem.setSortingField(self.searchItemDict['sortingField'])
        self.searchItem.setItemsPerRequest(self.searchItemDict['itemsPerRequest'])
        self.searchItem.setPosterType(self.searchItemDict['posterType'])
        return self.searchItem
