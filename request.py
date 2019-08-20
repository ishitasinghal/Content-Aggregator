import requests
response = requests.get('https://www.technewsworld.com')
#print(response.status_code)
# if response:
#     print('Success!!')
# else:
#     print('Oops!! Some error occured!!')

#print(response.content)   #to view the content in bytes

#print(response.text)   #to get in string utf encoding format; we can even specify the encoding by .encoding =''

print(response.headers)