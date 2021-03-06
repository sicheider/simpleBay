#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from pyexcel_ods3 import get_data

import simpleBay
import simpleErrors

import re

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def genDocHeader(self):
        self.responseContent = ("<html>\n" +
                                "<head>\n" +
                                "<title>Search Results</title>\n" +
                                "<style>\n" +
                                "table {border-collapse: collapse; width: 100%;}\n" +
                                "th, td {text-align: left; padding: 8px;}\n" +
                                "tr:nth-child(even){background-color: #f2f2f2}\n" +
                                "th {background-color: #4CAF50; color: white;}\n" +
                                "</style>\n" +
                                "</head>\n" +
                                "<body>\n")

    def genDocBottom(self):
        self.responseContent += ("</body>\n" +
                                 "</html>")

    def genErrorContent(self, errorMessage):
        self.genDocHeader()
        self.responseContent += "<strong>" + errorMessage + "</strong>"
        self.genDocBottom()

    def addAverageInfoToSearchResults(self):
        for searchResult in self.searchResults:
            searchResult['averagePrice'] = self.averagePrices[searchResult['keywordID'] - 1]
            searchResult['listingCount'] = self.listingsCount[searchResult['keywordID'] - 1]
            searchResult['sellThrough'] = self.sellThroughs[searchResult['keywordID'] - 1]

    def addProfitToSearchResults(self):
        for searchResult in self.searchResults:
            searchResult['profit'] = searchResult['averagePrice'] - searchResult['price']

    def genResponseContent(self):
        self.genDocHeader()
        self.responseContent += "<table>\n"
        self.responseContent += "<tr>\n"
        self.responseContent += "<th>Picture</th><th>Description</th><th>Price</th><th>Average price</th>"
        self.responseContent += "<th>Original keyword</th><th>Profit</th><th>Listings</th><th>Sellthrough</th><th>Date</th>\n"
        self.responseContent += "</tr>\n"
        for searchResult in self.searchResults:
            self.responseContent += "<tr>\n"
            self.responseContent += "<td><img src=\"" + str(searchResult['imgSrc']) + "\"></td>"
            self.responseContent += ("<td><a href=\"" + str(searchResult['url']) + "\" target=_blank>" +
                                     str(searchResult['title']) +
                                     "</a></td>\n")
            self.responseContent += "<td>" + str(searchResult['price']) + "€" + "</td>"
            self.responseContent += "<td>" + str(searchResult['averagePrice']) + "€" + "</td>"
            self.responseContent += "<td>" + searchResult['keyword'].replace("%20", " ") + "</td>"
            if searchResult['profit'] >= 0:
                self.responseContent += "<td><strong><font color=\"green\">" + "%.2f" % searchResult['profit'] + "€" + "</font></strong></td>"
            else:
                self.responseContent += "<td><strong><font color=\"red\">" + "%.2f" % searchResult['profit'] + "€" + "</font></strong></td>"
            self.responseContent += "<td>" + searchResult['listingCount'] + "</td>"
            self.responseContent += "<td>" + searchResult['sellThrough'] + "</td>"
            self.responseContent += "<td>" + searchResult['date'].strftime("%d.%m.%y %H:%M") + "</td>"
            self.responseContent += "</tr>\n"
        self.responseContent += "</table>\n"
        self.genDocBottom()

    def getListNonKeywords(self, searchFileName):
        searchFile = get_data(searchFileName)
        sheet2 = searchFile["Sheet2"]
        sheet2.pop(0)
        result = []
        for row in sheet2:
            result.append(row[0])
        return result

    def getListSearchTouplesFromFile(self, searchFileName):
        searchfile = get_data(searchFileName)
        sheet1 = searchfile["Sheet1"]
        listSearchTouples = []
        sheet1.pop(0)
        self.averagePrices = []
        self.listingsCount = []
        self.sellThroughs = []
        for row in sheet1:
            keywordID = int(row[0])
            company = str(row[1])
            company.replace(" ", "%20")
            model = str(row[2])
            model.replace(" ", "%20")
            keyword = company + "%20" + model
            ammount = int(row[3])
            averagePrice = float(row[6].replace("€", ""))
            listingCount = str(row[8])
            sellThrough = str(row[9])
            listSearchTouples.append((keyword, ammount, keywordID))
            self.averagePrices.append(averagePrice)
            self.listingsCount.append(listingCount)
            self.sellThroughs.append(sellThrough)
        return listSearchTouples
                    
    def handleCommand(self):
        try:
            listSearchTouples = self.getListSearchTouplesFromFile("Suchbegriffe.ods")
            listNonKeywords = self.getListNonKeywords("Suchbegriffe.ods")
            self.sb = simpleBay.SimpleBay(listNonKeywords, downloadPictures=False)
            self.searchResults = self.sb.getSearchResults(listSearchTouples)
            self.addAverageInfoToSearchResults()
            self.addProfitToSearchResults()
            self.genResponseContent()
        except simpleErrors.NoResultsError:
            self.genErrorContent("No search results!")
        except IndexError:
            self.genErrorContent("Invalid input file!")

    def do_GET(self):
        if not "favicon" in self.requestline:
            self.handleCommand()
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(bytes(self.responseContent, "UTF-8"))

class SimpleHTTPInterface:
    def __init__(self, hostIP="localhost", hostPort=9000):
        self.hostIP = hostIP
        self.hostPort = hostPort
        self.serverAdress = (self.hostIP, self.hostPort)
        self.server = HTTPServer(self.serverAdress, SimpleHTTPRequestHandler)

    def run(self):
        print("Http interface server started!")
        print("Open http://" + self.hostIP + ":" + str(self.hostPort) + " in your browser")
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            pass

s = SimpleHTTPInterface()
s.run()
