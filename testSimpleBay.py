import simpleBay
import simpleExceptions

s = simpleBay.SimpleBay()
print(s.extractorList)
print(s.getExtractorNames())
print(s._getExtractorByName("TestExtractor"))
try:
    s._getExtractorByName("TesstExtractor")
except simpleExceptions.ExtractorNotFoundException:
    print("ExtractorNotFound")
print(s.getSearchResults(["TestExtractor", "TestExtractor"],
                         ["hallo", "welt"],
                         [1, 2]))
s.getSearchResults("TesstExtractor",
                   ["hallo", "welt"],
                   [1, 2])
