import csv 

def get_query_result(user_id,Data,relational_table,query_set):
    queries = Data[user_id]
    for i in range(0,len(queries)-1):
        #print("ful query:\n",queries[i])
        #tt = str.split(str(queries[i]))
        tt = queries[1]

        for j in range(0,len(query_set)-1):
            # print(query_set[j][0])
            # print("\n",tt[0])

            if tt == query_set[j][0]:
                print("ecco\n",query_set[j])

    return query_set


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

##reading the queries
query_set = []
with open("query_set.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:   
        query_set.append(row)
    
        
q.close()
relational_table = []

with open("Relational_table.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:   
        relational_table.append(row)
        
q.close()
query_user = get_query_result("user_0129",all_data,relational_table,query_set)
print("ecco\n",query_user[1873])
# for i in ecc:

#     print("ecco\n",i)
#print(query_set)
nickname = []
with open("creator_nickname.csv") as f:
        lines = f.readlines()
        
        for raw in lines:
            word = str.split(raw)
            for i in word:
                i = str.replace(i,"@","")
                nickname.append(i)
                
        f.close()
#print(nickname)
# counter = 0
# for nick in nickname:
#     print("nickname:  ",nick)
#     counter += 1
  
tags = []                                    #create a list of all the attributes
c = 0
with open("raw_hashtags.csv") as f:
    lines = f.readlines()
        
    for raw in lines:
        word = str.split(raw)
        for i in word:
            i = str.replace(i,"#","")
            tags.append(i)
            c=c+1
                #print(c)
print("tags \n",tags[0])
#for i in range(len(all_data[0])):
print(len(query_user[1774]))

que = query_user[1774]
ind = []
for i in range(1,len(que)):
    query_spl = str.split(que[i],"=")
    for j in range(0, len(query_spl)-1,2):
        #print("\ncheck:", query_spl[0])
        if "content_creator_ID " == query_spl[0]:
            print("FORSE",query_spl[0])
            

            for k in range(0,len(relational_table)):
                #print("\n",relational_table[k][1])
                #print(relational_table[k][1])
                if (" "+relational_table[k][1]) == query_spl[1]:
                    print("\nFATTA FACCIAMO UNA CANNA")
        if query_spl[0] != "content_creator_ID ":
            for k in range(0,len(relational_table[0])):
                if(query_spl[0] == (relational_table[0][k]+" ")):
                    print("\nFUCK Motherfucker")
                    print("\n numero = ",k)
                    ind.append((k,query_spl[1]))
print(ind)
query_result = []
for j in relational_table: #this works only on the hashtag vector and not on the content creaqtor id
    c = 0
    print(j)
    for i,o in ind:
        print(j[i],i)
        if (j[i] == o):
            c += 1
            #print("bene\n",c)
        if(c == len(ind)-1):
            query_result.append(j)
print("query result:\n",query_result)
        
        #print("that'it:",i+2)
        