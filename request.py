#print(response.content)   #to view the content in bytes
#print(response.text)   #to get in string utf encoding format; we can even specify the encoding by .encoding =''
#print(response.headers)

from bs4 import BeautifulSoup
import requests
import re
site_lists = ['https://arstechnica.com', 'https://www.engadget.com/', 'https://techcrunch.com', 'http://thenextweb.com/', 'https://www.wired.com/']
links_list = []
for i in site_lists:

    response = requests.get(i)
    #print(response)
    #print(response.status_code)
    if response:
        print('Success!!')
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
            links_list.append(link.get('href'))

        # print(links_list)

    else:
        print('Oops!! Some error occured!!')
print(len(links_list))



