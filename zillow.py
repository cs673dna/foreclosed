from string import Template
import urllib2
import urllib
from xml.dom.minidom import parse

ZWSID = 'X1-ZWz1byi0snpg5n_7x5fi'
ZID = 'cs673dna'

GetSearchResultsTemplate = Template('http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=$ZWSID&address=$address&citystatezip=$citystatezip')

def zEstimate(address):
	uri=GetSearchResultsTemplate.substitute(ZWSID=ZWSID, address=urllib.quote(address.address), citystatezip=urllib.quote(address.citystatezip))
	f = urllib2.urlopen(uri)
	return parseSearchResults(f)


def parseSearchResults(results):
	resultsXML = parse(results)	
	try:
		responseXML = resultsXML.firstChild.getElementsByTagName('response')[0]
	except IndexError as e:
		raise ZillowError(resultsXML.getElementsByTagName("message")[0].getElementsByTagName("text")[0].firstChild.toxml())
	zestimateXML = responseXML.getElementsByTagName('zestimate')[0]
	amountXML = zestimateXML.getElementsByTagName('amount')[0]
	return amountXML.firstChild.toxml()


class ZillowError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
