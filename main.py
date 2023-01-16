import os
import csv
import numpy as np

<<<<<<< HEAD
def rnd_query():
    query_len = np.random.randint(0,15)
    name_len = np.random.randint(0,5)
    query = []
    query_name = []
    for j in range(name_len):
        query_name.append(np.random.randint(0,300))
    for i in range(query_len):
        query.append(np.random.randint(2,369))
    print("query len: ",query_len)
    print("names len: ",name_len)

    if query_len == 0 and name_len == 0:
        query, query_name = rnd_query()
          
    return (set(query),set(query_name))

def create_query(attribute,names,n_query):
    query_set = []
    for k in range(1,n_query+1):
        query_hash, query_name = rnd_query()
        query = []
        
        for i in query_name:
            q = str(attribute[1])+' = '+str(names[i])
            query.append(q)
        for i in query_hash:
            q = str(attribute[i])+' = '+str(np.random.randint(0,2))
            query.append(q)
        query.insert(0,'query_'+str(k).zfill(4))
        query_set.append(query)
        #query.clear()
    return set(tuple(i) for i in query_set)

def create_user(n_user):
    user_set = []
    for k in range(1,n_user+1):
        user = []
        user.append(str('user_'+str(k).zfill(4)))        
        user_set.append(user)
        
        #query.clear()
    return user_set

def create_query_log(users, queries):

    
    user_queries = []

    for user in users:        
        
        num_queries = np.random.randint(100,300)
        np.random.shuffle(queries)
        for i in range(0, num_queries):
            perc = np.random.randint(0,101)
            user_queries.append([user[0],queries[i],str(perc/100)])
            

        
    return user_queries
    #user_id = np.random.randint(0,len(users))
    #query_id = np.random.randint(0,len(queries))

    #user = users[user_id]
    #query = queries[query_id]



def extract_tags(path,tags):
    c = 0
    with open(path) as f:
        lines = f.readlines()
        
        for raw in lines:
            word = str.split(raw)
            for i in word:
                i = str.replace(i,"#","")
                tags.append(i)
                c=c+1
                #print(c)
    
def extract_names(path,tags):
    c = 0
    with open(path) as f:
        lines = f.readlines()
        
        for raw in lines:
            word = str.split(raw)
            for i in word:
                i = str.replace(i,"@","")
                tags.append(i)
                c=c+1

attribute = ['Post_ID','content_creator_ID']
tags = extract_tags('raw_hashtags.csv',attribute)
names = []
extract_names('creator_nickname.csv', names)
print("\nPORCODIO \n")
print(attribute)

# open the file in the write mode
f = open('Relational_table.csv', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerow(attribute)
f.close()

f = open('Relational_table.csv','a')
writer = csv.writer(f)
random_list_tags = []
random_Cre_ID = []
for j in range(0,200):
    random_list_tags.clear()
    random_list_tags.append(str(j).zfill(4))
    random_list_tags.append(names[j])

    for i in range(0,396):
        a = np.random.normal(loc=0.0, scale=1.0, size=None)
        if(a>1):
            random_list_tags.append(1)
        else:random_list_tags.append(0)
    
    writer.writerow(random_list_tags)
f.close()

f = open('query_set.csv','w')
writer = csv.writer(f)
num_query = 5000
query = create_query(attribute,names,num_query)

print(query)
# for query_ in query:
#     print("PROVA GET ID QUERY: ", query_[1][0])

for query_ in query:
    writer.writerow(query_)

# for i in range(num_query):
#     writer.writerow(query[i])
f.close()

user_num = 500
f = open('users.csv','w')
user_set = create_user(user_num)
writer = csv.writer(f)
print(user_set[1])
np.random.shuffle(user_set)
for i in range(0,user_num):
    writer.writerow(user_set[i])
f.close()

queries_id = []
with open("query_set.csv") as q:
    for row in q:
        queries_id.append(row.split(",")[0])
q.close()

f = open('query_log.csv', 'w')
writer = csv.writer(f)

lista_bella = create_query_log(user_set, queries_id)
np.random.shuffle(lista_bella)

for i in range(0,len(lista_bella)):
    writer.writerow(lista_bella[i])
#print(lista_bella[:5])
# for k in range(100):
        
#     query_hash, query_name = rnd_query()
#     query = []
    
#     for i in query_name:
#         q = str(attribute[1])+' = '+str(names[i])
#         query.append(q)
#     for i in query_hash:
#         q = str(attribute[i])+' = '+str(np.random.randint(0,2))
#         query.append(q)
#     print(query) 
#     query.insert(0,'query_'+str(k).zfill(4))
#     writer.writerow(query)
#     query.clear()
f.close()







# close the file


=======
all_data = {}

queries_log = []
users = []


with open("query_log.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:   
        queries_log.append(row)
        
q.close()

with open("users.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:        
        users.append(row[0])
        
q.close()
#print(queries_log[0][1])


#Let's divide all the date for each user

for user in users:
    list_values = []

    user = user.replace("\n", "")
    for query in queries_log:
        #if they have the same user_name
        if (user == query[0]):
            # tmp = []
            # tmp.append(query[1])
            # tmp.append(query[2])
            list_values.append((query[1], query[2]))
        
    all_data[user] = list_values

print((all_data))
>>>>>>> edd858cd3fd96b068a125c7e10b45d0777726684
