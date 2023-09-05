n=int(input())
k=int(input())
oddNumber =[]
evenNumber =[]
start,end =1,n

for x in range(start,end+1):
    if x%2!=0:
       # print(x,end =" ")
        oddNumber.append(x)

for x in range(start,end+1):      
    if x%2==0:
       # print(x,end=" ")
        evenNumber.append(x)

result=oddNumber+evenNumber
#print(result)
index=k-1  
if 0 <= index <len(result):
    value = result[index]
    print(value)