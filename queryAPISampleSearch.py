#!/usr/bin/env python


import requests
import json
import csv
import time


baseURL = 'okapi_url'

headers = {
	'x-okapi-tenant': "mytenant",
	'x-okapi-token': "mytoken"
	}

timestr = time.strftime("%Y%m%d-%H%M%S")

# see https://wiki.folio.org/display/FOLIOtips/MARC+Search+Query+API for syntax of search
# even though this is a post you aren't really creating a record, just sending the search request

mySearch = {
"fieldsSearchExpression": "035.a ^= '(CULAspace)'"
}
marcSearch = requests.post(baseURL + '/source-storage/stream/marc-record-identifiers', headers=headers, json=mySearch).json()

#write time stamped csv of instances so you don't accidentally overwrite your last search
#this csv should be data export ready

f = csv.writer(open("instanceSearchResults-"+ time.strftime("%Y%m%d-%H%M%S") + ".csv", "w", newline=''))
for result in marcSearch["records"]:
	f.writerow([result])

			
