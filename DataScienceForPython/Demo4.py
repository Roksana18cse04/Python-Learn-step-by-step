#code by youtube vedo

#Create a Pandas DataFrame
import pandas as pd

#DataSet
data ={
    'student':["Amit","Sumi","Rohani","Roksana","Rabita"],
    'ID':["18CSE101","18CSE102","18CSE103","18CSE104","18CSE105"],
    'Marks':[95,67,98,78,79]
}
df=pd.DataFrame(data)
print("Student Record\n\n",df)