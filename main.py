#using catitalize
a = "my name is saad. i read in class 6"
b = a.capitalize()
# the capitalize funtion capital the first letter of the sentence
#print(b)

#using casefold
name = "My name is shajidur Rhaman"
c = name.casefold()
#the case fold letter retures all the letter lower case
#print(c)

#using center align
center = "shajidur rahman "
aligncenter = center.center(50)
#The center() method will center align the string, using a specified character (space is default) as the fill character.
#print(aligncenter)

#using count method
txt = "i love coding but coding is not my job . coding is my hobby"
counting = txt.count("coding")
print(counting)