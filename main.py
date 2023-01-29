import os
import csv
import numpy as np
import random

# \start 
# FUNCTIONS

def random_hashtag_values():
    one = 1
    zero = 0
    a = np.random.normal(loc=0.0, scale=1.0, size=None)
    if(a>0.5):
        return one
    else:
        return zero

def rnd_query():
    query_len = np.random.randint(0,8)
    name_len = np.random.randint(0,4)
    query = []
    query_name = []
    for j in range(name_len):
        query_name.append(np.random.randint(0,300))
    for i in range(query_len):
        query.append(np.random.randint(2,369))
    #print("query len: ",query_len)
    #print("names len: ",name_len)

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
            q = str(attribute[i])+' = '+str(random_hashtag_values())
            query.append(q)
        query.insert(0,'query_'+str(k).zfill(5))
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

def create_query_log(users, queries_set,relational_table):

    list_index_hashtags = []
    for i in range(2, 398):
        list_index_hashtags.append(i)

    random.shuffle(list_index_hashtags)
    user_queries = []

    for user in users:        
        lista1,lista2,lista3 = [],[],[]
        lis1,lis2,lis3 = [],[],[]

        # n_1 = np.random.randint(1,20)
        # n_2 = np.random.randint(1,20)
        # n_3 = np.random.randint(1,20)
        n_1 = 132 
        n_2 = 264
        n_3 = 396
        for j in range(0,n_1):
            lista1.append(list_index_hashtags[j])
        for j in range(n_1,n_2):
            lista2.append(list_index_hashtags[j])
        for j in range(n_2,n_3):
            lista3.append(list_index_hashtags[j])
            #lista3.append(np.random.randint(2,398))
        # lista1 = set(lista1)
        # lista2 = set(lista2)
        # lista3 = set(lista3)
        # inters = set.intersection(lista1,lista2,lista3)
        # #print(inters)
        # if len(inters) == 0:

        for i in lista1:
            lis1.append(relational_table[0][i])
        for i in lista2:
            lis2.append(relational_table[0][i])
        for i in lista3:
            lis3.append(relational_table[0][i])
        #print("\nlis 1 chaaaaaarrrr:",lis1)
        bella = 0
        for i in queries_set:
            count1 = 0
            count2 = 0
            count3 = 0
            count = 0
            query_ID = i[0]
            perc = 0
            perc1 = 0
            perc2 = 0
            perc3 = 0

            for t in range(1,len(i)):

                canna = str.split(i[t]," = ")
                #print("\n",[canna[0]])
                if (canna[0] == "content_creator_ID"):
                    bella += 1
                else:
                    if canna[0] in lis1 and canna[1]== "1":
                        #print("\n",[canna[0]])
                        count1 += 1
                        count += 1
                        
                        #user_queries.append([user[0],query_ID,str(perc/100)])

                    # elif count==n_1:
                        perc = np.random.randint(80,101)
                        perc1 += perc
                    #     user_queries.append([user[0],query_ID,str(perc/100)])

                    if canna[0] in lis2  and canna[1]== "1":
                        count2 += 1
                        count += 1
                        
                    # elif count==(n_2):
                        perc = np.random.randint(50,71)
                    #     user_queries.append([user[0],query_ID,str(perc/100)])
                        perc2 += perc

                    if canna[0] in lis3  and canna[1]== "1":
                        count3 += 1
                        count += 1
                        
                    # elif count==(n_3):
                        perc = np.random.randint(5,31)
                    #     user_queries.append([user[0],query_ID,str(perc/100)])
                        perc3 += perc
                   
            if count>=6:
                #perc = ((count1*perc1)+(count2*perc2)+(count3*perc3))/(count1+count2+count3)
                #perc = round(perc, 2)

                perc = ((perc1*2.5)+(perc2*2)+(perc3*1.5))/((2.5*count1)+(2*count2)+(1.5*count3))
                user_queries.append([user[0],query_ID,str(perc/100)])

            #print(count)

    # num_queries = np.random.randint(100,300)
    # np.random.shuffle(queries)
    # for i in range(0, num_queries):
    #     perc = np.random.randint(0,101)
    #     user_queries.append([user[0],queries[i],str(perc/100)])
    #     #lista1 = np.random
    #     #if ( in lista1)
        
    #print("Ciao: ", len(ciao))
            #print("1: ", count1, "2: ", count2, "3: ", count3)
    else:(
        print("Frate guarda che hanno intersezione")
    )
    return user_queries


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
def get_random_creator_ID (names):
    num_rand = np.random.randint(0, 300)
    name = names[num_rand]
    
    return name

# \end 
# FUNCTIONS

attribute = ['Post_ID','content_creator_ID']
tags = extract_tags('raw_hashtags.csv',attribute)
names = []
extract_names('creator_nickname.csv', names)
print("\nPORCODIO \n")
#print(attribute)
print("LUNGHEZZA NAMES: ", len(names))
# open the file in the write mode
f = open('Relational_table.csv', 'w')

# create the csv writer
writer = csv.writer(f)
print("NOME CASUALE: ", get_random_creator_ID(names))
# write a row to the csv file
writer.writerow(attribute)
f.close()


relational_table = []

with open("Relational_table.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:   
        relational_table.append(row)
        
q.close()

query_set = []
with open("query_set.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:   
        query_set.append(row)



f = open('Relational_table.csv','a')
writer = csv.writer(f)
random_list_tags = []
random_Cre_ID = []
for j in range(1,20000):
    random_list_tags.clear()
    random_list_tags.append(str(j).zfill(4))
    #random_list_tags.append(names[j])
    if j < 301:
        random_list_tags.append(names[j-1])
    else:
        if 301 < j < 600:
            random_list_tags.append(names[j-301])
        else:
            random_list_tags.append(get_random_creator_ID(names))
    
    for i in range(0,396):
        # a = np.random.normal(loc=0.0, scale=1.0, size=None)
        # if(a>1):
        #     random_list_tags.append(1)
        # else:random_list_tags.append(0)
        random_list_tags.append(random_hashtag_values())
    
    writer.writerow(random_list_tags)


f.close()

f = open('query_set.csv','w')
writer = csv.writer(f)
num_query = 20000
query = create_query(attribute,names,num_query)

#print(query)
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

lista_bella = create_query_log(user_set, query_set, relational_table)
#lista_bella = create_query_log(user_set, queries_id)
np.random.shuffle(lista_bella)

for i in range(0,len(lista_bella)):
    writer.writerow(lista_bella[i])

f.close()

# close the file


