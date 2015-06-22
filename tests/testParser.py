#! /usr/bin/env python3
# coding: utf-8
#######################
import unittest, sys
sys.path.extend([".", ".."])
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
    self.counter = 0

  def testDictToUrlConversion(self):
    verbose = True

    baseUrl = "http://kleinanzeigen.ebay.de/anzeigen/s-suchanfrage.html"
    tagListOne = ("maxPrice=", "minPrice=", "locationStr=", "keywords=TEST",
                  "action=find", "pageNum=1","sortingField=SORTING_DATE")
    tagListTwo = ("maxPrice=100", "minPrice=30", "action=find", "pageNum=1",
                  "keywords=wasser+hahn", "locationStr=Berlin",
                  "sortingField=SORTING_DATE")

    for (actualString, tagList) in (
        (self.parseInstance.urlGenerator(), tagListOne),
        (self.parseInstance.urlGenerator(self.fields), tagListTwo)):

      self.assertTrue(baseUrl in actualString)
      if verbose:
        print('\n', "Actual String:", '\n', actualString, '\n', sep='')

      for tag in tagList:
        self.counter += 1
        self.assertTrue(tag in actualString)
        if verbose:
          print("Counter: ", self.counter, '\t', "==>", tag)


def main():
  unittest.main()

if __name__ == "__main__":
  main()
