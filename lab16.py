""" 
Trammel May, Gene Evans, Trent Duhart
"""

""" Make a website showing the top 10 rated movies on IMDB """ 

def makePage():
  response = getRaw("http://www.imdb.com/chart/top")
  print response

def getRaw(url):
  req = urllib2.Request(url)
  return urllib2.urlopen(req).read()


