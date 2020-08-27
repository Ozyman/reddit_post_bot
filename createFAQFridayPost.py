#!/usr/bin/python
import praw
import datetime

test = False

username = ""
password = ""
subreddit = "raisingKids"
dt = datetime.datetime.now() #+ datetime.timedelta(days=1)

ds = dt.strftime("%B %d, %Y")

r = praw.Reddit(user_agent="Used by /r/raisingKids to make 'weekly event' posts")
r.login(username,password)

# read next topic
ftFile = open('/home/presto/raisingKids/faq-topics.txt','r')
topic = ""
description = ""
therest = ""

for line in ftFile:
   if topic == "":
       topic = line
       if test:
          therest += line
   elif description == "":
       description = line
       if test:
          therest += line
   else:
       therest += line
ftFile.close()

# write faq file back without first two lines.
ftFile = open('/home/presto/raisingKids/faq-topics.txt','w')
ftFile.write(therest)
ftFile.close()

# read body
fbFile = open('/home/presto/raisingKids/faq-body.txt','r')
body = fbFile.read()
fbFile.close()

# merge topic/description into body
body = body.replace("%%TOPIC%%",topic)
body = body.replace("%%DESCRIPTION%%", description)

title = "FAQ Friday(" + ds + ") - " + topic

# do post

if test:
    print "TITLE:"+title + "\n\n"    
    print "BODY:"+body + "\n\n"
else:
   r.submit(subreddit, title, body)







   


