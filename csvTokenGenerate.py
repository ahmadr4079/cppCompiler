import pandas as pd
from uuid import uuid1
import subprocess
import os


def generateTokenCsvFile():
    process = subprocess.Popen("ls", stdout=subprocess.PIPE, shell=True)
    (output,err) = process.communicate()
    if 'token.csv' in output.decode('utf-8'):
        os.remove('token.csv')
        initialData = []
        keywordFile = open('cppKeyword.txt','r')
        for item in keywordFile:
            initialData.append([uuid1(),'keyword',item.split('\n')[0],None])
        keywordFile.close()

        dataFrameToken = pd.DataFrame(data=initialData,columns=['id','tokenName','attributeValue','line'])
        dataFrameToken.to_csv('token.csv')

        return True
    else:
        initialData = []
        keywordFile = open('cppKeyword.txt','r')
        for item in keywordFile:
            initialData.append([uuid1(),'keyword',item.split('\n')[0],None])
        keywordFile.close()

        dataFrameToken = pd.DataFrame(data=initialData,columns=['id','tokenName','attributeValue','line'])
        dataFrameToken.to_csv('token.csv')

        return True
