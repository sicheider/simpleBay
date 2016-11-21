import extractors
import simpleErrors
from operator import itemgetter

class SimpleBay:
    def __init__(self, listNonKeywords,
            downloadPictures = True,
            sort= "date",
            filterNonKeywords = True,
            filterDoubleArticles = True):
        self.downloadPictures = downloadPictures
        self.sort = sort
        self.filterNonKeywords = filterNonKeywords
        self.filterDoubleArticles = filterDoubleArticles
        self.listNonKeywords = listNonKeywords
        self.extractorList = extractors.genExtractors()
        self.genExtractorNames()

    def genExtractorNames(self):
        self.extractorNames = []
        for extractor in self.extractorList:
            self.extractorNames.append(extractor.name)

    def getSearchResults(self, listSearchTouples):
        result = []
        print("Searching for:")
        for keyword, ammount, keywordID in listSearchTouples:
            print("Keyword: " + keyword.replace("%20", " "))
        for extractor in self.extractorList:
            for keyword, ammount, keywordID in listSearchTouples:
                ad = extractor.extract(keyword, ammount, keywordID, self.downloadPictures)
                result += ad
        if len(result) == 0:
            raise simpleErrors.NoResultsError
        result = self.filterResult(result)
        result = self.sortResult(result)
        return result
        
    def sortResult(self, searchResults):
        if self.sort == "date":
            return sorted(searchResults, key=itemgetter("date"), reverse = True)
        if self.sort == "price":
            return sorted(searchResults, key=itemgetter("price"), reverse = True)
        else:
            return searchResults

    def filterResult(self, searchResults):
        if self.filterDoubleArticles:
            run = True
            while run:
                listUrls = []
                found = False
                run = False
                for searchResult in searchResults:
                    for url in listUrls:
                        if searchResult["url"] == url:
                            found = True
                            run = True
                    if found:
                        searchResults.remove(searchResult)
                    else:
                        listUrls.append(searchResult["url"])
                    found = False

        if self.filterNonKeywords:
            run = True
            while run:
                run = False
                for searchResult in searchResults:
                    for nonKeyword in self.listNonKeywords:
                        if nonKeyword.lower() in searchResult["title"].lower():
                            try:
                                searchResults.remove(searchResult)
                                run = True
                            except ValueError:
                                continue
        return searchResults
