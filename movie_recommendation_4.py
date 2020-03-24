import pandas as pd
import operator as op
# Get the data 
column_names=['movie_title','imdb_score']
path = 'movie_metadata.csv'
df = pd.read_csv(path)
movie= df[column_names].copy()

#add column index
count_row = movie.shape[0] 
cc= [x for x in range(count_row)]
movie['index']=cc

def strip(row):
    s= row['movie_title']   
    s=s.replace(u'\xa0',u' ')  # removing encoding
    while( len(s)>1 and s[-1] ==' '):
        s= s[0:-1]
    return str(s)
movie['movie_title']= movie.apply(strip,axis=1)

#remove all spaces, caps from names so that the avengers is same as THE avengers etc.
def strip2(row):
    s= row['movie_title']  
    s=s.lower()           
    a=""
    for i in s:
        if(i != ' '):
            a+=i
    return str(a)
#print(strip2("Suniti Jain 99 2"))
movie['movie_title_2']= movie.apply(strip2,axis=1)


#handle missing values
column_names= list(movie)
for c in column_names:
  movie[c]=movie[c].fillna('')
########print(movie.iloc[0][1])  
  
"""  
#handle missing values
column_names= list(movie)
for c in column_names:
  movie[c]=movie[c].fillna('')    
"""
##stip the spaces and caps
def strip3(s): 
    s=s.lower()           
    a=""
    for i in s:
        if(i != ' '):
            a+=i
    return str(a)

# movie.attributei.e. column name
def get_title_from_index(index):
    return movie[movie.index==index]['movie_title'].values[0]

def get_index_from_title(title):
   title= strip3(title) 
   return movie[movie.movie_title == title]['index'].values[0]

#computing distance between two movies
def ComputeDistance(a, b):
    knndist = abs(a-b)
    return  knndist    
    
#fetching k neighbours
def getNeighbors(movieID, K):
    distances = []
    for id in movie.index.values:
        if (id != movieID):
            dist = ComputeDistance(movie.iloc[movieID][1], movie.iloc[id][1])
            distances.append((id, dist))
    distances.sort(key=lambda elem: elem[1])
    neighbors = []
    for x in range(K):
        neighbors.append(movie.iloc[distances[x][0]][0])
    return neighbors

# K = 10   
# m= 'The Avengers'
# index= get_index_from_title(m)
# #print(index)
# neighbors = getNeighbors(index, K) 
# for neighbor in neighbors:
#     print (neighbor ) #+" "+str(movie.iloc[neighbor][1]))
  