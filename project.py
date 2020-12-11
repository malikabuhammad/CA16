from flask import Flask,render_template
import random
from flask import url_for

me = {
	"first_name":"Malik",
	"last_name":"Abuhammad",
	"description": " Computer Science graduate.",
	"social_links": [
			{"site":"linked in","url":"https://www.linkedin.com/in/malik-abuhammad-59414b1b5"}, 
			{"site": "GitHub", "url": "https://github.com/malikabuhammad"}
	],
	"age": 21,
	"avatarURL": "https://web.facebook.com/photo?fbid=1577552849062328&set=a.104626909688270",
	"email": "malik.shaher16@email.com",
	"skills": ["Python", "Flask", "JavaScript", "HTML","Video editing ",  ],
	"projects": [
		{"name":"Tic-Tac-Toe", "description":"A description for the project.", "tags":["functions", "control structures", "game"]},
		{"name":"Battle of Teams", "description":"A description for the project.", "tags":["functions", "OOP"]},
		{"name":"Resume", "description":"A description for the project.", "tags":["flask", "web application", "HTTP routes"]}
	],
	"favourite_quotes": [
		{"quote":"“Forge your heart into something strong. Unbreakable.”", "author":"Rell"},
		{"quote":"only those you love can break your heart .", "author":"Alan Watts"},
		{"quote":"The darker the night, the brighter the stars.", "author":"Albert Einstein"}
	],
	"favourite_songs":[
		{"song":"empty crown", "singer ":"yas"},
		{"song": "demons","singer":"imagin dragons"},
		{"song":"unstoppable" , "singer":"sia"}	]
}
@app.route('/')
def display_info():
    name=me.get('first_name')+me.get('last_name')
    about=me.get('description')
    menu=['ME','skills','Projects','Quote of the Day']
    return render_template("index.html" , name=name,description=about,menu=menu)


@app.route('/me/')
def myinfo():
    name=me.get('first_name')+me.get('last_name')
    age=me.get('age')
    avatar=me.get('avatarURL')
    email=me.get("email")
    return render_template("me.html",avatar=avatar,name=name,age=age,email=email)

@app.route('/quotes/')
def display_quote():
	ran=random.randint(1,3)
	my_quote=me.get("favourite_quotes")
	return render_template('quotes.html',quote=my_quote[ran])

@app.route('/skills/')
def display_skills():
	my_skills=me.get('skills')
	return render_template('skills.html',skill=my_skills)

# @app.route('/songs/')
# def disply_songs():
#     songs=me.get('songs')
# 	return render_template('songs.html')


def disply_projects():
	my_projects=me.get('projects')
	return render_template('projects.html')