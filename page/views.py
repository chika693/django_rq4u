from multiprocessing import context
from django.shortcuts import render
import requests
from datetime import datetime
from .forms import user_name_form

# ## function that gets the random quote
# def get_random_quote():
# 	try:
# 		## making the get request
# 		response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
# 		if response.status_code == 200:
# 			## extracting the core data
# 			json_data = response.json()
# 			data = json_data['data']

# 			## getting the quote from the data
# 			print(data[0]['quoteText'])
# 		else:
# 			print("Error while getting quote")
# 	except:
# 		print("Something went wrong! Try Again!")

# Using datetime
now = datetime.now()
year = now.year


## making the get request
response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
if response.status_code == 200:
	## extracting the core data
	json_data = response.json()
	data = json_data['data']

	## getting the quote from the data
get_quote = data[0]['quoteText']

context = {
		'year': year,
		'quote': get_quote,
		}
# Create your views here.
def home(request):
	submitted = False
	if request.method == 'POST':
		form = user_name_form(request.POST)
		if form.is_valid():
			form.save()
	return render(request, 'page/home.html', context)

