from faker import Faker
import random
import pandas as pd
ourFake = Faker()
Faker.seed(111)
random.seed(111)
# create an Empty DataFrame object
df = pd.DataFrame()
#creating user_id
store_ids =[]
for i in range(1,3000):
    store_ids.append('S'+f'{i:06}')
df['store_id'] = store_ids
merchant_ids=[]
for i in range(1,1000):
    merchant_ids.append('M'+f'{i:06}')
df['Merchant_id'] =random.choices(merchant_ids,k=len(df))
address=[]
for i in range(1,3000):
    address.append('A'+f'{i:06}')
df['address_id'] = address
street=[]
for i in range(1,3000):
    street.append(ourFake.street_address())
df['street'] = street
Tax=[]
for i in range(1,3000):
    Tax.append(round(random.uniform(1.00,9.99), 2))
df['Tax'] =Tax
df.to_csv('stores.csv')
print(df)

# Store_Id char(7),
# 	 Merchant_Id char(7),
#        State varchar(20),
# 	 City varchar(20),
# 	 Tax decimal(4,2),
# 	 primary key (Store_Id),
# 	 foreign key (Merchant_Id) references Merchants(Merchant_Id)