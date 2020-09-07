import json 
 
f = open('twitter.json')  # open a json file in read mode open() return a file object

twitterData = json.load(f)  # json.load() takes a file object and return the json

info = twitterData['info'];

def getDegreeOfProfanity(words): # this function will return the degree of profanity in a given list of words
    return sum(1 for word in words if word.lower() in profane) / len(words)

profane = [
    'head',
    'tail',
    'compiling',
    'playlist'
] # this array will store all the profane words

report = [] #this array will store the result(degree of profanity) related to a particular tweet 

for userInfo in info:
    listOfWords = userInfo['tweet'].split(' ')
    res = {
        'id': userInfo['id'],
        'degreeOfProfanity': getDegreeOfProfanity(listOfWords)
    }
    report.append(res)

