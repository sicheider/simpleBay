#! /usr/bin/env python3
# coding: utf-8        #########################################################
#                            ebYp - an eBay Parser                            #
#                                   gsec < 2k1x >
#
#     This is free software,
#     do whatever you want.
#     Except evil stuff!
#-------------------------------------------------------------------------------
# from the tutorial:
# http://blog.miguelgrinberg.com/post/easy-web-scraping-with-python
################################################################################
import requests
import argparse
from bs4 import BeautifulSoup


def get_search_url(search_term):
  root_url = "http://kleinanzeigen.ebay.de"
  return root_url + "/anzeigen/s-" + search_term + "/k0"


def get_ad_page_urls(index_url, selector=None):
  if not selector:
    selector = "section.ad-listitem-main a[href^=]"

  response = requests.get(index_url)
  soup = BeautifulSoup(response.content)
  return [entry.attrs.get("href") for entry in soup.select(selector)]


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("search", type=str)
  args = parser.parse_args()
  index_url = get_search_url(args.search)

  for url in get_ad_page_urls(index_url):
    print(url)

  print("\n", "/~"*50 + "/", "\n")

  for field in advanced_search():
    print(field)


#----------------------------
#- XXX under construction XXX
#----------------------------
def advanced_search():
  # implcitly joined string
  search_string = ("http://kleinanzeigen.ebay.de/anzeigen/s-suchanfrage.html"
                   "?keywords={keywords}&categoryId={categoryId}&locationStr=&"
                   "locationId=0&radius=0&sortingField=SORTING_DATE&adType=&"
                   "posterType=&pageNum=1&action=find&maxPrice=&minPrice=")
  return search_string.split('?')[-1].split('&')


class Project():
  def __init__(self, name):
    self.name = name


#--------------------------------   BOILERPLATE   ------------------------------
if __name__ == '__main__':
  main()
  #advanced_search()
