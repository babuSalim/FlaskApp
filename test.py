import pandas as pd
Location = "File.xls"
df = pd.read_excel(Location)
sl=['51','52']
fn=['Salim','Esper']
ln=['Babu','nick']
gn=['Male','Female']
cn=['Bangladesh','India']
age=['23','22']
dt=['11/10/21','11/10/21']
id=['2222','3333']
EmpList=zip(sl,fn,ln,gn,cn,age,dt,id)
df=pd.DataFrame(data=EmpList,columns=['Sl','First Name','Last Name','Gender','Country','Age','Date','Id'])
writer=pd.ExcelWriter('File.xls',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1')
writer.save()
df = pd.read_excel(Location)
print(df.head())
