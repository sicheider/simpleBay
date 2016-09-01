#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler

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

    def genStartDoc(self):
        self.genDocHeader()
        self.responseContent += ("<strong>Supported websides:</strong>\n" +
                                 "<ul>\n")
        for extractorName in self.sb.extractorNames:
            self.responseContent += "<li>" + extractorName + "</li>\n"
        self.responseContent += "</ul>\n"
        self.responseContent += ("<strong>Append /[keyword1],[ammount1];" +
                                 "[keyword2],[ammount2];... to your url line!")
        self.genDocBottom()

    def genResponseContent(self):
        self.genDocHeader()
        self.responseContent += "<table>\n"
        self.responseContent += "<tr>\n"
        self.responseContent += "<th>Picture</th><th>Description</th><th>Date</th><th>Price</th>\n"
        for searchResult in self.searchResults:
            self.responseContent += "<tr>\n"
            self.responseContent += "<td><img src=\"" + str(searchResult['imgSrc']) + "\"></td>"
            self.responseContent += ("<td><a href=\"" + str(searchResult['url']) + "\" target=_blank>" +
                                     str(searchResult['title']) +
                                     "</a></td>\n")
            self.responseContent += "<td>" + searchResult['date'].strftime("%A, %d %B %H:%M") + "</td>"
            self.responseContent += "<td><strong>" + str(searchResult['price']) + "</strong></td>"
            self.responseContent += "</tr>\n"
        self.responseContent += "</table>\n"
        self.genDocBottom()
            
    def handleCommand(self):
        self.sb = simpleBay.SimpleBay(downloadPictures=False)
        searchItems = self.command.split(";")
        searchItems.pop()
        if len(searchItems) == 0:
            self.genStartDoc()
        else:
            listSearchTouples = []
            for searchItem in searchItems:
                expressions = searchItem.split(",")
                searchTouple = (expressions[0], int(expressions[1]))
                listSearchTouples.append(searchTouple)
            try:
                self.searchResults = self.sb.getSearchResults(listSearchTouples)
                self.genResponseContent()
            except simpleErrors.NoResultsError:
                self.genErrorContent("No search results!")

    def checkValidCommand(self):
        pattern = re.compile("^((([0-9A-Za-z-%])+,[0-9]+;)+)$|")
        result = pattern.match(self.command)
        if result == None:
            self.genErrorContent("Invalid input!")
            return False
        else:
            return True

    def do_GET(self):
        self.command = self.requestline.split(" ")[1].split("/")[1]
        if self.checkValidCommand():
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
        print("Open http://" + self.hostIP + ":" + str(self.hostPort) +
                "/[webside],[keyword],[ammount];... in your browser")
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            pass

s = SimpleHTTPInterface()
s.run()
