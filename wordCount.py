# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:53:45 2020

@author: joeyr
"""

#Reads the file and forms a list with the words
def fileReader(theFile):
    a_list = []
    with open(theFile, 'r') as f:
        for line in f:
            line = line.rstrip('\n').lower() #gets rid of '\n' and makes everything lowercase
            line = line.replace(',', '') #gets rid of commas
            line = line.replace(':', '') #gets rid of colons
            line = line.replace(';', '') #gets rid of semi-colons
            line = line.replace('.', '') #gets rid of periods
            line = line.replace('?', '') #gets rid of question marks
            a_list.append(line.split(' ')) #split and add each line to the list
            #a_list.append(line.rstrip('\n').lower().split(' '))
            
    return a_list


#returns a dictionary with the word and the number of times it appears
def wordCount(a_list):
    words = dict() #blank dictionary
    
    for i in range(len(a_list)):   #go through the list of words
        for j in range(len(a_list[i])):
                
            if(a_list[i][j] not in words): #if the word isn't in the dictionary
                words[a_list[i][j]] = 1 #set it's value to 1
                
            else:
                words[a_list[i][j]] = words[a_list[i][j]] + 1 #adds one everytime it sees a repeated word
                
    return words


#writes the file with dictionary
def writeFile(words, fileName): #words is the dictionary
    
    temp = list(words.keys()) #list of the dictionary keys
    with open(fileName, 'w') as file:
        for key in temp:
            line = key + ': ' + str(words[key]) + '\n' #create a string 'line'
            file.write(line)




a_list =  fileReader('declaration.txt')
numOfWords = wordCount(a_list)

print(len(numOfWords))

for key in list(numOfWords.keys()):
    print(key, ":", numOfWords[key])
    
writeFile(numOfWords, 'declarationKey1.txt')