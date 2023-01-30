import os
import csv
import numpy as np
import random

from tqdm import tqdm
from processing_2 import retriev_query, retrieve_batch, sum_vector
# \start 
# FUNCTIONS

def random_hashtag_values_():
    one = 1
    zero = 0
    a = np.random.normal(loc=0.0, scale=1.0, size=None)
    if(a>0.5):
        return one
    else:
        return zero


def random_hashtag_values(i,f,tt):
    one = 1
    zero = 0
    if tt==1:
        if i < f:
            a = np.random.normal(loc=0.0, scale=1.0, size=None)
            if(a>0.001):
                return one
            else:
                return zero
        if i>=f:
            a = np.random.normal(loc=0.0, scale=1.0, size=None)
            if(a>6):
                return one
            else:
                return zero
    else:
        if i < f:
            a = np.random.normal(loc=0.0, scale=1.0, size=None)
            if(a>6):
                return one
            else:
                return zero
        if i>=f:
            a = np.random.normal(loc=0.0, scale=1.0, size=None)
            if(a>0.001):
                return one
            else:
                return zero
        


def rnd_query():
    query_len = np.random.randint(10,20)
    name_len = np.random.randint(0,2)
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
            q = str(attribute[i])+' = '+str(random_hashtag_values_())
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

# def create_query_log(users, queries):

    
#     user_queries = []

#     for user in users:        
        
#         num_queries = np.random.randint(100,300)
#         np.random.shuffle(queries)
#         for i in range(0, num_queries):
#             perc = np.random.randint(0,101)
#             user_queries.append([user[0],queries[i],str(perc/100)])
            
def liking_percentage(freq_vector, l1, l2):
    perc = 0
    w1 = 3
    w2 = 0.5
    perc1,perc2 = 0,0
    #print("1", freq_vector[1])
    #print("0", freq_vector[0])
    p = 0
    n = 0
    for j in l1:
        perc1 += freq_vector[1][int(j)-2]
        p += 1 
    for h in l2:
        perc2 += freq_vector[1][int(h)-2]
        n += 1
    perc = ((perc1*w1+perc2*w2)/(w1+w2))/(perc1+perc2)
    # perc1 = perc1/p
    # perc2 = perc2/n
    
    #print("\nqueste sono le altre percentuali : ",perc1,"___",perc2)
    #print("\nperc1: ",perc1,"perc2: ",perc2)
    id = freq_vector[0]
    

    return perc,id


def from_query_to_frequency(queries):
    list_tot = []
    frequency_vector = []
    list_ = []
    for i in tqdm(range(len(queries))):
        query_result = retrieve_batch(i,queries)
        
        #print("QUERY RESULT:", len(query_result))
        list_tot.append(query_result)
        if len(query_result) != 0:
            list_.append(query_result)
            frequency_vector.append((queries[i][0],sum_vector(query_result)))

    return frequency_vector




#     return user_queries

def create_query_log(users, queries_set,relational_table):

    list_index_hashtags = []
    for i in range(2, 398):
        list_index_hashtags.append(i)

    #random.shuffle(list_index_hashtags)
    list_positive_index = list_index_hashtags[:190]
    list_negative_index = list_index_hashtags[220:]
    #random.shuffle(list_positive_index)
    #random.shuffle(list_negative_index)
    user_queries = []

    frequency_vector = from_query_to_frequency(queries_set)
    #print(frequency_vector[:5])
    dic_preferences = {}
    for user in users:        
        lista1,lista2,lista3 = [],[],[]
        lis1,lis2,lis3 = [],[],[]

        # n_1 = np.random.randint(1,20)
        # n_2 = np.random.randint(1,20)
        # n_3 = np.random.randint(1,20)
        n_1 = 132 
        n_2 = 264
        n_3 = 396
        for j in range(0,len(list_positive_index)-30):
            lista1.append(list_positive_index[j])
        for j in range(0,len(list_negative_index)-30):
            lista3.append(list_negative_index[j])
            #lista3.append(np.random.randint(2,398))
        
        f = open("dict_preferences.csv","a")
        writer = csv.writer(f)
        dic_preferences = (user,lista1,lista3)

        for i in range(len(dic_preferences)):
            writer.writerow(dic_preferences[i])
        # lista1 = set(lista1)
        # lista2 = set(lista2)
        # lista3 = set(lista3)
        # inters = set.intersection(lista1,lista2,lista3)
        # #print(inters)
        # if len(inters) == 0:

        for i in lista1:
            lis1.append(relational_table[0][i])
        for i in lista3:
            lis3.append(relational_table[0][i])
        #print("\nlis 1 chaaaaaarrrr:",lis1)
        #bella = 0
        for i in range(len(frequency_vector)):
            perc, q_ID = liking_percentage(frequency_vector[i], lista1, lista3)
            user_queries.append([user[0],q_ID,str(round(perc,2))])

        #     count1 = 0
        #     count2 = 0
        #     count3 = 0
        #     count = 0
        #     query_ID = i[0]
        #     perc = 0
        #     perc1 = 0
        #     perc2 = 0
        #     perc3 = 0

        #     for t in range(1,len(i)):

        #         canna = str.split(i[t]," = ")
        #         #print("\n",[canna[0]])
        #         if (canna[0] == "content_creator_ID"):
        #             bella += 1
        #         else:
        #             if canna[0] in lis1 and canna[1]== "1":
        #                 #print("\n",[canna[0]])
        #                 count1 += 1
        #                 count += 1
                        
        #                 #user_queries.append([user[0],query_ID,str(perc/100)])

        #             # elif count==n_1:
        #                 perc = np.random.randint(80,101)
        #                 perc1 += perc
        #             #     user_queries.append([user[0],query_ID,str(perc/100)])

        #             if canna[0] in lis2  and canna[1]== "1":
        #                 count2 += 1
        #                 count += 1
                        
        #             # elif count==(n_2):
        #                 perc = np.random.randint(50,71)
        #             #     user_queries.append([user[0],query_ID,str(perc/100)])
        #                 perc2 += perc

        #             if canna[0] in lis3  and canna[1]== "1":
        #                 count3 += 1
        #                 count += 1
                        
        #             # elif count==(n_3):
        #                 perc = np.random.randint(5,31)
        #             #     user_queries.append([user[0],query_ID,str(perc/100)])
        #                 perc3 += perc
                   
        #     if count>=1:
        #         #perc = ((count1*perc1)+(count2*perc2)+(count3*perc3))/(count1+count2+count3)
        #         #perc = round(perc, 2)

        #         perc = ((perc1*2.5)+(perc2*0.5)+(perc3*1.5))/((2.5*count1)+(0.5*count2)+(1.5*count3))
        #         user_queries.append([user[0],query_ID,str(perc/100)])

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


f = open('Relational_table.csv','a')
writer = csv.writer(f)
random_list_tags = []
random_Cre_ID = []
for j in range(1,50000):
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
    
    tt = np.random.randint(0,2)
    rnd = np.random.randint(50,347)

    for i in range(0,396):
        # a = np.random.normal(loc=0.0, scale=1.0, size=None)
        # if(a>1):
        #     random_list_tags.append(1)
        # else:random_list_tags.append(0)
        
        random_list_tags.append(random_hashtag_values(i,rnd,tt))
    
    writer.writerow(random_list_tags)


f.close()


relational_table = []

with open("Relational_table.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:   
        relational_table.append(row)
        
q.close()

f = open('query_set.csv','w')
writer = csv.writer(f)
num_query = 3000
query = create_query(attribute,names,num_query)
for query_ in query:
    writer.writerow(query_)


f.close()

query_set = []
with open("query_set.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:   
        query_set.append(row)






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


