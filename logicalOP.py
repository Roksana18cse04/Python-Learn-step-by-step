
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
subjects.sort()
print(subjects)
subjects.reverse()

number=[10,40,39,48,12,45,30]
print(number)
number.reverse()
print("reverse number :",number)  # reverse : 30,45,12,48,39,40,10
number.sort()
print("Sorting Number" ,number)  #Sort : 10,12,30,39,40,45,48
print(len(number))
number.pop()
print("After pop number : ",number)  # last number is pop
print(len(number))

pos=number.index(40)
print(pos)
number.append(40)
print(number) ## last position is added the new number

print("doubleTime",number.count(40))

num=list(range(10))   # 0-9 to range function & convert to list 
print("num",num)
num2 =list(range(5,20))
print("num2",num2) # 5-19 range

num3=list(range(2,101,2)) # difference 3rd parameter last range 2nd parameter and 1st paramete is staring point
print("num3",num3)

###  For loop in python

# list item for separete in For loop working in abobe


## add number in list num

index=0
n=len(num)
while index<n:
    print(num[index])
    index=index+1


### For loop

for x in num2:
    print(x)