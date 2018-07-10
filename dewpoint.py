import urllib2
import json
from flask import Flask, render_template,request, jsonify
from flask_bootstrap import Bootstrap
from decimal import Decimal


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/form', methods=['GET', 'POST'])
def form():

  if request.method == 'POST': 
	zipcode = request.form.get('zip')
  else:
	zipcode = '11230'

  f = urllib2.urlopen('https://api.wunderground.com/api/d5b402928887a79d/forecast/geolookup/conditions/q/'+zipcode+'/format.json')
  json_string = f.read()
  
  resp = json.loads(json_string)

  f.close()

  bad_hair_cat = 'http://img06.deviantart.net/2c2a/i/2013/236/5/5/doodle_237___persian_cat_by_giovannag-d6jlpei.jpg';
  good_hair_cat = 'http://i.imgur.com/ZiEBSak.jpg?1';

  image_size = '200';

  location = resp['location']['city'];
  temp_f = resp['current_observation']['temp_f'];
  dewpoint = resp['current_observation']['dewpoint_string'];
  dewpoint_f = resp['current_observation']['dewpoint_f'];
  humidity = resp['current_observation']['relative_humidity'];
  icon_url = resp['current_observation']['icon_url'];

  if dewpoint_f > 65:
    image = bad_hair_cat
    desc  = "Bad hair day! Run!"
    color = "red"

  else:
    image = good_hair_cat
    desc = "Good hair day, good kitty!"
    color = "green"

  return render_template('index.html', msg=1, zipcode=zipcode, desc=desc, color=color, image=image,temp_f=temp_f,dewpoint=dewpoint,dewpoint_f=dewpoint_f, humidity=humidity,icon_url=icon_url, image_size=image_size)
  #return json.dumps(parsed_json)
  

# @app.route('/form', methods=['GET', 'POST']) #allow both GET and POST requests
# def form():
#     if request.method == 'POST': #this block is only entered when the form is submitted
#         zip = request.form.get('zip')

#   	myweather = weather()

# 	return render_template('index.html', msg=myweather)




if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000: