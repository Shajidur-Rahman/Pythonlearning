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
#you can also check can i use it in python as a (a = 2) or not
#print(b)

#using islower
a = "hello world"
b = a.islower()
#Check if all the characters in the text are in lower case:
#print(b)

#using printable
a = "hello i am saa/*/d"
b = a.isprintable()
#print(b)

#using isspace
a = " "
b = a.isspace()
#print(b)

#using istitle
a = "Hello And Welcome To My World!"
b = a.istitle()
#Check if each word start with an upper case letter
#print(b)

#using issuper
a = "MY NAME IS SHAJIDUR "
#Check if all the characters in the text are in upper case:
#print(a.isupper())

# using join
a = ("shajidur","rahman")
b = '123'.join(a)
#Join all items in a tuple into a string, using a hash character as separator:
#print(b)

#using !just
a = 'banana'
b = a.ljust(20)
#print(a,"is loved by me")

#using lower
a = "MY NAME IS SHAJIDUR RAHMAN"
b = a.lower()
#The lower() method returns a string where all characters are lower case.
#print(b)

#using maketurens
txt = "Hello Sam!";
mytable = txt.maketrans("S", "P");
#Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:
#print(txt.translate(mytable));

#using pertition
a = "my name is fat sifat"
txxt = a.partition("is")
#print(txxt)

#using replace
a = "i love my sisters very much"
b = a.replace("sisters","mother")
#The replace() method replaces a specified phrase with another specified phrase.
#print(b)

#using refind
a = "i love my mother very much"
b = a.rfind("love")
#if you want to find an element use it you can also use reindxe
#print(b)
#print(a.rindex("love"))

#using split
a = "i love to code"
b = a.split("love")
#remove a item
#print(b)

#using swipcase
a = 'my name is shajHDFUidur rahman'
b = a.swapcase()
#print(b)

# go to the https://www.w3schools.com/python/ref_string_translate.asp to learn translation