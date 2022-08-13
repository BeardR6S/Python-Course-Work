from types import new_class


legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

# raw_db = [legacy_customers, new_customers]

# print(raw_db)

#What you get =  [['Alice', 'Bob'], ['Tiffany', 'Kristine']]

#what we want = ['Alice', 'Bob', 'Tiffany', 'Kristine'] 

for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer)

print(new_customers)