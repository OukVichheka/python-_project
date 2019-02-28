import json

file_book = open('book.json','r')

book_data = json.load(file_book)
for content in book_data['Content']:
    for chapter in content:                           
        print(content)
        print(chapter)