# HTML parser used to seperate different tags, item, text and attributes. there is a lbrary called HTML parser used to do this.

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for item in attrs:
            print "->", item[0], ">", item[1]
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for item in attrs:
            print "->", item[0], ">", item[1]
	def handle_comment(self, data):
        if "\n" in data:
            print ">>> Multi-line Comment \n", data
        else:
            print ">>> Single-line Comment \n", data
    
    def handle_data(self, data):
        if not "\n" in data:
            print ">>> Data \n", data


html = ""       
for i in range(int(raw_input())):
    html += raw_input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
#parser = MyHTMLParser()
#for item in range(int(raw_input())):
 #   parser.feed(raw_input())