from .superExtractor import SuperExtractor

class TestExtractorIE(SuperExtractor):
    def __init__(self):
        self.name = "TestExtractor"

    def extract(self, keywords, ammounts):
        self.checkCache()
        result = []
        for keyword, ammount in keywords, ammounts:
            result.append({'path' : 'path',
                          'description' : 'description',
                          'price' : 10,
                          'url' : 'url'})
        return result
