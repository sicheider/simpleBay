import unittest
import parser


class ParserTests(unittest.TestCase):

  def setUp(self):
    """ Set up test fixture """
    self.fields = {'keywords': "wasser hahn",
                  'categoryId': "",
                  'locationStr': "Berlin",
                  'locationId': "",
                  'radius': "",
                  'sortingField': "SORTING_DATE",
                  'adType': "",
                  'posterType': "",
                  'pageNum': 1,
                  'action': "find",
                  'maxPrice': "",
                  'minPrice': ""}
    self.parseInstance = parser.Parser()

  def testUrlGenerator(self):
    expected_string = "http://kleinanzeigen.ebay.de/anzeigen/s-suchanfrage.html?keywords=wasser%20hahn&categoryId=&locationStr=Berlin&locationId=&radius=&sortingField=SORTING_DATE&adType=&posterType=&pageNum=1&action=find&maxPrice=&minPrice="
    self.assertTrue(self.parseInstance.urlGenerator(self.fields) == expected_string)


def main():
  unittest.main()

if __name__ == "__main__":
  main()
