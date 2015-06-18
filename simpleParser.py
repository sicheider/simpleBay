import urllib.request
import urllib.parse


class Parser():
  def __init__(self):
    self.standardFields = {'keywords': "keywords",
                            'categoryId': "categoryId",
                            'locationStr': "locationStr",
                            'locationId': "locationId",
                            'radius': "radius",
                            'sortingField': "sortingField",
                            'adType': "adType",
                            'posterType': "posterType",
                            'pageNum': "pageNum",
                            'action': "action",
                            'maxPrice': "maxPrice",
                            'minPrice': "minPrice"}

  def urlGenerator(self, fields=None, baseUrl=None):
    """Takes fields-dict and returns URL string."""
    if not baseUrl:
      baseUrl = "http://kleinanzeigen.ebay.de/anzeigen/s-suchanfrage.html?"
    if not fields:
      fields = self.standardFields

    data = urllib.parse.urlencode(fields)
    fullUrl = baseUrl + data

    return fullUrl
