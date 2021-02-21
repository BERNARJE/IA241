...
#Lab 6
...

#3.1

for i in range(6):
    if i !=3:
        print(i)
        
#3.2

result = 1

for i in range(1,6):
    result = result * i
    
print(result)

#3.3 

result = 0

for i in range(1,6):
    result = result + i
    
print(result)

#3.4 

result = 1

for i in range(3,9):
    result = result * i
    
print(result)

#3.5

result = 1

for i in range(4,9):
    result = result * i
    
print(result)

#3.6

result = 0
for word in 'this is my 6th string'.split():
    #print(word)
    result = result +1
    
print(result)

#3.7

my_tweet = {
    "favorite_count":1138,
    "lang": "en",
    "coordinates": (-75, 40),
    "entities": {"hashtags": ["Preds", "Pens", "SingIntoSpring"]}
    }

# print(my_tweet['entities']['hashtags'])

result = 0 

for hashtag in my_tweet['entities']['hashtags']:
    result = result +1
print(result)