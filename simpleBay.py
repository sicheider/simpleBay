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

    def getSearchResults(self, extratorName, keywords, ammounts):
        extractor = self._getExtractorByName(extratorName)
        return extractor.extract(keywords, ammounts)
