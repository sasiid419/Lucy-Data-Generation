from faker import Faker
import random
import pandas as pd
ourFake = Faker()
Faker.seed(111)
random.seed(111)
import pandas as pd

# create an Empty DataFrame object
df = pd.DataFrame()


mapping = pd.read_csv('tickets.csv')
refund_ids=[]
ticket_ids=[]
transaction_id =[]
amount =[]
reason =['FAILED_TRANSACTION','PENDING_TRANSACTION','CANCELLED']
for i in range(1,100):
    refund_ids.append('T'+f'{i:09}')
for i in range(1,100):
    amount.append(round(random.uniform(1.00,9.99), 2))
df['refund_id'] = refund_ids
df['amount'] = amount
df['reason'] =random.choices(reason,k=len(df))
for i in range(len(df)):
    ticket_ids.append(mapping.loc[i,'ticket_id'])
    transaction_id.append(mapping.loc[i,'transaction_id'])
df['ticket_id'] = ticket_ids
df['transaction_id'] = transaction_id
print(df)
# Refund_Id char(10),
# 	 Transaction_Id char(10),
# 	 Ticket_Id char(7),
#        Amount decimal(8,2),
#        Reason Varchar(20),
# 	 primary key (Refund_Id),
# 	 foreign key (Transaction_id) references Payments (Transaction_Id),
# 	 foreign key (Ticket_Id) references Tickets (Ticket_Id) set null
df=df[['refund_id','transaction_id','ticket_id','amount','reason']]
df.to_csv('refunds.csv')