from faker import Faker
import random
ourFake = Faker()
Faker.seed(111)
random.seed(111)
print(ourFake.name())
import time

import pandas as pd

# create an Empty DataFrame object
df = pd.DataFrame()
mapping = pd.read_csv('sampled-payments.csv')
mapping = mapping[1:1000]
# mapping = mapping.sample(frac=0.1)
# mapping.to_csv('sampled-payments.csv')

print("mapping done")
# Ticket_Id char(7),
# 	 Transaction_Id char(10),
# 	 User_Id char(7),
# 	 Type varchar(20),
# 	 Status varchar(20),
#        Agent varchar(20),
#        created_timestamp timestamp,
#        resolved_timestamp timestamp,
# 	 primary key (Ticket_id),
# 	 foreign key (Transaction_id) references Payments (Transaction_Id),
# 	 foreign key (User_Id) references Users (User_Id)
ticket_ids=[]
for i in range(1,1000):
    ticket_ids.append('T'+f'{i:06}')
df['ticket_id'] = ticket_ids
created_timestamp=[]
for i in range(1,1000):
    created_timestamp.append(ourFake.date_time_this_year())
type =['MERCHANT_REVERSAL','BANK_REVERSAL','FAILED_TRANSACTION','USER_ISSUE','APP_LATENCY','MERCHANT_REVERSAL','BANK_REVERSAL','FAILED_TRANSACTION','MERCHANT_REVERSAL','BANK_REVERSAL','FAILED_TRANSACTION','MERCHANT_REVERSAL','BANK_REVERSAL','FAILED_TRANSACTION']
Status = ['OPEN','RESOLVED','RESOLVED','RESOLVED','RESOLVED','RESOLVED','RESOLVED','RESOLVED','RESOLVED','RESOLVED','RESOLVED','RESOLVED']
Agent_name = ['Sasi','Sati','Krupa','illi','Messi','Ronaldo','Alba','Rayleigh','chappel','pant','gamg','mixa']
user_id =[]
transaction_id = []
resolved_timestamp=[]
print("tickets created")
print(mapping)
df['type']= random.choices(type,k=len(df))
df['agent_name']= random.choices(Agent_name,k=len(df))
df['status'] = random.choices(Status,k=len(df))
df['user_id'] = mapping['user_id']
df['transaction_id'] = mapping['transaction_id']

df['created_timestamp']  = created_timestamp
for i in range(len(df)):
    if(df.loc[i,'status']=="OPEN"):
        resolved_timestamp.append("infinity")
    else:
        resolved_timestamp.append(ourFake.date_time_this_year())

df['resolved_timestamp'] = resolved_timestamp
df = df[['ticket_id','transaction_id','user_id','type','status','agent_name','created_timestamp','resolved_timestamp']]
df.to_csv('tickets.csv')

