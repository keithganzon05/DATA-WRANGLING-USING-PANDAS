import pandas as pd
data1 = {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],'Dimension':['Length','Width','Height','Length','Width','Height'],'Value':[6,4,2,5,3,4]}
messy = pd.DataFrame(data1,columns=['Box','Dimension','Value'])
tidy = messy.pivot_table(index='Box',columns='Dimension',values='Value').reset_index()
volume1 = tidy.iloc[0,1]*tidy.iloc[0,2]*tidy.iloc[0,3]
volume2 = tidy.iloc[1,1]*tidy.iloc[1,2]*tidy.iloc[1,3]
add = pd.Series([volume1,volume2],index=[0,1])
merge = pd.concat([tidy,add],axis=1)
final1 = merge.rename(columns={0:'Volume'})
swap = list(final1)
swap[1],swap[2] = swap[2],swap[1]
swap[2],swap[3] = swap[3],swap[2]
final1 = final1.reindex(columns = swap)