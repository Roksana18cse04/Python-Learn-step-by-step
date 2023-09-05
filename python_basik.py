#one line statement
print("roksana")
 # two line statement in single line
l=20 ; b=30

print(l+b)

# muliple line in one staement-----(1)

addition = 10+20+\
        30+40+\
        50+60
print(addition)

# (1)  of opsit () in multiple line in one statement

add=(12+13+
     14+15+
     16+16)

print(add)


# Dictionaries  : # dictionary name as a key and mark as a value
# int: string

StudentId ={
    201 :"Rakibul Islam Likhon",
    202 :"Anik Das",
    203 : "Yesin Arafat",
    204 : "Roksana Akter"

}
print(StudentId)
print(StudentId[204])
print(StudentId.get(107))
print(StudentId.get(107,"Not A Valid key")) # Error catch defalt