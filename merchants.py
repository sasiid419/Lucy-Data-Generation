from faker import Faker
import random
import pandas as pd
ourFake = Faker()
Faker.seed(111)
random.seed(111)

# create an Empty DataFrame object
df = pd.DataFrame()
#creating user_id
merchant_ids =[]
merchant_name = []
merchant_type = ['NATIONAL','STATE','REGIONAL']
Category = ['MOBILE_RECHARGE','BROADBAND','UTILITY','GAS','CABLE']
comission=[]

for i in range(1,1000):
    merchant_ids.append('M'+f'{i:06}')
for i in range(1,1000):
    merchant_name.append(ourFake.company())
df['merchant_id'] = merchant_ids
df['merchant_name'] = merchant_name
df['merchant_type']= random.choices(merchant_type,k=len(df))
df['merchant_category']=random.choices(Category,k=len(df))
for i in range(1,1000):
    comission.append(round(random.uniform(1.00,9.99), 2))
df['commission']= comission

df.to_csv('merchants.csv')
print(str(df))



