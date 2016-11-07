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

    def genResponseContent(self):
        self.genDocHeader()
        self.responseContent += "<table>\n"
        self.responseContent += "<tr>\n"
        self.responseContent += "<th>Picture</th><th>Description</th><th>Date</th><th>Price</th>"
        self.responseContent += "<th>Average price</th><th>Listings</th><th>Sellthrough</th>\n"
        self.responseContent += "</tr>\n"
        for searchResult in self.searchResults:
            self.responseContent += "<tr>\n"
            self.responseContent += "<td><img src=\"" + str(searchResult['imgSrc']) + "\"></td>"
            self.responseContent += ("<td><a href=\"" + str(searchResult['url']) + "\" target=_blank>" +
                                     str(searchResult['title']) +
                                     "</a></td>\n")
            self.responseContent += "<td>" + searchResult['date'].strftime("%A, %d %B %H:%M") + "</td>"
            self.responseContent += "<td><strong>" + str(searchResult['price']) + "</strong></td>"
            self.responseContent += "<td>" + self.averagePrices[searchResult['keywordID'] - 1] + "</td>"
            self.responseContent += "<td>" + str(self.listingsCount[searchResult['keywordID'] - 1]) + "</td>"
            self.responseContent += "<td>" + self.sellThroughs[searchResult['keywordID'] - 1] + "</td>"
            self.responseContent += "</tr>\n"
        self.responseContent += "</table>\n"
        self.genDocBottom()

    def getListSearchTouplesFromFile(self):
        searchfile = get_data("simpleBaySuchbegriffe.ods")
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
            averagePrice = str(row[5])
            listingCount = int(row[7])
            sellThrough = str(row[8])
            listSearchTouples.append((keyword, ammount, keywordID))
            self.averagePrices.append(averagePrice)
            self.listingsCount.append(listingCount)
            self.sellThroughs.append(sellThrough)
        return listSearchTouples
                    
    def handleCommand(self):
        self.sb = simpleBay.SimpleBay(downloadPictures=False)
        try:
            listSearchTouples = self.getListSearchTouplesFromFile()
            self.searchResults = self.sb.getSearchResults(listSearchTouples)
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
