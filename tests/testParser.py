#! /usr/bin/env python3
# coding: utf-8
#######################
import unittest, sys
sys.path.insert(0, "..")
from simpleParser import Parser


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
    self.parseInstance = Parser()

  def testUrlGenerator(self):
    expected_string = ("http://kleinanzeigen.ebay.de/anzeigen/"
    "s-suchanfrage.html?keywords=wasser+hahn&categoryId=&locationStr=Berlin&"
                       "locationId=&radius=&sortingField=SORTING_DATE&adType=&"
                       "posterType=&pageNum=1&action=find&maxPrice=&minPrice=")
    actual_string = self.parseInstance.urlGenerator(self.fields)
    #print("EXP: ", expected_string)
    print("ACT: ", actual_string)
    #self.assertTrue(actual_string == expected_string)


def main():
  unittest.main()

if __name__ == "__main__":
  main()
