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
        
        t = 0
        numberCommit = []
        while t < len(y):
            numberCommit.append(y[t]['"commit"'])
            t = t + 1
            
        print('Repo: ' + repository + 'Number of commits: ' + len(numberCommit))       
getUser(username)