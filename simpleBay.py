import extractors
import simpleErrors
from operator import itemgetter

class SimpleBay:
    def __init__(self, downloadPictures=True, sort="date"):
        self.downloadPictures = downloadPictures
        self.sort = sort
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
            print("Keyword: " + keyword.replace("%20", " ") + "\t\t\t\tAmmount: " + str(ammount))
        for extractor in self.extractorList:
            for keyword, ammount, keywordID in listSearchTouples:
                extractor.downloadPictures = self.downloadPictures
                ad = extractor.extract(keyword, ammount, keywordID, self.downloadPictures)
                result += ad
        if len(result) == 0:
            raise simpleErrors.NoResultsError
        else:
            if self.sort == "date":
                return sorted(result, key=itemgetter("date"), reverse=True)
            else:
                return result
