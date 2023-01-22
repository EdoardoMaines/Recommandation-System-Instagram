import csv 

# reading the query_log
queries_log = []
with open("query_log.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:   
        queries_log.append(row)        
q.close()

# reading the users' names
users = []
with open("users.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:        
        users.append(row[0])        
q.close()

# let's divide all the date for each user
all_data = {}
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



##### SCRIPT #####

# save in a dict all the result of queries from the relational table
# key: query_ID
# values: posts resulted by the query
queries_results = {}

id_user_test = 3 #690
for i in range(0, len(query_set)):

    #print("query_set: ", query_set[i])
    #print("query_ID: ", query_set[i][0])
    query_ID = query_set[i][0]
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
    #print(ind)
    query_result = []

    # this works only on the hashtag vector and not on the content creator id
    # now we want to read every rows in the relational table (posts)


    #print(content_creator_id_list)

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

    if len(query_result) == 0:
        print("\nLa query ", query_ID, " non da nessun risultato")


    #print("query result:\n",len(query_result))
    queries_results[query_ID] = query_result

#print(queries_results["query_4912"])
#print(len(queries_results["query_4912"]))
        