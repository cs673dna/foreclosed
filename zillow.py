from string import Template
import urllib2
import urllib

ZWSID = 'X1-ZWz1byi0snpg5n_7x5fi'
ZID = 'cs673dna'

GetSearchResultsTemplate = Template('http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=$ZWSID&address=$address&citystatezip=$citystatezip')

def zEstimate(address):
	uri=GetSearchResultsTemplate.substitute(ZWSID=ZWSID, address=urllib.quote(address.address), citystatezip=urllib.quote(address.citystatezip))
	print uri
	f = urllib2.urlopen(uri)
	return f
