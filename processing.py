import csv 


#FUNZIONE DA CONTROLLARE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def get_query_result(user_id, data, relational_table, query_set):

    # getting the list of tuples (query_id, percentage of liking) for a specific user
    queries = data[user_id]

    for i in range(0,len(queries)-1):
        #print("ful query:\n",queries[i])
        #tt = str.split(str(queries[i]))
        tt = queries[1]

        for j in range(0,len(query_set)-1):
            # print(query_set[j][0])
            # print("\n",tt[0])

            if tt == query_set[j][0]:
                #print("ecco\n",query_set[j])
                print("ecco\n")


    return query_set


all_data = {}

queries_log = []
users = []

id_user_test = 10

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


# let's divide all the date for each user

for user in users:
    list_values = []

    user = user.replace("\n", "")
    for query in queries_log:
        # if they have the same user_name
        if (user == query[0]):
            # tmp = []
            # tmp.append(query[1])
            # tmp.append(query[2])
            list_values.append((query[1], query[2]))
        
    all_data[user] = list_values

# reading the queries
query_set = []
with open("query_set.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:   
        query_set.append(row)
    
        
q.close()

# reading the rows in the relational table and save them in a list
relational_table = []

with open("Relational_table.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:   
        relational_table.append(row)
        
q.close()


# query_user = get_query_result("user_0129", all_data, relational_table, query_set)
#print("query_user: ", query_user[id_user_test])
print("query_set: ", query_set[id_user_test])
# for i in ecc:

#     print("ecco\n",i)
#print(query_set)

# reading the nicknames from the file and save them in a list (without the @)
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

# create a list of all the attributes
tags = []
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
#print("tags \n",tags[0])
#for i in range(len(all_data[0])):
#print(len(query_user[1762]))

#que = query_user[id_user_test]
que = query_set[id_user_test]
ind = []
content_creator_id_list = []

# range() starts from index 1 because we know that in position 0 there is the query_id
# we iterate for every hashtag ("hashtag_name = value")
for i in range(1,len(que)):

    # for every values, we want only the name of the value (like "name of hashtag" or "content_creator_ID")
    query_spl = str.split(que[i]," = ")

    # we have:
    # query_spl[0] = hashtag_name
    # query_spl[1] = value

    if query_spl[0] == "content_creator_ID":
        content_creator_id_list.append(query_spl[1])

    # if query_spl[0] = hashtag_name
    else:
        # we want the index of the hashtags in the relational table
        # we are going to iterate on the first row in the relational table, in which we have the names of the hashtags
        for k in range(0,len(relational_table[0])):
            if(query_spl[0] == (relational_table[0][k])):
                
                # now we have a list of tuples (index of hashtag in the relational table, value of that hashtag in the query)
                ind.append((k,query_spl[1]))
print(ind)
query_result = []

# this works only on the hashtag vector and not on the content creator id
# now we want to read every rows in the relational table (posts)



for row in relational_table:
    if (len(content_creator_id_list) != 0):
        for content_creator in content_creator_id_list:
            if (row[1] == content_creator):
                c = 0
                for index_hashtag, value in ind:
                    if(row[index_hashtag] == (value)):
                        c += 1
                    if(c == len(ind)):
                        query_result.append(row)

    else:
        c = 0
        for index_hashtag, value in ind:
            if(row[index_hashtag] == (value)):
                c += 1
            if(c == len(ind)):
                query_result.append(row)



print("query result:\n",len(query_result))
        
        #print("that'it:",i+2)
        