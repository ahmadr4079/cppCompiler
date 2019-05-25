import pandas as pd
from uuid import uuid1


initialData = [[uuid1(),'keyword','float']]
dataFrameToken = pd.DataFrame(data=initialData,columns=['id','tokenName','attributeValue'])
dataFrameToken.to_csv('Token.csv')



