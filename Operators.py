#list sector
frout_name = ['banana','mango','sifat']
#print(frout_name)


#len list
person_name = ['sifat','saad','jannat']
#print(len(person_name))

#type list
person = ['saad','sifat']
#print(type(person))

#using -1
a = ['saad','sifat','apu']
#use -1 to get last item
#print(a[-1])

#changing the value
a = ["sifat",'saad']
a[0] = 'smrity'
#print(a)

#insert or adding
a = ['saad','sifat']
a.insert(1,'smrity')
#print(a)

#add 2 list
a = ['sifat','sifat']
b = ['smrity','hi']
a.extend(b)
#print(a)

# removing . (you can use remove key or pop key or del key)
a = ['saad','sifat']
#del a[0]
#print(a)

#name = ['sifat','saad','smrity']
#for i in name:
    #print(i)
#short cut
#name = ['sifat','saad']
#[print(i) for i in name]



#using while loop in for loop
name_person = ['saad', 'sifat', 'smrity', 'asjd']
i = 0
while i < len(name_person):
    print(name_person[i]) #i am getting an error
    i = i + 1

#end of the day
