from flask import Flask,render_template
app = Flask(__name__)

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
		{"quote":"The more a thing tends to be permanent, the more it tends to be lifeless.", "author":"Alan Watts"},
		{"quote":"Logic will get you from A to Z; imagination will get you everywhere.", "author":"Albert Einstein"}
	]
    

}
@app.route('/')
def display_info():
    name=me.get('first_name')+me.get('last_name')
    about=me.get('description')
    menu=['ME','skills','Projects','Quote of the Day']
    return render_template("index.html" , name=name,description=about,menu=menu)


@app.route('/me')
def myinfo():
    age=me.get('age')
    avatar=me.get('avatarURL')
    email=me.get("email")
    return render_template("me.html")