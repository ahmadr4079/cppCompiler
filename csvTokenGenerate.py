import pandas as pd
from uuid import uuid1


initialData = []
keywordFile = open('cPlusKeyword.txt','r')
for item in keywordFile:
    initialData.append([uuid1(),'keyword',item])
keywordFile.close()

dataFrameToken = pd.DataFrame(data=initialData,columns=['id','tokenName','attributeValue'])
dataFrameToken.to_csv('token.csv')



