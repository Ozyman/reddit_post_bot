#!/usr/bin/python
import praw
import datetime

test = False

username = ""
password = ""
subreddit = "raisingKids"
dt = datetime.datetime.now() #+ datetime.timedelta(days=1)

ds = dt.strftime("%B %d, %Y")

title = "Good Times Tuesday(" + ds + ") Post a positive family experience you had recently."

#title += " Thanksgiving Edition"

r = praw.Reddit(user_agent="Used by /r/raisingKids to make 'weekly event' posts")
r.login(username,password)

# read lines from GNT file

f = open('/home/presto/raisingKids/GTT-body.txt','r')

body = f.read()
f.close()

# do post

if (test):
    print "TITLE:"+title + "\n\n"
    print "BODY:"+body + "\n\n"
else:
    r.submit(subreddit, title, body) 


