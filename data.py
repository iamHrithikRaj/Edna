import requests as res
from bs4 import BeautifulSoup

header = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
}

response = res.get("https://status.net/articles/performance-review-phrases-examples/", header)
htmlParser = BeautifulSoup(response.content, "html.parser")

p_tag_attrs = {'style': "padding-left: 60px;"}
h2_tag_attrs = {'class': ['chapter-subtitle']}

filename = "dataset.txt"
f_obj = open(filename, "w")

for line in htmlParser.find_all(["p", "h2"]):
    if line.attrs == h2_tag_attrs :
        f_obj.write("\n\n\n\n\n" + line.text+"\n")
    elif line.attrs == p_tag_attrs and "✓" not in line.text:
        # plain_text = (line.text).replace("✗ ", "    -")
        f_obj.write(line+"\n")
        
