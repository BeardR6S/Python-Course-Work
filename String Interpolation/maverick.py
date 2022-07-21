#Very Basic Form of String Interpolation/ Anything in {} will be parsed and treated like a python script./ 
#To have a print function that displays the {} you need to put double brackets. {{}}
#need to put f so python looks for python code

name = 'Kristine'
product = 'Python Elearning course'

email_content = f"""
Hi {name}

Thank you for purchasing the {product}

Regards,

Sales Team 
"""

print(email_content)




