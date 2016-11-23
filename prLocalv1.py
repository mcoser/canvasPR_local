# GET details for a course from the Canvas API
import os
import csv
import requests
import webbrowser

import time
import json
import operator

TOKEN = 'TOKEN'
# add an access token here

print 
courseNum = input("Enter Canvas Course Number: ")
print 
# 5774
print "Gathering Data..."

# loop over all of the courses in the course list
users_url = 'https://your.canvas.domain/api/v1/courses/%s' % courseNum +'/users?per_page=500'


# call the API and raise exceptions as needed
headers = {
    'Authorization': 'Bearer {}'.format(TOKEN),
}


# user data
try: 
    print users_url
    userResp = requests.get(users_url, headers=headers)
    #print userResp
    userResp.raise_for_status()
except requests.exceptions.RequestException as e:
    print e
    raise

print "__________________________________________________________________________________"
print

# save json response as a list of objects
api_userResponse = userResp.json
#print api_userResponse



#for each student user in the course, get their user_id
userID = []
for d in api_userResponse:
    userIdSingle = d['id']
    userID.append(userIdSingle)


#print userID

profileFull = []

# profile data
for i in userID:
    enroll_url = 'https://your.canvas.domain/api/v1/users/%s' % i +'/profile?per_page=500'
    try: 
        profileResp = requests.get(enroll_url, headers=headers)
        #print profileResp.json
        print "User " + str(i) + " - success..."
        profileFull.append(profileResp.json)
        profileResp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print enroll_url
        raise


# Writing the information from data to a CSV file
'''
with open('course_settings.csv', 'wb') as f:
    writer = csv.writer(f)
    #writer.writerow(['course_id'])
    writer.writerows(data)
    '''
with open('prData.js', 'w') as outfile:
    outfile.write('var prData = ')
    json.dump(profileFull, outfile)

print
print
print "DONE! Data File Complete."
print
print "Please stand by..."
print
print
time.sleep(3) 

webbrowser.open('html file')
