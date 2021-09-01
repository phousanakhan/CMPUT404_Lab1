import requests

url = "https://raw.githubusercontent.com/phousanakhan/CMPUT404_Lab1/main/requestScript.py"
res = requests.get(url)
print(res.text)
