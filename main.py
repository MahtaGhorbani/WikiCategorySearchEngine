import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from WikiFinder import WikiFinder

if __name__ == '__main__':
    wiki = WikiFinder()
    while True:
        query = input("Enter your query: ")
        if query.lower() == "exit":
            print("Thank You for using WikiFinder !!!")
            break
        pages = wiki.search(query)
        if pages:
            for page in pages:
                print(page[0])
                print()
        else:
            print("No results found\n")
        print("*" * 50)
