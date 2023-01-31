import csv
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler 
from sklearn import decomposition
from sklearn import datasets
from sklearn.cluster import KMeans
from statistics import mean

import tarfile
import urllib

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

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
            for k in range(0,len(relational_table)):
                if (" "+relational_table[k][1]) == query_spl[1]:
                        post_id_of_cc.append(relational_table[k][0])

        if query_spl[0] != "content_creator_ID ":
            for k in range(0,len(relational_table[0])):
                if(query_spl[0] == (relational_table[0][k]+" ")):
                    ind.append((k,query_spl[1]))
    for i in range(len(relational_table)):
        c=0
        if len(post_id_of_cc) > 0:
            if relational_table[i][0] in post_id_of_cc:
                for indx,val in ind:
                    if(" "+relational_table[i][indx] == (val)):
                        c += 1
                        if(c == len(ind)):
                            query_result.append(relational_table[i])
        else:
            for indx,val in ind:
                if(" "+relational_table[i][indx] == (val)):
                    c += 1
                    if(c == len(ind)):
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
    retrievd_percentage_true = []
    for i in range(0,len(query_log_user)):
        retrieved_query = retriev_query(query_log_user[i][0])
        retrievd_percentage.append(query_log_user[i][1])
        query_result = retrieve_batch(retrieved_query,query_set)
        list_tot.append(query_result)
        if len(query_result) != 0:
            list.append(query_result)
            frequency_vector.append(sum_vector(query_result))
            retrievd_percentage_true.append(query_log_user[i][1])
        if(len(query_result) == 0): 
            empty_result.append(1)
    return frequency_vector, retrievd_percentage_true
   


def sum_vector(batch_of_post):
    encoded_vector = []
    for j in range(2,len(batch_of_post[0])):
        tmp = 0
        for i in range(0,len(batch_of_post)):
            tmp += int(batch_of_post[i][j])
        encoded_vector.append(tmp) 
    return encoded_vector




def testing(freq_vec_train,freq_vect_test,labels_train,labels_test,pipe):
    res = 0
    nearest_list = []
    loss = []
    for i in range(0,len(freq_vect_test)):
        dis = []
        res = pipe.predict([freq_vect_test[i]])
        for indx,j in enumerate(pipe["clusterer"]["kmeans"].labels_):
                if (j != res):
                    dis.append( (indx,distance_from_centroid(np.array(freq_vect_test[i]), np.array(freq_vec_train[indx]))) )

        dis = sorted(dis,key=lambda x:x[1])
        nearest_list.append((i,dis[0]))

    for k1,k2 in nearest_list:
        ltrain = labels_train[k2[0]]
        ltest = labels_test[k1]
        mse = (np.square(float(ltrain) - float(ltest))).mean(axis=None)
        loss.append(mse)
    return loss








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
    query_log_user = list(all_data["user_0158"])

    frequency_list, retrievd_percentage = get_frequency_list(query_log_user)

    print(len(frequency_list),len(retrievd_percentage))
   
    








    frequency_list_train, frequency_list_test, labels, labels_test = train_test_split(frequency_list, retrievd_percentage, test_size=0.20, random_state=42)


    n_clusters = 2
    
    preprocessor = Pipeline(
        [
            ("scaler", MinMaxScaler()),
            ("pca", PCA(n_components=128, random_state=42)),
        ]
    )
    clusterer = Pipeline(
        [
            (
                "kmeans",
                KMeans(
                    n_clusters=n_clusters,
                    init="k-means++",
                    n_init=50,
                    max_iter=500,
                    random_state=42,
                ),
            ),
        ]
    )
    pipe = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("clusterer", clusterer)
        ]
    )

    pipe.fit(frequency_list_train)
    preprocessed_data = pipe["preprocessor"].transform(frequency_list_train)
    predicted_labels = pipe["clusterer"]["kmeans"].labels_



    perdita = testing(frequency_list_train, frequency_list_test, labels, labels_test, pipe)
    print("LOSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS\n", perdita)
    print(len(perdita))
    print(mean(perdita))



    # X = frequency_vector_scld
    # y = km.labels_
    # #y = [0,1,2]
    # fig = plt.figure(1, figsize=(4, 3))
    # plt.clf()

    # ax = fig.add_subplot(111, projection="3d", elev=48, azim=134)
    # ax.set_position([0, 0, 0.95, 1])


    # plt.cla()
    # pca = decomposition.PCA(n_components=2)
    # pca.fit(X)
    # X = pca.transform(X)

    # for name, label in [("0", 0), ("1", 1)]:
    #     ax.text3D(
    #         X[y == label, 0].mean(),
    #         X[y == label, 1].mean(),
    #         name,
    #         horizontalalignment="center",
    #         bbox=dict(alpha=0.5, edgecolor="w", facecolor="w"),
    #     )
    # # Reorder the labels to have colors matching the cluster results
    # y = np.choose(y,[0,1]).astype(float)
    # ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.nipy_spectral, edgecolor="k")

    # ax.xaxis.set_ticklabels([])
    # ax.yaxis.set_ticklabels([])
    # #ax.zaxis.set_ticklabels([])

    # plt.show()
    # kmeans_kwargs = {
    #             "init": "random",
    #             "n_init": 10,
    #             "max_iter": 300,
    #             "random_state": 42,
    #         }
        
    #         # A list holds the SSE values for each k
    # sse = []
    # for k in range(1, 11):
    #     kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    #     kmeans.fit(frequency_vector_scld)
    #     sse.append(kmeans.inertia_)

    # plt.style.use("fivethirtyeight")
    # plt.plot(range(1, 11), sse)
    # plt.xticks(range(1, 11))
    # plt.xlabel("Number of Clusters")
    # plt.ylabel("SSE")
    # plt.show()
