import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

graphs = []

#First Network
graph1 = nx.read_adjlist("SmallWorlds/data/cit-HepTh.txt")
graphs.append(graph1)

# average degree of neighbors
degree1, avg_neigh_degree1 = zip(*nx.average_degree_connectivity(graph1).items())

# convert to list
degree1 = list(degree1)
avg_neigh_degree1 = list(avg_neigh_degree1)


#plotting the graph
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1,1,figsize=(12,8))

sns.regplot(x=degree1,y=avg_neigh_degree1,ax=ax)

ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neigbhor degree")
ax.set_xlim(0,None)
plt.show()


#Second Network
graph2 = nx.read_adjlist("SmallWorlds/data/twitter_combined.txt")
graphs.append(graph2)

# average degree of neighbors
degree2, avg_neigh_degree2 = zip(*nx.average_degree_connectivity(graph2).items())

# convert to list
degree2 = list(degree2)
avg_neigh_degree2 = list(avg_neigh_degree2)


#plotting the graph
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1,1,figsize=(12,8))

sns.regplot(x=degree2,y=avg_neigh_degree2,ax=ax)

ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neigbhor degree")
ax.set_xlim(0,None)
plt.show()


#Third Network
graph3 = nx.read_adjlist("SmallWorlds/data/Wiki-Vote.txt")
graphs.append(graph3)

# average degree of neighbors
degree3, avg_neigh_degree3 = zip(*nx.average_degree_connectivity(graph3).items())

# convert to list
degree3 = list(degree3)
avg_neigh_degree3 = list(avg_neigh_degree3)


#plotting the graph
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1,1,figsize=(12,8))

sns.regplot(x=degree3,y=avg_neigh_degree3,ax=ax)

ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neigbhor degree")
ax.set_xlim(0,None)
plt.show()


#Forth Network
graph4 = nx.read_adjlist("SmallWorlds/data/email-Eu-core.txt")
graphs.append(graph4)

# average degree of neighbors
degree4, avg_neigh_degree4 = zip(*nx.average_degree_connectivity(graph4).items())

# convert to list
degree4 = list(degree4)
avg_neigh_degree4 = list(avg_neigh_degree4)


#plotting the graph
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1,1,figsize=(12,8))

sns.regplot(x=degree4,y=avg_neigh_degree4,ax=ax)

ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neigbhor degree")
ax.set_xlim(0,None)
plt.show()


#Fifth Network
graph5 = nx.read_adjlist("SmallWorlds/data/CA-GrQc.txt")
graphs.append(graph5)

# average degree of neighbors
degree5, avg_neigh_degree5 = zip(*nx.average_degree_connectivity(graph5).items())

# convert to list
degree5 = list(degree5)
avg_neigh_degree5 = list(avg_neigh_degree5)


#plotting the graph
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1,1,figsize=(12,8))

sns.regplot(x=degree5,y=avg_neigh_degree5,ax=ax)

ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neigbhor degree")
ax.set_xlim(0,None)
plt.show()
    
count = 1
for graph in graphs:
    print("Análise da rede {}".format(count))
    print("A rede tem {} vértices e {} arestas".format(graph.number_of_nodes(), graph.number_of_edges()))
    print("Degree Assortativity Coefficient: {}".format(nx.degree_assortativity_coefficient(graph)))
    print("Quantidade de componentes conectados: {}".format(nx.number_connected_components(graph)))
    print("Tamanho do componente gigante (GCC): {}".format(len(max(nx.connected_components(graph), key=len))))
    print("Coeficiente de clusturing avg_clustering(): {}".format(nx.average_clustering(graph)))
    print('\n')
    count += 1
    