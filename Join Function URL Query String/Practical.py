# https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q=' 
tags = ['python', 'development', 'tutorial']  
formatted_tags = '-'.join(tags) 
query_uir = f'{uri}{formatted_tags}'

print(formatted_tags) #just the tags, no https://google.com...

print(query_uir) #Shows the full search link from google.

