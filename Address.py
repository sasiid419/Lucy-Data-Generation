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
address =[]
state =[]
city =[]
for i in range(1,10000):
    address.append('A'+f'{i:06}')

for i in range(1,10000):
    state.append(ourFake.state())
for i in range(1,10000):
    city.append(ourFake.city())

df['address_id'] = address
df['state'] = state
df['city']=city


df.to_csv('address.csv')
print(str(df))
