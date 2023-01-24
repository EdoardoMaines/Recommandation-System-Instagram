import csv 

def retrieve_batch(query_index):
    que = query_set[query_index]
    ind = []
    post_id_of_cc = []
    for i in range(1,len(que)):
        query_spl = str.split(que[i],"=")        
        if "content_creator_ID " == query_spl[0]:
            for k in range(0,len(relational_table)):
                if (" "+relational_table[k][1]) == query_spl[1]:
                        post_id_of_cc.append(relational_table[k][0]) #append the id of the content_creator 

        if query_spl[0] != "content_creator_ID ":
            for k in range(0,len(relational_table[0])):
                if(query_spl[0] == (relational_table[0][k]+" ")):
                    #print("\n numero posizionale = ",k)
                    ind.append((k,query_spl[1]))
    #print("\nindice ",ind)
    #print("\npost of the content creators in the query:\n",len(post_id_of_cc))
    query_result = []
    for j in relational_table: #this works only on the hashtag vector and not on the content creaqtor id
        c = 0
        #print("nuovo post\n")
        for i,o in ind:
            #print(j[i],o)
            if(" "+j[i] == (o)):
                c += 1
            if(c == len(ind)) and len(post_id_of_cc)==0 :  #(j[0] in set(post_id_of_cc))
                query_result.append(j)
                c == 0
            elif(len(post_id_of_cc)>0 and (j[0] in set(post_id_of_cc))):
                query_result.append(j)
                c == 0
    return query_result
    
def sum_vector(batch_of_post):
    encoded_vector = []
    
    for j in range(2,len(batch_of_post[0])):
        tmp = 0
        for i in range(0,len(batch_of_post)):
            tmp += int(batch_of_post[i][j])
        encoded_vector.append(tmp)


    #encoded_vector = sum(batch_of_post)
    return encoded_vector


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

nickname = []
with open("creator_nickname.csv") as f:
        lines = f.readlines()
        
        for raw in lines:
            word = str.split(raw)
            for i in word:
                i = str.replace(i,"@","")
                nickname.append(i)
                
        f.close()
  
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

encoded = []
#s = retrieve_batch(0)
#print(s)
for i in range(0,15):

    query_result = retrieve_batch(i) #take as input the index of the query_set
    print("query result len: ",len(query_result),"\n")
    if len(query_result) != 0:


        encoded.append(sum_vector(query_result))
print("encoded:\n",len(encoded))
