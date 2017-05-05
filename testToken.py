import requests
from bs4 import BeautifulSoup
import json


def checkConnec():
	link = "http://www.supremenewyork.com"
	link = "https://www.google.com"
	# link = "http://52.5.38.234"

	# r = requests.get(link)
	# print(r.status_code)


	r = requests.get(link, headers={'host': 'www.supremenewyork.com'})
	print(r.status_code)


	# r = requests.get('https://google.com/', headers={'host': 'example.com'})
	# print(r.status_code)
def loadToken():
	tokens = []
	with open("tokens.json","r") as infile:
		tokens = json.load(infile)

	if len(tokens) != 0:
		print(len(tokens))
		token = tokens[0]
		tokens.pop(0)
	else:
		print("No tokens solved!")
		exit()
	with open("tokens.json","w") as outfile:
		json.dump(tokens,outfile)

	return token

def submitData():
	form_data = {"g-recaptcha-response": loadToken()}
	link = "https://www.google.com/recaptcha/api2/demo"
	r = requests.post(link, headers={'host': 'www.google.com'}, data=form_data)
	print("Satus: "+ str(r.status_code) + "\n")

	soup = BeautifulSoup(r.text,"html.parser")

	if soup.find("div",{"class":"recaptcha-success"}) == None:
		print("Invalid key!")
	else:
		print("Captcha solved!")


def main():
	submitData()

if __name__ == '__main__':
	main()
