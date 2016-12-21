import urllib, json

url = "http://cab.inta-csic.es/rems/wp-content/plugins/marsweather-widget/api.php"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data