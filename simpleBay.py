import extractors
import simpleExceptions

class SimpleBay:
    def __init__(self):
        self.extractorList = extractors.genExtractors()
        self._genExtractorNames()

    def _genExtractorNames(self):
        self.extractorNames = []
        for extractor in self.extractorList:
            self.extractorNames.append(extractor.name)

    def _getExtractorByName(self, extractorName):
        for extractor in self.extractorList:
            if extractor.name == extractorName:
                return extractor
        raise simpleExceptions.ExtractorNotFoundException()

    def getExtractorNames(self):
        return self.extractorNames

    def getSearchResults(self, extractorNames, keywords, ammounts):
        result = []
        for extractorName, keyword, ammount in zip(extractorNames, keywords, ammounts):
            extractor = self._getExtractorByName(extractorName)
            result += extractor.extract(keyword, ammount)
        return result
