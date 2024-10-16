


# Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
# name = “  JOHn  .“ to “john”
name= " JOHn ."
# lower
name=name.lower()
# replace
name=name.replace(".", "")
# strip
name=name.strip()
print(name)

# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”

sentence_one = "The Dog Breed is German Shepherd"
 # 'Breed is German'
print(sentence_one[8:23])

# sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])

# Split the below sentence using a semicolon i.e ; And display length of the result. 
# “The lazy dog; ran so fast; it hit the wall.” 
sentence3 = "The lazy dog; ran so fast; it hit the wall."
sentence3 = sentence3.split(";")
print(sentence3)

# first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name="  Joh.n" 
firstname= first_name.strip().replace(".", "")
last_name="   Do,e" 
lastname= last_name.strip().replace(",","")
fullname=firstname+" "+lastname
print(fullname)


# Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
clean_r = r.replace('["', "").replace('"]', "").replace('","', "")  # 'EWC'
print(clean_r)
