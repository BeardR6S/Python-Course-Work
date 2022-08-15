"""
remove_first_and_last(list_to_clean)

html = ['<h1>', 'Some Content', '</h1>']

remove_first_and_last(html)
=> 'some content'

html_2 = ['<h1>', 'Some Content', 'more', '</h1>']

remove_first_and_last(html)
=> ['some content', 'more']
"""

# def remove_first_and_last(list_to_clean):
#     _, *content, _ = list_to_clean
#     return content

# html = ['<h1>', 'Some content', '</h1>']

# print(remove_first_and_last(html))


def remove_first_and_last(list_to_clean):
    _, *content, _ = list_to_clean
    return content

html = ['<h1>', 'Some content', 'more', '</h1>']

print(remove_first_and_last(html))

