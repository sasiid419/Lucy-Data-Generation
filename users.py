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
state =[]
city =[]
email= []
for i in range(1,1000):
    user_ids.append('U'+f'{i:06}')

for i in range(1,1000):
    names.append(ourFake.name())
for i in range(1,1000):
    salary.append(random.randint(60000,200000))
for i in range(1,1000):
    state.append(ourFake.state())
for i in range(1,1000):
    city.append(ourFake.city())
for i in range(1,1000):
    email.append(ourFake.email())

df['user_id'] = user_ids
df['name'] = names
df['salary'] = salary
df['state'] = state
df['city']=city
df['email']=email

df.to_csv('users.csv')
print(str(df))
