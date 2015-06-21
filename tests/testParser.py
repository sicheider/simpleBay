#! /usr/bin/env python3
# coding: utf-8
#######################
import unittest, sys
sys.path.insert(0, "..")
from simpleParser import Parser


class UrlGeneratorTests(unittest.TestCase):
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
                  'maxPrice': "100",
                  'minPrice': "30"}
    self.parseInstance = Parser()

  def testStandardFields(self):
    expectedTags = ("http://kleinanzeigen.ebay.de/anzeigen/s-suchanfrage.html",
                    "maxPrice=", "minPrice=", "locationStr=",
                    "keywords=TEST", "action=find", "pageNum=1",
                    "sortingField=SORTING_DATE")
    actualString = self.parseInstance.urlGenerator()
    print("Actual String:", actualString, "", sep='\n')

    for tag in expectedTags:
      print(tag, '==>', actualString.find(tag))
      self.assertTrue(actualString.find(tag) >= 0)

  def testSelfFields(self):
    expectedTags = ("http://kleinanzeigen.ebay.de/anzeigen/s-suchanfrage.html",
                    "maxPrice=100", "minPrice=30", "locationStr=Berlin",
                    "keywords=wasser+hahn", "action=find", "pageNum=1",
                    "sortingField=SORTING_DATE")
    actualString = self.parseInstance.urlGenerator(self.fields)
    print("Actual String:", actualString, "", sep='\n')

    for tag in expectedTags:
      print(tag, '==>', actualString.find(tag))
      self.assertTrue(actualString.find(tag) >= 0)


def main():
  unittest.main()

if __name__ == "__main__":
  main()
