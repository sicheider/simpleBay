class Parser():
  def __init__(self):
    pass

  def urlGenerator(self, fields):
    """Takes fields-dict and returns URL string."""
    search_string = ("http://kleinanzeigen.ebay.de/anzeigen/s-suchanfrage.html?"
                    "keywords={keywords}&"
                    "categoryId={categoryId}&"
                    "locationStr={locationStr}&"
                    "locationId={locationId}&"
                    "radius={radius}&"
                    "sortingField={sortingField}&"
                    "adType={adType}&"
                    "posterType={posterType}&"
                    "pageNum={pageNum}&"
                    "action={action}&"
                    "maxPrice={maxPrice}&"
                    "minPrice={minPrice}").format(**fields)
    return search_string


