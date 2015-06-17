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
  """Create instances of distinct search projects."""
  def __init__(self, name, place):
    self.name = name
    self.place = place

  def syncAds(self):
    """Synchronize ads of current project.

    Add new ads in empty project or updates already saved ads.
    """
    pass

  def markAd(self):
    """Mark an ad based on its ID."""
    pass

  def deletedAd(self, id):
    """Remove ad from currrent project."""
    pass

  def saveProject(self):
    """Saves the project to disk."""
    # TODO: -add save-to location
    #       -request project name (e.g. from self.name)
    #       -append timestamp to distinguish same-named projects
    pass

  def loadProject(self):
    """Retrieve Project from disk."""
    pass


class Ad():
  """Contains infromations about specific ads."""
  def __init__(self, name, id, link):
    self.name = name
    self.id = id
    self.link = link

  def adDeleted(self):
    """Mark ad for removal."""
    #TODO: pass boolean and remove ad in exit-method if True.
    pass

  def adMarked(self):
    """Set marked flag."""
    pass

  def adNew(self):
    """Set new flag."""
    pass


class SearchItem():
  """Do the actual search on the Website and parse results."""
  def __init__(self, name, distance, number=None, minPrice=None, maxPrice=None):
    self.name = name
    self.distance = distance
    self.number_of_requests = number
    self.minPrice = minPrice
    self.maxPrice = maxPrice

  def requestSearch(self):
    """Request results from the search field."""
    # TODO: implement with get_ad_page_urls()
    pass


#--------------------------------   BOILERPLATE   ------------------------------
if __name__ == '__main__':
  main()
  #advanced_search()
