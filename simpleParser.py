import urllib.request
import urllib.parse


class Parser():
  def __init__(self):
    self.standardFields = {'keywords': "TEST",
                           'categoryId': "",
                           'locationStr': "",
                           'locationId': "",
                           'radius': "",
                           'sortingField': "SORTING_DATE",
                           'adType': "",
                           'posterType': "",
                           'pageNum': 1,
                           'action': "find",
                           'maxPrice': "",
                           'minPrice': ""}

  def urlGenerator(self, fields=None, baseUrl=None):
    """Take fields dictonary and returns URL string."""
    if not baseUrl:
      baseUrl = "http://kleinanzeigen.ebay.de/anzeigen/s-suchanfrage.html?"
    if not fields:
      fields = self.standardFields

    data = urllib.parse.urlencode(fields)
    fullUrl = baseUrl + data

    return fullUrl


  def dictTranslator(self):
      pass

  def getAllAds(self, searchItemDict):
      pass

