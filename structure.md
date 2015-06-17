## SimpleBay: eBay -Kleinanzeigen- parser

# UML structure Overview

### **Project** `[ (1) <--> (*, SearchItem) ]`
* methods:
  1. syncAds
  2. markAd
  3. deleteAd
  4. saveProject
  5. loadProject
* attributes:
  1. projectPlace
  2. projectName

### **Ad** `[ (*) <--> (1, Project) ]`
* methods:
  1. adDeleted
  2. adMarked
  3. adNew
* attributes:
  1. ID
  2. Name
  3. Link

### **SearchItem** `[ (*) <--> (1, Project) ]`
* methods:
  1. requestSearch
* attributes:
  1. itemName
  2. itemsPerRequest
  3. itemRange
  4. minPrice
  5. maxPrice
