#!/usr/bin/env python3

import sys
import socket
import string
import sys
import datetime
import requests
import subprocess
import os
import shutil
import uuid
import json
import time
from time import strftime
from pathlib import Path

target = sys.argv[1]
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
url = 'https://localhost:9200/'+target+'-subdomain/_search'
auth=('admin', '39fd950e-873f-11ee-913a-470ee3d36827')
list_subs = []

def consulta_subdomain():
	data = {"size":10000}
	get_doc = requests.get(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
	parse_scan = json.loads(get_doc.text)
	for x in parse_scan['hits']['hits']:
		if(x['_source']['server.domain'] not in list_subs):
			list_subs.append(x['_source']['server.domain'])
	print(list_subs)
		
	
def main():
	consulta_subdomain()
if __name__ == '__main__':
	main()
