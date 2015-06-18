import urllib.request
import urllib.parse


class Parser():
  def __init__(self):
    self.standard_fields = {'keywords': "keywords",
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

  def urlGenerator(self, fields=None, base_url=None):
    """Takes fields-dict and returns URL string."""
    if not base_url:
      base_url = "http://kleinanzeigen.ebay.de/anzeigen/s-suchanfrage.html?"
    if not fields:
      fields = self.standard_fields

    data = urllib.parse.urlencode(fields)
    full_url = base_url + data

    return full_url
