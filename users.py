from faker import Faker
import random
ourFake = Faker()
Faker.seed(111)
random.seed(111)
print(ourFake.name())

import pandas as pd

# create an Empty DataFrame object
df = pd.DataFrame()
#creating user_id
user_ids =[]
names=[]
salary = []
address=[]
street_name = []
email= []
for i in range(1,1000):
    user_ids.append('U'+f'{i:06}')

for i in range(1,1000):
    names.append(ourFake.name())
for i in range(1,1000):
    salary.append(random.randint(60000,200000))
for i in range(1,1000):
    address.append('A'+f'{i:06}')
for i in range(1,1000):
    street_name.append(ourFake.street_address())
for i in range(1,1000):
    email.append(ourFake.email())

df['user_id'] = user_ids
df['name'] = names
df['address_id'] = address
df['street_name']=street_name
df['salary'] = salary
df['email']=email

df.to_csv('users.csv')
print(str(df))
