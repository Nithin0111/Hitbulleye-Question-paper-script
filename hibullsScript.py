f = open("questions.txt", "r")
x1 = f.read()
print(x1)


#Accessing a text file - www.101computing.net/mp3-playlist/

file = open("questions.txt","r")
questions = []
#Repeat for each question in the text file
for line in file:
  #Let's split the line into an array called "fields" using the ";" as a separator:
  fields = line.split(".")
  #and let's extract the data:
  serialNumber = fields[0]
  question = fields[1]
  #append questions to the questions array that we have created
  questions.append(question)
#It is good practice to close the file at the end to free up resources   
file.close()
print(len(questions))#length of the questions array
#dividing questions one by one to search independedntly
for i in range(len(questions)):
    print(questions[i])

from googlesearch import *
import webbrowser
#to search, will ask search query at the time of execution
# for i in range(len(questions)):
query = questions
#iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
#chrome_path = r'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
for i in range(len(questions)):
    query = questions[i]
    for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
        webbrowser.open("https://google.com/search?q=%s" % query)
