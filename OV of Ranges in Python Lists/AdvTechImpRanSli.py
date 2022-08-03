#depending on what Developers you work with you might hear ranges and slices used interchangably.

tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming',
    'computer science'
]

#tag_range = tags[:-1:2] #tags[:-1:2] = before the : means first item, -1 means before last itema and 2 means go 1,3,5,7,9 / 0,2,4,6,8, etc.

tag_range = tags[::-1] #flips the entire order of the list.

print(tag_range)