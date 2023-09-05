s=input()
t=input()


def reversed(s):
    str=""
    for i in s:
        str=i+str
    return str

if reversed(s)==t:
    print("YES")
else:
    print("NO")
