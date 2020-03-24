#!/usr/bin/env python3
#cosine similarity in prev project
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# Get the data
path = 'movie_metadata.csv'
df = pd.read_csv(path)

#print(list(df))

column_names= ['movie_title','genres','director_name','content_rating','imdb_score','plot_keywords','actor_2_name','actor_1_name']

movie= df[column_names].copy()



movie=movie.drop('content_rating',axis=1)

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


# movie= movie.drop_duplicates(subset='movie_title', keep='first')
# #reseting of index other wise , previous index kept, then 0: 5043, some index are missing problem in 
# movie.reset_index(drop= True)


#add column index
count_row = movie.shape[0]
cc= [x for x in range(count_row)]
movie['index']=cc

#handle missing values
column_names= list(movie)
for c in column_names:
    movie[c]=movie[c].fillna('')

#spliting genres
def split_genre(row):
    s=''
    a= row['genres'].split('|')
    for k in a:
        s+= str(k)
        s+=' '
    return s
movie['genres']= movie.apply(split_genre,axis=1)

#combing all the fields
comb= 'combined'

def combining_funct(row):
    s=''
    for c in column_names:
       if c != 'content_rating' and c!= 'index' and c!= 'imdb_score' and c!='movie_title_2':
        s+=str(row[c])
        s+=' '
    return s

movie[comb]= movie.apply(combining_funct, axis=1)

## vectorisation
cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(movie[comb])

##cosine similarity
cosine_sim = cosine_similarity(count_matrix)


# movie.attributei.e. column name
def get_title_from_index(index):
    return movie[movie.index==index]['movie_title'].values[0]

def get_index_from_title(title):
   title= strip3(title)
   return movie[movie.movie_title_2 == title]['index'].values[0]

## findind movie
def is_movie_present(title):
   title= strip3(title)
   #if movie[movie.movie_title_2 == title].shape[0]>=1:  #also works! return matching rows
   if title in movie.movie_title_2.values: 
    return 1
   else :return 0

##stip the spaces and caps
def strip3(s): 
    s=s.lower()           
    a=""
    for i in s:
        if(i != ' '):
            a+=i
    return str(a)

"""
m='Avatar' 
no='Inside Out'
n='The Avengers'

#print(is_movie_present(m))

###########apply all#####################


movie_index = get_index_from_title(m)
#print(movie_index)
similar_movies = list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
i=0
print("Top 20 similar movies to",m, "are:\n")
for element in sorted_similar_movies:
    print(get_title_from_index(element[0]))
    i=i+1
    if i>20:
        break

##############till here####################
movie_index = get_index_from_title(no)
print(movie_index)
similar_movies = list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
i=0
print("Top 20 similar movies to",no, "are:\n")
for element in sorted_similar_movies:
    print(get_title_from_index(element[0]))
    i=i+1
    if i>20:
        break


movie_index = get_index_from_title(n)
print(movie_index)
similar_movies = list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
i=0
print("Top 20 similar movies to",n, "are:\n")
for element in sorted_similar_movies:
    print(get_title_from_index(element[0]))
    i=i+1
    if i>20:
        break
        
        
"""