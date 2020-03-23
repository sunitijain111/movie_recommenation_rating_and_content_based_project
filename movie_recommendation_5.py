#!/usr/bin/env python3
import sys
import movie_recommendation_3 as content
import movie_recommendation_4 as rating
print("Enter movie name : ")
x= input()
x.strip()

# a=""
# for i in range(len(x)):
#     if i==0:
#         a+=x[i].upper()
#     elif i and x[i-1]==' ':
#         a+=x[i].upper()
#     else:
#         a+=x[i]
# #print("entered movie : "+ a)

# x=a

if not content.is_movie_present(x):
    print("the movie "+ x+" doesn't exisits in our database")
    sys.exit()
    
movie_index = content.get_index_from_title(x)
#print(movie_index)
similar_movies = list(enumerate(content.cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
sorted_similar_movies=sorted_similar_movies[0:40]
content_result=[]
for element in sorted_similar_movies:
     content_result.append(content.get_title_from_index(element[0]))
     
     
neighbors = rating.getNeighbors(movie_index, 400) 

highly=[]
for name in neighbors:
    if name in content_result:
        highly.append(name)

if(len(name)): print("\n\n HIGHLY RECOMMENDED MOVIES ARE ")
for name in highly:
    neighbors.remove(name)
    content_result.remove(name)
    print(name)    

print("\n\n  CONTENT BASED RECOMMENDED MOVIES ARE")
for name in content_result[0:10]:
    print(name)

print("\n\n  OTHER RECOMMENDED MOVIES ARE")
for name in neighbors[0:10]:
    print(name)

# for neighbor in neighbors:
#     print (neighbor)

#i=0
# print("Top 20 similar movies to",x, "are:\n")
# for element in sorted_similar_movies:
#     print(content.get_title_from_index(element[0]))
#     i=i+1
#     if i>20:
#         break
