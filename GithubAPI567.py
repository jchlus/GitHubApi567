# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:46:14 2019

@author: jchlu
"""

import requests
import json

username = input("What is your github user name: ")

def getUser(variable):
    
    url = requests.get("https://api.github.com/users/" + variable + "/repos")
    x = json.loads(url.text)

    i = 0
    repos = []
    while i < len(x):
        repos.append(x[i]['name'])
        i = i + 1
    
    for repository in repos:
        commits = requests.get("https://api.github.com/repos/" + variable + "/" + repository + "/commits")
        y = json.loads(commits.text)
        print('Repo: ' + repository + ' - Number of commits: ' + str(len(y)))       
getUser(username)


#Below I tested two of my friends githubs and they were all correct. I also tested (with print statements)
#The output of the requests.get (variable)
#The array of repos
#The requests.get (variable + repository)

#Test 1
#print(getUser("tommypinto"))
#$Output should be
#Repo: SchoolWork - Number of commits: 3

#Test 2
#print(getUser("tkautz12"))
#$Output should be
#Repo: Everything- - Number of commits: 15

#Test 3
#print(getUser("jchlus"))
#$Output should be
#Repo: Baseball-scouter - Number of commits: 6
#Repo: GitHubApi567 - Number of commits: 4
#Repo: SW-567 - Number of commits: 1
#Repo: Triangle567-Hw02 - Number of commits: 3
#Repo: Triangles - Number of commits: 2