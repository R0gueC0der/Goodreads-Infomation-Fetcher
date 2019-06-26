import requests
import xmltodict
import json

key = "IJLQ6N252s1ZSnOCzU5hQ"

# Sample Id: 32590

def get_author_books(authorId, noOfBooks):
    url = "https://www.goodreads.com/author/list/{}?format=xml&key={}".format(authorId, key)
    r = requests.get(url)
    
    xml_file = r.content
    json_file = json.dumps(xmltodict.parse(xml_file))

    data = json.loads(json_file)
    #print("Author Name: " + str(data[0]["GoodreadsResponse"]["author"]["books"]["book"]["title"]))

    books = data["GoodreadsResponse"]["author"]["books"]["book"]

    print("Author Name: " + data["GoodreadsResponse"]["author"]["name"])
    print("\nBook List")
    print("----------------------")
    for x in range(noOfBooks):
        print(str(x + 1) + ". " + books[x]["title"])

id = input("Enter Author ID: ")
bookNo = int(input("Enter No Of Books: "))

get_author_books(id, bookNo)