import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/page1.htm')
for line in fhand:
    print(line.decode().strip())