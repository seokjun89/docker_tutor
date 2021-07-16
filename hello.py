import pandas as pd

df = pd.read_csv("./sample.csv", encoding='euc-kr')

print(df['센터명'].value_counts())

# TODO 광역시별 센터 분포 

#city = []
#for data in df['주소']:
#    city.append(data.split(' ')[0])

#print(list(set(city)))

print(df['센터명'].apply(lambda x: x.split(' ')[1]).value_counts())
