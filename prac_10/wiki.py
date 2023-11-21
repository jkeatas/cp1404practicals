import wikipedia


page_title = input("Page title: ")
while page_title != "":
    page = wikipedia.page(page_title)
    print(page.url, page.title, page.summary)
    page_title = input("Page title: ")
