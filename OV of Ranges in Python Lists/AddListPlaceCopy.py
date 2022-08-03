tags = ['python', 'development', 'tutorials', 'code'] 

# Nope-
# tags[-1] = 'Programming'

# tags.extend('Programming') #spreads out each element so 'P' 'R' 'O' etc

# tags.extend(['Programming']) #Most common way to add a element to a list.

new_tags = tags + ['Programming'] #this way the OG list is still usable, so others can grab it and not the stuff you added.

print(new_tags)