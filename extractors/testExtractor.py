from .superExtractor import SuperExtractor

class TestExtractorIE(SuperExtractor):
    def __init__(self):
        self.name = "TestExtractor"

    def extract(self, keyword, ammount):
        self.checkCache()
        result = []
        result.append({'path' : 'path',
                      'description' : 'description',
                      'price' : 10,
                      'url' : 'url',
                      'extractorName' : self.name})
        return result
