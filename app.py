from flask import Flask
app = Flask(__name__)


def home():
	return render_template()

app.run(debug = True)