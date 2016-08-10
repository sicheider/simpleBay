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

    def getSearchResults(self, extractorNames, keywords, ammounts):
        result = []
        for extractorName, keyword, ammount in zip(extractorNames, keywords, ammounts):
            extractor = self.getExtractorByName(extractorName)
            extractor.downloadPictures = self.downloadPictures
            result += extractor.extract(keyword, ammount)
        return result
