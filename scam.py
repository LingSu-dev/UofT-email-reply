import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://app.engagebay.com/jsapi/rest/add-subscriber?'

names = json.loads(open('name.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))
	username = name.lower() + name_extra + '@mail.utoronto.ca'
	password = ''.join(random.choice(chars) for i in range(8))
	owner_id = int(''.join(random.choice(string.digits) for i in range(16)))
	visitor_id = int(''.join(random.choice(string.digits) for i in range(16)))
	source_id = int(''.join(random.choice(string.digits) for i in range(16)))
	page_url = 'https://loginwy.engagebay.com/embed-forms/' + str(source_id)
	lettersAndDigits = string.ascii_letters + string.digits
	lettersAndDigits = ''.join((random.choice(lettersAndDigits) for i in range(26)))
	session_token = "%s-%s-%s-%s-%s" % (lettersAndDigits[0:7], lettersAndDigits[0:3], lettersAndDigits[4:7], lettersAndDigits[8:11], lettersAndDigits[0:11])
	requests.post(url, allow_redirects=False, data={
		'owner_id': owner_id,
		'formData': {
			"email":username,
			"addAsTags":[],
			"addAsNotes":[],
			"wsdfb":name.lower(),
			"effef":password
		},
		'formFieldOrderKeys': ["email","wsdfb","effef"],
		'visitor_id': visitor_id,
		'our_user': 'null',
		'visitorStatus': 'NEW',
		'source_type': 'FORM',
		'source_id': source_id,
		'referrer': '(none)',
		'page_url': page_url,
		'browser_info': {"browser":"Chrome","version":"81.0.4044.138","mobile":'false',"os":"Windows","osversion":"10"},
		'trafficType': 'typein',
		'utm_campaign': '(none)',
		'utm_source': '(direct)',
		'utm_medium': '(none)',
		'utm_content': '(none)',
		'utm_term': '(none)',
		'entry_point': page_url,
		'pages_visit_count': '1',
		'ehub_email': username,
		'session_token': session_token,
		'apiKey': lettersAndDigits
	})
	print(username, password)
	#print 'sending username %s and password %s' % (username, password)
