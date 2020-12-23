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
#print(counting)

#using ecode
ecoding = "my name is saad"
a = ecoding.encode()
#print(a)

#using endswith
a = "shajidur rahman."
b = a.endswith(".")
#if you use it you can check if what is the last element have (true or false)
#print(b)

#go to the "https://www.w3schools.com/python/ref_string_expandtabs.asp" link to know expendsteg

#using find it is same to index
a = "welcome to my website"
b = a.find("welcome")
#if you have the velue it will show you the index number
#print(b)
#if you dont have it will show you -1

#check all isalnum
a = "mynameissaad"
b = a.isalnum()
#the result will be true
#print(b)

a = "my name is saad"
b = a.isalnum()
#the result will be false
#because there is some space
#print(b)

# using isalpha
a = "shajidur"
b = a.isalpha()
#Check if all the characters in the text is alphabetic
#print(b)

#using identifier
a = "shajidurrahman"
b = a.isidentifier()
#Check if the string is a valid identifier:
#print(b)

#using islower
a = "hello world"
b = a.islower()
#Check if all the characters in the text are in lower case:
print(b)