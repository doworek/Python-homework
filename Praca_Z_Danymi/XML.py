#SAX
print ('\n SAX \n')
import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "movie":
         print ("----------------------------------------")
         title = attributes["title"]
         print ('Title:', title)

   def endElement(self, tag):
      if self.CurrentData == 'type':
         print ('Type:', self.type)
      elif self.CurrentData == 'format':
         print ('Format:', self.format)
      elif self.CurrentData == 'year':
         print ('Year:', self.year)
      elif self.CurrentData == 'rating':
         print ('Rating:', self.rating)
      elif self.CurrentData == 'stars':
         print ('Stars:', self.stars)
      elif self.CurrentData == 'description':
         print ('Description:', self.description)
      self.CurrentData = ""

   def characters(self, content):
      if self.CurrentData == 'type':
         self.type = content
      elif self.CurrentData == 'format':
         self.format = content
      elif self.CurrentData == 'year':
         self.year = content
      elif self.CurrentData == 'rating':
         self.rating = content
      elif self.CurrentData == 'stars':
         self.stars = content
      elif self.CurrentData == 'description':
         self.description = content
  
if ( __name__ == "__main__"):
   
   parser = xml.sax.make_parser()
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   parser.parse("movies.xml")

# DOM
print ('\n DOM \n')
from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print ("Catalog: %s" % collection.getAttribute("shelf"))

movies = collection.getElementsByTagName("movie")

for movie in movies:
   print ("----------------------------------------")
   if movie.hasAttribute("title"):
      print ('Title: %s' % movie.getAttribute("title"))

   type = movie.getElementsByTagName('type')[0]
   print ('Type: %s' % type.childNodes[0].data)

   format = movie.getElementsByTagName('format')[0]
   print ('Format: %s' % format.childNodes[0].data)

   year = movie.getElementsByTagName('year')[0]
   print ('Year: %s' % year.childNodes[0].data)

   rating = movie.getElementsByTagName('rating')[0]
   print ('Rating: %s' % rating.childNodes[0].data)

   stars = movie.getElementsByTagName('stars')[0]
   stars.childNodes[0].nodeValue = '10' #modyfikacja
   print ('Stars: %s' % stars.childNodes[0].data)

   description = movie.getElementsByTagName('description')[0]
   print ('Description: %s' % description.childNodes[0].data)

tmp_config = 'C:\\Users\\User\\Documents\\STUDIA\\IV rok\\Python\\movies_modyfikowane.xml'
f = open(tmp_config, 'w')
DOMTree.writexml( f )
f.close()