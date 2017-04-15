""" 
Lab16
@Author Trammel May, Gene Evans, Trent Duhart
"""

""" Make a website showing the top 10 rated movies on IMDB """ 

def makePage():
  setWorkingDir()
  writeToFile(extractTopTen(getRaw("http://www.imdb.com/chart/top")))
  
def getRaw(url):
  import urllib2
  req = urllib2.Request(url)
  return urllib2.urlopen(req).read()

def makeHTML(topten):
  html = """<!DOCTYPE html>
  <html>
  <body>
  <ol>"""
  for movie in topten:
    html += """<li>""" + movie + """</li>"""
  html += """</ol>
  </body>
  </html>"""
  return html

def writeToFile(topten):
  file = open(getMediaPath() + "/top_ten.html", 'w+')
  file.write(makeHTML(topten))
  file.close()
  
def setWorkingDir():
  showInformation("Please select the working directory of the project")
  setMediaPath()
  
def extractTopTen(data):
  import re
  matcher = "<td class=\"titleColumn\">\n.*\n.*\ntitle=.+\" >(.*)<"
  return re.findall(matcher, data)[0:10]
  

  

