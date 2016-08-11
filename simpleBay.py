import extractors
import simpleErrors

class SimpleBay:
    def __init__(self, downloadPictures=True):
        self.downloadPictures = downloadPictures
        self.extractorList = extractors.genExtractors()
        self.genExtractorNames()

    def genExtractorNames(self):
        self.extractorNames = []
        for extractor in self.extractorList:
            self.extractorNames.append(extractor.name)

    def getExtractorByName(self, extractorName):
        for extractor in self.extractorList:
            if extractor.name == extractorName:
                return extractor
        raise simpleErrors.ExtractorNotFoundError()

    def getSearchResults(self, listSearchTriples):
        result = []
        for extractorName, keyword, ammount in listSearchTriples:
            extractor = self.getExtractorByName(extractorName)
            extractor.downloadPictures = self.downloadPictures
            ad = extractor.extract(keyword, ammount)
            result += ad
        if len(result) == 0:
            raise simpleErrors.NoResultsError
        else:
            return result
