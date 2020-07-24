from flask import Flask,render_template,request
from flask_mail import Mail
import datetime
import requests
app = Flask(__name__)
#mail functionality
app.config.update(

    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PORT = "465",
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "jilvinthomas@gmail.com",
    MAIL_PASSWORD = "Your Password"

)
mail = Mail(app)

@app.route("/")
@app.route("/index",methods = ["GET","POST"])
def index():
    API_KEY = '90ea70a0851bb9882192c0e7845b167c'
    location = "Kerala"
    if(request.method=="POST"):
        location = request.form.get("location")

    if(location=="" or location==None):
        location = "Kerala"

    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={API_KEY}'
    response = requests.get(url).json()
    current_temperature = response.get('main', {}).get('temp')
    current_temperature = int(round(current_temperature -273.15,2))
    wind_speed = response.get('wind', {}).get('speed')
    humidity = response.get('main', {}).get('humidity')
    icon = response["weather"][0]["icon"]

    params = {
                "ct":current_temperature,
                "city_name":location.upper(),
                "ws":wind_speed,
                "humid":humidity,
                "icon_sym":str(icon)

             }

    return render_template("index.html",param = params)

@app.route("/contact",methods=["GET","POST"])
def contact():

    if(request.method=="POST"):

        name = request.form.get("name")
        phone = request.form.get("PhoneNumber")
        email = request.form.get("email")
        message = request.form.get("message")

        #sending mail to the admin
        mail.send_message('New message from'+name,

                          sender = email,
                          recipients= ["jilvinthomas@gmail.com"],
                          body= message+"Phone NUmber is"+phone

                          )

    return render_template("contact.html")

app.run(debug = True)
