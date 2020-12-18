from flask import Flask,render_template,redirect,request,flash
import random
from flask import url_for

app = Flask(__name__)

site = {
    'name': 'resume'
}
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
	"skills": ["Python", "Flask", "Drawing", "HTML","Video editing ",  ],
	"projects": [
		{"name":"Tic-Tac-Toe", "description":"A description for the project.", "tags":["functions", "control structures", "game"]},
		{"name":"Battle of Teams", "description":"A description for the project.", "tags":["functions", "OOP"]},
		{"name":"Resume", "description":"A description for the project.", "tags":["flask", "web application", "HTTP routes"]}
	],
	"favourite_quotes": [
		{"quote":"“ Forge your heart into something strong.Unbreakable. ”", "author":"Rell"},
		{"quote":"“ only those you love can break your heart. ”", "author":"mor"},
		{"quote":"“ The darker the night, the brighter the stars. ”", "author":" malik"},
		{"quote":"“ Tomorrow is a hope never a promise. ”", "author":" malik"}
	],
	"favourite_songs":[
		{"song":"empty crown", "singer":"yas"},
		{"song": "demons","singer":"imagin dragons"},
		{"song":"unstoppable" , "singer":"sia"},
		{"song":"Bird Set Free","singer":"sia"},
		{"song":"هزيم الرعد", "singer":"spacetoon"}]
}


@app.route('/editq', methods=['POST','GET'])
def edit_quotes():
	if request.method == 'GET':
		return render_template('edit-quotes.html')
	else:
		# Read values from form
		quote=str(request.form['quote'])
		author=str(request.form['auther'])
		added_quote={'qoute':quote,'author':author}
		me['favourite_quotes'].append(added_quote)
		return redirect(url_for('display_quote'))

@app.route('/addsong', methods=['GET','POST'])
def edit_songs():
	if request.method == 'GET':
		return render_template('edit-songs.html')
	else:
		# Read values from form
		song=str(request.form['song'])
		singer=str(request.form['singer'])
		added_song={'song':song,'singer':singer}
		me['favourite_songs'].append(added_song)
		return redirect(url_for('disply_songs'))

@app.route('/')
def display_info():	
    name=me.get('first_name')+me.get('last_name')
    about=me.get('description')
    my_menu = [{"title":"ME", "url":url_for("myinfo")},
            {"title":"Skills", "url":url_for("display_skills")},
            {"title":"Quotes", "url":url_for("display_quote")},
            {"title":"projects", "url":url_for("display_projects")},
			{"title":"songs", "url":url_for("disply_songs")}
        ]
    return render_template("base.html", menu=my_menu)

@app.route('/me/')
def myinfo():
    name=me.get('first_name')+me.get('last_name')
    age=me.get('age')
    avatar=me.get('avatarURL')
    email=me.get("email")
    return render_template("me.html",avatar=avatar,name=name,age=age,email=email)

@app.route('/quotes/')
def display_quote():
	ran=random.randint(0,len(me.get('favourite_quotes')))
	my_quote=me.get("favourite_quotes")
	return render_template('quotes.html',quote=my_quote[ran])

@app.route('/skills/')
def display_skills():
	my_skills=me.get('skills')
	return render_template('skills.html',skills=my_skills)

@app.route('/songs/')
def disply_songs():
	songs=me.get('favourite_songs')
	return render_template('songs.html',songs=songs)
	
@app.route('/projects/')
def display_projects():
	my_projects=me.get("projects")
	return render_template('my-projects.html',project=my_projects)