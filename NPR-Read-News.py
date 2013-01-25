'''learned from codeacademy.com tutorial'''

from urllib2 import urlopen
from json import load


subject_ids = {'technology':1019, 'business':1006, 'economy':1017,
                'science':1007}

def get_api_key():
	'''(NoneType) -> str
	Retrieve API_KEY from another file
	'''
	f = open("API_KEY.txt")
	API_KEY = f.read()
	f.close()
	return API_KEY
	

def make_url():
	'''(NoneType) -> str
	Creates URL that will fetch news stories based 
	on user inputed data
	'''
	url_base = 'http://api.npr.org/query?apiKey='
	num_results_url = '&numResults=' + get_num_results()
	url_format = '&format=json'
	subject_id = '&id=' + get_subject()
	
	url = url_base + get_api_key() + num_results_url + url_format + subject_id
	
	return url
	

def get_num_results():
	'''(NoneType) -> str 
	Return number of results user wants to read
	'''
	
	num_results = raw_input("How many results would you like?\n")
	try:
		int(num_results)
	except ValueError:
		num_results = get_num_results()
	
	
	return str(num_results)

def get_subject():
	'''(NoneType) -> str 
	Return which subject the user wants to read about
	'''
	
	print "Please choose a subject:"
	for k,v in subject_ids.items():
		print k
		
	subject = raw_input("> ")
	if subject not in subject_ids.keys():
		subject = get_subject()
	
	
	return str(subject)
		
	                    
		
def print_results(url):
	'''(str) -> str
	Prints out the news stories
	'''

	#open our url, load the JSON
	response = urlopen(url)
	json_obj = load(response)
	
	
	for story in json_obj['list']['story']:
		print "TITLE: " + story['title']['$text'] + "\n"
		print "DATE: "	+ story['storyDate']['$text'] + "\n"
		
		
		
		#printing the story
		for paragraph in story['textWithHtml']['paragraph']:
			print paragraph['$text'] + " \n"
			
	
		
#running the program
print_results(make_url())