import urllib
url = 'https://inventory.data.gov/api/action/datastore_search?resource_id=102fd9bd-4737-401b-b88f-5c5b0fab94ec&limit=5&q=title:jones'
fileobj = urllib.urlopen(url)
print fileobj.read()
