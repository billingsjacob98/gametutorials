from django.shortcuts import render
from tutorials.models import Game
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.core.files.base import ContentFile
from io import StringIO
from datetime import datetime

def home(request):
	return render(request, 'base.html')

def games(request):
	games = Game.objects.all()
	context = {'games': games}
	return render(request, 'games.html', context)

def detail(request, game_id):
	game = Game.objects.get(pk=game_id)
	context = {'game': game}
	return render(request, 'game.html', context)

def get_game_image(game_url):
	r = requests.get('http://en.wikipedia.org' + game_url)
	raw = r.content
	soup = BeautifulSoup(str(raw))
	image = soup.find_all('img')[0]
	src = image['src']
	image_data = requests.get('http:' + src, stream=True)
	binary_image_data = image_data.content
	return binary_image_data

def get_games(request):
	WIKIPEDIA_URL = 'http://en.wikipedia.org/wiki/List_of_Xbox_One_games'
	r = requests.get(WIKIPEDIA_URL)
	raw = r.content
	soup = BeautifulSoup(str(raw))
	table = soup.find_all('table', attrs={'class', 'wikitable'})

	# there should be only one table on the page
	for item in table:
		t = item
		rows = t.find_all('tr')
		# TODO - FINISH THIS - CURRENTLY JUST GETTING ROW 3 (THIRD GAME IN THE LIST)
		print(rows)
		rows = rows[3]
		print(rows)
		for i, row in enumerate(rows):
			if i > 0:
				name = row.find_all('a')[0].text
				game_url = row.find_all('a')[0]['href']
				if game_url.startswith('/wiki'):
					game_image = get_game_image(game_url)
				import pdb;pdb.set_trace()
				release_date = row.find_all('td')[7]
				try:
					publisher = row.find_all('td')[3].find_all('a')[0].text
				except IndexError:
					publsher = None
				unreleased = False
				try:
					release_date = release_date.find_all('span')[1].text
					# Convert release date to a Python datetime
					try:
						release_date = datetime.strptime(release_date, "%B %d, %Y")
					except ValueError:
						# Guess we don't have the day (just month and year e.g. December 2014)
						# don't save in the database...
						continue
				except IndexError:
					# The game must not have a release date yet (either TBA or e.g. 2015)
					unreleased = True
					release_date = release_date.text
				# Only try to create the game in the database if it has been released
				if not unreleased:
					image_field = ContentFile(game_image)
					game, created = Game.objects.get_or_create(name=name, release_date=release_date, 
						publisher=publisher, front_cover=image_field)
	return HttpResponse('OK')

