import re
import urllib

url = "https://www.google.com/finance?q="
z=raw_input("Which company do you want to know the rates of the stock to???")
url_final = url + z

data = urllib.urlopen(url_final).read()
data1 = data.decode("utf-8")
m = re.search('meta itemprop="price"',data1)
start = m.start()
end = start +50
newString = data1[start:end]
n = re.search('content="',newString)
start1=n.end()
newString1 = newString[start1:]
p = re.search('" />',newString1)
start2 = p.start()
final= newString1[:start2]
print ("The stock of your requested company " + z),
print (":" + final)


