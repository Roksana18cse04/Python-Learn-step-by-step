# vowel 

ch='B'

if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
    print("Vowel")
else:
    print("Consonant")

    ### Loop stateme 
    ###for loop , while loop

    # while loop 
i=1
while i<=20:
    if i==12:
        break ## Break stament work if condition is true the print 1 to 11
    print(i)
    i=i+1
print ("Loop End")

'''
i=1
while i<=20:
    if i==12:
        continue ## Break stament work if condition is true the print 1 to 11
    print(i)
    i=i+1
print ("Loop End")
### for loop
'''
# list 

subjects = ["C","c++","java","python","Android","OS","TOC"]

print(subjects)
print(subjects[0])
print(subjects[2:])
print(subjects[-1])
print("html" in subjects)
print("React" not in subjects)
print(subjects + ["HTML","React"])
print(subjects + [27])
print(subjects)
print(subjects[-1])


print("affter append list item")
subjects.append("HTML")
print(len(subjects))
print("after insert list item")
subjects.insert(2,"SQL")
print(subjects)
print(len(subjects))
subjects.remove("HTML")
print(subjects)