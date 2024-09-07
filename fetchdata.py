import requests
from bs4 import BeautifulSoup


# def fetchdataandsave (url, path):
#     r = requests.get(url)
#     with open (path, "w", encoding='utf-8') as f:
#         f.write (r.text)


# url = "https://www.youtube.com/watch?v=4tAp9Lu0eDI"
# fetchdataandsave(url, "d:/Beautifulsoup/newdata.html")

with open ("newdata.html", "r", encoding='utf-8') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)"
# print(soup.title.parent.name)  #to print "head"
# print(soup.div)
# print(soup.p['class'])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find_all("div"))
# print(soup.find_all("div")[0])
# print(soup.find(id="link3"))
# for link in soup.find_all('a'):
#     print(link.get("href"))
# s = soup.find(id="link3")
# print(s.get("href"))
# for link in soup.find_all('a'):
#     print(link.get_text())
# print(soup.select("div.italic"))
# print(soup.select("span.italic"))
# print(soup.select("span#italic"))
# print(soup.find(class_="italic"))

# for child in soup.find(class_="container").children:
#     print(child)
# i = 0
# for parent in soup.find(class_="box").parents:
#     i +=1
#     print(parent)
#     if(i==2):
#         break
# cont = soup.find(class_="container")  #this is how we can modify an existing tag in html doc.
# cont.name = "span"
# print(cont)

# cont["class"] = "myclass class2"   #This is how e can chnage the name of class 

#How to insert new tags in the existing html

# ulTag = soup.new_tag("ul")   # make a ul tag
# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "About"
# ulTag.append(liTag)

# #This is how we can make a new modified html
# soup.html.insert(0, ulTag)
# with open ("modified.html", "w", encoding='utf-8') as f:
#     f.write(str(soup))

# Finding out if an attribute exists in the html file or not

# cont = soup.find(class_="container")
# print(cont.has_attr("contenteditable"))
# print(cont.has_attr("class"))

# def has_class_but_not_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")

# results = soup.find_all(has_class_but_not_id)
# print(results)


# def not_has_class_but_not_id(tag):
#     return not tag.has_attr("class") and not tag.has_attr("id")

# results = soup.find_all(not_has_class_but_not_id)
# print(results)

# def not_has_class_but_not_id(tag):
#     return not tag.has_attr("class") and not tag.has_attr("id")

# results = soup.find_all(not_has_class_but_not_id)
# for result in results:
#     print(result, "\n\n")