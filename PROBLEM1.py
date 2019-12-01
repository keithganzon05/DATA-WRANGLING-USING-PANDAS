import pandas as pd
data1 = {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
data2 = {'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
data3 = {'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
data4 = {'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}

bear1 = pd.DataFrame(data1,columns=['Student','Math'])
bear2 = pd.DataFrame(data2,columns=['Student','Electronics'])
bear3 = pd.DataFrame(data3,columns=['Student','GEAS'])
bear4 = pd.DataFrame(data4,columns=['Student','ESAT'])

mer1 = pd.merge(bear1,bear2,how='inner',on='Student')
mer2 = pd.merge(mer1,bear3,how='inner',on='Student')
mer3 = pd.merge(mer2,bear4,how='inner',on='Student')