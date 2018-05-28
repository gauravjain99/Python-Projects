import json
import whois

url = input("Enter a url : ")
data = str(whois.whois(url))
info = json.loads(data)

print("Organisation : ", info['org'])
print("Emails : ", info['emails'])