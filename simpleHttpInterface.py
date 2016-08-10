from http.server import HTTPServer, BaseHTTPRequestHandler

import simpleBay
import re

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def genDocHeader(self):
        self.responseContent = ("<html>\n" +
                                "<head>\n" +
                                "<title>Search Results</title>\n" +
                                "</head>\n" +
                                "<body>\n")

    def genDocBottom(self):
        self.responseContent += ("</body>\n" +
                                 "</html>")

    def genResponseContent(self):
        self.genDocHeader()
        self.responseContent += "<table border=\"1\">\n"
        for searchResult in self.searchResults:
            self.responseContent += "<tr>\n"
            self.responseContent += "<td><img src=\"" + str(searchResult['imgSrc']) + "\"></td>"
            self.responseContent += ("<td><a href=\"" + str(searchResult['url']) + "\" target=_blank>" +
                                     str(searchResult['title']) +
                                     "</a></td>\n")
            self.responseContent += "<td><strong>" + str(searchResult['price']) + "</strong></td>"
            self.responseContent += "</tr>\n"
        self.responseContent += "</table>\n"
        self.genDocBottom()
            
    def handleCommand(self):
        sb = simpleBay.SimpleBay(downloadPictures=False)
        searchItems = self.command.split(";")
        extractors = []
        keywords = []
        ammounts = []
        for searchItem in searchItems:
            expressions = searchItem.split(",")
            extractors.append(expressions[0])
            keywords.append(expressions[1])
            ammounts.append(int(expressions[2]))
        self.searchResults = sb.getSearchResults(extractors, keywords, ammounts)
        self.genResponseContent()

    def checkValidCommand(self):
        pattern = re.compile("(([0-9A-Za-z])+,([0-9A-Za-z])+,[0-9]+;)+(([0-9A-Za-z])+,([0-9A-Za-z])+,[0-9]+)")
        result = pattern.match(self.command)
        if result == None:
            return False
        else:
            return True

    def do_GET(self):
        self.command = self.requestline.split(" ")[1].split("/")[1]
        if not self.checkValidCommand():
            self.genDocHeader()
            self.responseContent = "<strong>Invalid input!</strong>"
            self.genDocBottom()
        else:
            self.handleCommand()
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(bytes(self.responseContent, "UTF-8"))

class SimpleHTTPInterface:
    def __init__(self):
        self.hostIP = "localhost"
        self.hostPort = 9000
        self.serverAdress = (self.hostIP, self.hostPort)
        self.server = HTTPServer(self.serverAdress, SimpleHTTPRequestHandler)

    def run(self):
        print("Http interface server started!")
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            pass

s = SimpleHTTPInterface()
s.run()
