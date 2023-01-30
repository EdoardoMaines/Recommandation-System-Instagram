import csv
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler 
from sklearn import decomposition
from sklearn import datasets
from sklearn.cluster import KMeans
import numpy as np
# unused but required import for doing 3d projections with matplotlib < 3.2
import mpl_toolkits.mplot3d  # noqa: F401

def distance_from_centroid(frequency_vect,centroid):
    dist = np.linalg.norm(frequency_vect-centroid)

    return dist


def retriev_query(query_id):
    a = 0

    for i in range(0,len(query_set)):
        if query_set[i][0] == query_id:
            a = i
            break

    return a

def retrieve_batch(query_index,query_set):
    que = query_set[query_index]
    ind = []
    content_creator_id_list = []
    post_id_of_cc = []
    query_result = []
    empty = []
    for i in range(1,len(que)):
        query_spl = str.split(que[i],"=")        
        if "content_creator_ID " == query_spl[0]:
            content_creator_id_list.append(query_spl[1])
            for k in range(0,len(relational_table)): #da cambiare con all_data
                if (" "+relational_table[k][1]) == query_spl[1]:
                        post_id_of_cc.append(relational_table[k][0]) #append the id of the content_creator 

        if query_spl[0] != "content_creator_ID ":
            for k in range(0,len(relational_table[0])):
                if(query_spl[0] == (relational_table[0][k]+" ")):
                    #print("\n numero posizionale = ",k)
                    ind.append((k,query_spl[1]))
    #print("\nindice ",ind)
    #print("\npost of the content creators in the query:\n",len(post_id_of_cc))
    # for j in relational_table: #this works only on the hashtag vector and not on the content creaqtor id
    #     c = 0
    #     #print("nuovo post\n")
    #     for i,o in ind:
    #         #print(j[i],o)
    #         if(" "+j[i] == (o)):
    #             c += 1
    #             if(c == len(ind)) and len(post_id_of_cc)==0:  #(j[0] in set(post_id_of_cc))
    #                 query_result.append(j)

    for i in range(len(relational_table)):
        c=0
        if len(post_id_of_cc) > 0:
            #print("post_id_of_cc: ", post_id_of_cc)
            if relational_table[i][0] in post_id_of_cc:
                #print("ciao")
                for indx,val in ind:
            #print(j[i],o)
                    if(" "+relational_table[i][indx] == (val)):
                        c += 1
                        if(c == len(ind)):  #(j[0] in set(post_id_of_cc))
                            #print("appende?")
                            query_result.append(relational_table[i])
        else:
            #if i in post_id_of_cc:
            
            for indx,val in ind:
        #print(j[i],o)
                if(" "+relational_table[i][indx] == (val)):
                    c += 1
                    if(c == len(ind)):  #(j[0] in set(post_id_of_cc))
                        #print("appende?")
                        query_result.append(relational_table[i])
                    else:
                        empty.append(relational_table[i])        

    return query_result
def get_frequency_list(query_log_user):
    empty_result = []
    query_asdf = []
    query_result = []
    list = []
    list_tot = []
    retrievd_percentage = []
    for i in range(0,len(query_log_user)):
        retrieved_query = retriev_query(query_log_user[i][0])
        retrievd_percentage.append(query_log_user[i][1])

        #print("retrieved query \n",retrieved_query)
        query_result = retrieve_batch(retrieved_query,query_set) #take as input the index of the query_set
        #print("CIAO")
        #print(query_result[:5])
        #query_result = batch_of_post(retrieved_query)
        #print(query_result[0])
        #print("query result len: ",query_result,"\n")
        list_tot.append(query_result)
        if len(query_result) != 0:
            list.append(query_result)

            #print("somma vettore\n\n",sum_vector(query_result))

            frequency_vector.append(sum_vector(query_result))
            #print("freq_vect\n",frequency_vector)
        if(len(query_result) == 0): 
            empty_result.append(1)
    # print("\nretrieved percentage = ",len(retrievd_percentage))

    # print("empty result ",len(empty_result))
    # print("non empty ", len(list))
    # print("tot ", len(list_tot))
    return frequency_vector, retrievd_percentage
def retrieve_batch(query_index,query_set):
    que = query_set[query_index]
    ind = []
    content_creator_id_list = []
    post_id_of_cc = []
    query_result = []
    empty = []
    for i in range(1,len(que)):
        query_spl = str.split(que[i],"=")        
        if "content_creator_ID " == query_spl[0]:
            content_creator_id_list.append(query_spl[1])
            for k in range(0,len(relational_table)): #da cambiare con all_data
                if (" "+relational_table[k][1]) == query_spl[1]:
                        post_id_of_cc.append(relational_table[k][0]) #append the id of the content_creator 

        if query_spl[0] != "content_creator_ID ":
            for k in range(0,len(relational_table[0])):
                if(query_spl[0] == (relational_table[0][k]+" ")):
                    #print("\n numero posizionale = ",k)
                    ind.append((k,query_spl[1]))
    #print("\nindice ",ind)
    #print("\npost of the content creators in the query:\n",len(post_id_of_cc))
    # for j in relational_table: #this works only on the hashtag vector and not on the content creaqtor id
    #     c = 0
    #     #print("nuovo post\n")
    #     for i,o in ind:
    #         #print(j[i],o)
    #         if(" "+j[i] == (o)):
    #             c += 1
    #             if(c == len(ind)) and len(post_id_of_cc)==0:  #(j[0] in set(post_id_of_cc))
    #                 query_result.append(j)

    for i in range(len(relational_table)):
        c=0
        if len(post_id_of_cc) > 0:
            #print("post_id_of_cc: ", post_id_of_cc)
            if relational_table[i][0] in post_id_of_cc:
                #print("ciao")
                for indx,val in ind:
            #print(j[i],o)
                    if(" "+relational_table[i][indx] == (val)):
                        c += 1
                        if(c == len(ind)):  #(j[0] in set(post_id_of_cc))
                            #print("appende?")
                            query_result.append(relational_table[i])
        else:
            #if i in post_id_of_cc:
            
            for indx,val in ind:
        #print(j[i],o)
                if(" "+relational_table[i][indx] == (val)):
                    c += 1
                    if(c == len(ind)):  #(j[0] in set(post_id_of_cc))
                        #print("appende?")
                        query_result.append(relational_table[i])
                    else:
                        empty.append(relational_table[i])        

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

relational_table = []

with open("Relational_table.csv", "r") as q:
    reader = csv.reader(q)
    for row in reader:   
        relational_table.append(row)
            
q.close()

if __name__ == '__main__':
    
    
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
    print("\nuser len:",len(users))
    ##reading the queries
    query_set = []
    with open("query_set.csv", "r") as q:
        reader = csv.reader(q)
        for row in reader:   
            query_set.append(row)    
            
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

    frequency_vector = []
    #s = retrieve_batch(0)
    #print(s)
    #query_set_user = all_data["user_0145"]
    query_log_user = list(all_data["user_0278"])

    print("aaaaaaaaal dataaaaaaaa\n",len(query_log_user))


        #query_set[query_id]
    frequency_list, retrievd_percentage= get_frequency_list(query_log_user)
    # empty_result = []
    # query_asdf = []
    # query_result = []
    # list = []
    # list_tot = []
    # retrievd_percentage = []
    # for i in range(0,len(query_log_user)):
    #     retrieved_query = retriev_query(query_log_user[i][0])
    #     retrievd_percentage.append(query_log_user[i][1])

    #     #print("retrieved query \n",retrieved_query)
    #     query_result = retrieve_batch(retrieved_query,query_set) #take as input the index of the query_set
    #     #print("CIAO")
    #     #print(query_result[:5])
    #     #query_result = batch_of_post(retrieved_query)
    #     #print(query_result[0])
    #     #print("query result len: ",query_result,"\n")
    #     list_tot.append(query_result)
    #     if len(query_result) != 0:
    #         list.append(query_result)

    #         #print("somma vettore\n\n",sum_vector(query_result))

    #         frequency_vector.append(sum_vector(query_result))
    #         #print("freq_vect\n",frequency_vector)
    #     if(len(query_result) == 0): 
    #         empty_result.append(1)
    # print("\nretrieved percentage = ",len(retrievd_percentage))
    # #print(len(list[0]))
    # #print(frequency_vector[-1])
    # print("empty result ",len(empty_result))
    # print("non empty ", len(list))
    # print("tot ", len(list_tot))
    # # #print("encoded:\n",len(frequency_vector))
    a = 0
    # print("\nquery result 0\n", query_result[0],"\nlen: ",len(query_result))
    # print("\nquery_asdf\n",query_asdf[0])
    # print(len(query_result))
    # for i in range(0,len(query_result)-1):
    #     a += int(query_result[i][2])


    #print("\nfrequ vect del primo \n",frequency_vector[0])
    print("\na: ", a)
    # print("\nempty ",len(empty_result))
    # #print(frequency_vector[0])

    encoded = np.array(frequency_vector)

    X = np.array(encoded)
    #print("X \n",len(X))
    # scaler = StandardScaler()

    # scaled_features = scaler.fit_transform(X)
    km = KMeans(
        n_clusters=2, init='random',
        n_init=30, max_iter=100, 
        tol=1e-04, random_state=42
    )
    #scaler = StandardScaler()
    #scaled_features = scaler.fit_transform(frequency_vector)
    scaler = StandardScaler()
    frequency_vector_scld = scaler.fit_transform(frequency_vector)
    km.fit(frequency_vector_scld)
    # kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X)
    km.labels_
    print("\nlabels: ",km.labels_,"labels_len: ",len(km.labels_))
    print("\nfrequency vector len: ", len(frequency_vector_scld))
    #kmeans.predict([[0, 0], [12, 3]])
    pred1 = km.predict([frequency_vector_scld[0]])
    print(frequency_vector_scld[0])
    print(frequency_vector_scld[1])
    print(frequency_vector_scld[2])
    print(frequency_vector_scld[3])
    print("ciaone 0\n",km.predict([frequency_vector_scld[0]]),"with percentage of like: ",retrievd_percentage[0])
    print("\nciaone 1\n",km.predict([frequency_vector_scld[1]]),"with percentage of like: ",retrievd_percentage[1])
    print("\nciaone 2\n",km.predict([frequency_vector_scld[2]]),"with percentage of like: ",retrievd_percentage[2])
    print("ciaone 3\n",km.predict([frequency_vector_scld[3]]),"with percentage of like: ",retrievd_percentage[3])
    print("\nciaone 4\n",km.predict([frequency_vector_scld[4]]),"with percentage of like: ",retrievd_percentage[4])
    print("\nciaone -4\n",km.predict([frequency_vector_scld[-4]]),"with percentage of like: ",retrievd_percentage[-4])

    print("\nciaone -5\n",km.predict([frequency_vector_scld[-5]]),"with percentage of like: ",retrievd_percentage[-5])
    print("\nciaone -6\n",km.predict([frequency_vector_scld[-6]]),"with percentage of like: ",retrievd_percentage[-6])

    # print(km.cluster_centers_[0])
    # print(km.cluster_centers_[1])

    #print(km.cluster_centers_[2])
    #print(km.cluster_centers_[3])


    print("VALORE", retrievd_percentage[-1])
    dist1 = distance_from_centroid(frequency_vector_scld[0],km.cluster_centers_[0])
    dist2 = distance_from_centroid(frequency_vector_scld[0],km.cluster_centers_[1])
    dist3 = distance_from_centroid(frequency_vector_scld[1],km.cluster_centers_[0])
    dist4 = distance_from_centroid(frequency_vector_scld[1],km.cluster_centers_[1])
    dist5 = distance_from_centroid(frequency_vector_scld[2],km.cluster_centers_[0])
    dist6 = distance_from_centroid(frequency_vector_scld[2],km.cluster_centers_[1])
    dist7 = distance_from_centroid(frequency_vector_scld[3],km.cluster_centers_[0])
    dist8 = distance_from_centroid(frequency_vector_scld[3],km.cluster_centers_[1])
    dist9 = distance_from_centroid(frequency_vector_scld[4],km.cluster_centers_[0])
    dist10 = distance_from_centroid(frequency_vector_scld[4],km.cluster_centers_[1])
    dist11 = distance_from_centroid(frequency_vector_scld[-5],km.cluster_centers_[0])
    dist12 = distance_from_centroid(frequency_vector_scld[-5],km.cluster_centers_[1])
    dist13 = distance_from_centroid(frequency_vector_scld[-6],km.cluster_centers_[0])
    dist14 = distance_from_centroid(frequency_vector_scld[-6],km.cluster_centers_[1])
    #dist3 = distance_from_centroid(frequency_vector_scld[-1],km.cluster_centers_[2])



    print("\ndistanza: ",dist1,"_",dist2)
    print("\ndistanza: ",dist3,"_",dist4)
    print("\ndistanza: ",dist5,"_",dist6)
    print("\ndistanza: ",dist7,"_",dist8)
    print("\ndistanza: ",dist9,"_",dist10)
    print("\ndistanza: ",dist10,"_",dist11)
    print("\ndistanza: ",dist12,"_",dist13)
    print("\ndistanza: ",dist14,"_",dist13)



    for i in range(km.n_clusters):
        c,ci,cz = 0,0,0

        percentage_cluster1,percentage_cluster2,percentage_cluster3 = 0,0,0
        for i in range(0,len(frequency_vector_scld)):
            prediction = km.predict([frequency_vector_scld[i]])

            perc = retrievd_percentage[i]
            if prediction == 0:
                c += 1
                #print("\n0 percentuale:",perc)
                percentage_cluster1 += float(perc)
            if prediction == 1:
                ci += 1
                percentage_cluster2 += float(perc)
                #print("\n1 percentuale:",perc)

            # if prediction == 2:
            #     cz += 1
            #     percentage_cluster3 += float(perc)
            #     #print("\n2 percentuale:",perc)
            
    if c != 0 and ci != 0 :#and cz != 0:

        percentage_cluster1 = percentage_cluster1/c
        percentage_cluster2 = percentage_cluster2/ci
        #percentage_cluster3 = percentage_cluster3/cz
        #percentage_cluster4 = percentage_cluster4/cz

        # percentage_cluster1 = percentage_cluster1/(percentage_cluster1+percentage_cluster2+percentage_cluster3)
        # percentage_cluster2 = percentage_cluster2/(percentage_cluster1+percentage_cluster2+percentage_cluster3)
        # percentage_cluster3 = percentage_cluster3/(percentage_cluster1+percentage_cluster2+percentage_cluster3)

    print("number of query per claster in user history: ",c,"__",ci)
    print("with liking percentage per cluster = ",percentage_cluster1,"__",percentage_cluster2)

    X = frequency_vector_scld
    y = km.labels_
    #y = [0,1,2]
    fig = plt.figure(1, figsize=(4, 3))
    plt.clf()

    ax = fig.add_subplot(111, projection="3d", elev=48, azim=134)
    ax.set_position([0, 0, 0.95, 1])


    plt.cla()
    pca = decomposition.PCA(n_components=2)
    pca.fit(X)
    X = pca.transform(X)

    for name, label in [("0", 0), ("1", 1)]:
        ax.text3D(
            X[y == label, 0].mean(),
            X[y == label, 1].mean(),
            name,
            horizontalalignment="center",
            bbox=dict(alpha=0.5, edgecolor="w", facecolor="w"),
        )
    # Reorder the labels to have colors matching the cluster results
    y = np.choose(y,[0,1]).astype(float)
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.nipy_spectral, edgecolor="k")

    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    #ax.zaxis.set_ticklabels([])

    plt.show()
    kmeans_kwargs = {
                "init": "random",
                "n_init": 10,
                "max_iter": 300,
                "random_state": 42,
            }
        
            # A list holds the SSE values for each k
    sse = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
        kmeans.fit(frequency_vector_scld)
        sse.append(kmeans.inertia_)

    plt.style.use("fivethirtyeight")
    plt.plot(range(1, 11), sse)
    plt.xticks(range(1, 11))
    plt.xlabel("Number of Clusters")
    plt.ylabel("SSE")
    plt.show()
