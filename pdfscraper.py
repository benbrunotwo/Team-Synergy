# 1. Add some necessary libraries
from bs4 import BeautifulSoup
import scraperwiki
from urllib.request import urlopen


# 2. The URL/web address where we can find the PDF we want to scrape
url = 'https://www.jstage.jst.go.jp/article/jcbn/40/3/40_3_163/_pdf'


# 3. Grab the file and convert it to an XML document we can work with
f = urlopen(url)
pdfdata = f.read()
xmldata = scraperwiki.pdftoxml(pdfdata)
soup = BeautifulSoup(xmldata, "lxml-xml")
print(soup.prettify())

#root = lxml.etree.fromstring(xmldata)

# 4. Have a peek at the XML (click the "more" link in the Console to preview it).
#print(lxml.etree.tostring(root, pretty_print=True))

# 5. How many pages in the PDF document?
#pages = list(root)
#print("There are", len(pages), "pages")



