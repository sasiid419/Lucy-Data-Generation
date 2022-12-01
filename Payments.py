from faker import Faker
import random
import pandas as pd
ourFake = Faker()
Faker.seed(111)
random.seed(111)
# 

#Transaction_ID	User_Id	Merchant_Id	Store_Id	State	Category	Inst	Timestamp	Amount	Reciever_Id
#T000000001	U000007	null null	SUCCESS	PEER-PEER	ACCOUNT	1/9/2022 9:59	93.32	U000004

# Transaction_Id char(10) ,
# 	 User_Id char(7) not null,
# 	 Merchant_Id char(7),
# 	 State varchar(30),
# 	 Store_Id char(7),
# 	 Category varchar(20),
# 	 Payment_Instrument varchar(20),
# 	 Payment_timestamp timestamp not null,
# 	 Amount decimal(8,2) check (amount >0),
# 	 Receiver_Id varchar(7),
# 	 primary key (Transaction_id),
# 	 foreign key (Merchant_Id) references Merchants (Merchant_Id),
#        foreign key (Store_Id) references Stores(Store_Id),
#        foreign key (User_Id) references Users(User_Id)
mapping = pd.read_csv('stores.csv')

Payment_state = ['SUCCESS','FAILED','PENDING_FROM_MERCHANT','PENDING_FROM_BANK','SUCCESS','SUCCESS','SUCCESS','SUCCESS','SUCCESS','SUCCESS','SUCCESS','SUCCESS','SUCCESS']
Payment_Category =['MOBILE_RECHARGE','BROADBAND','UTILITY','GAS','CABLE','PEER-PEER','PEER-PEER','PEER-PEER','PEER-PEER','PEER-PEER','PEER-PEER','PEER-PEER','PEER-PEER']
Payment_Instrument = ['ACCOUNT','CREDIT_CARD','DEBIT_CARD','WALLET','ACCOUNT','ACCOUNT','ACCOUNT','ACCOUNT','ACCOUNT','ACCOUNT']
df = pd.DataFrame()
transaction_ids =[]
amount=[]
for i in range(1,1100000):
    transaction_ids.append('T'+f'{i:09}')
    amount.append(round(random.uniform(1.00, 99.99), 2))
df['transaction_id']= transaction_ids
user_ids = []
for i in range(1,1000):
    user_ids.append('U'+f'{i:06}')
#M001000  LUCY  nattional peer-peer commision 1.5
df['user_id'] = random.choices(user_ids,k=len(df))
df['payment_category'] = random.choices(Payment_Category,k=len(df))
df['payment_state'] = random.choices(Payment_state,k=len(df))
df['Payment_instrument'] = random.choices(Payment_Instrument,k=len(df))
timestamp = []
for i in range(1,1100000):
    timestamp.append(ourFake.date_time_this_decade())
    print("done..")
df['timestamp'] = timestamp
count=0
reciever_id = []
store_id =[]
merchant_id = []
for i in range(len(df)):
    if(df.loc[i,"payment_category"]=='PEER-PEER'):
        j=i%999
        reciever_id.append(user_ids[j])
        merchant_id.append('M001000')
        store_id.append("S000000")
    else:
        reciever_id.append("null")
        j =i%2999
        merchant_id.append(mapping.loc[j,"Merchant_id"])
        store_id.append(mapping.loc[j,"store_id"])
df['reciever_id'] = reciever_id
df['merchant_id'] = merchant_id
df['store_id'] = store_id
df['amount'] = amount
df = df[['transaction_id', 'user_id', 'merchant_id','payment_state','store_id','payment_category','Payment_instrument','timestamp','amount','reciever_id']]
print(df)
df.to_csv('payments.csv')
