from flask import Flask, render_template

app = Flask(__name__)

temples = [
    {"name":"Somnath","location":"Veraval, Gujarat","img":"somnath.jpeg"},
    {"name":"Mallikarjuna","location":"Srisailam, AP","img":"mallikarjuna.jpeg"},
    {"name":"Mahakaleshwar","location":"Ujjain, MP","img":"mahakaleshwar.jpeg"},
    {"name":"Omkareshwar","location":"Mandhata, MP","img":"omkareshwar.jpeg"},
    {"name":"Kedarnath","location":"Kedarnath, UK","img":"kedarnath.jpeg"},
    {"name":"Bhimashankar","location":"Pune, MH","img":"bhimashankar.jpeg"},
    {"name":"Kashi Vishwanath","location":"Varanasi, UP","img":"kashivishwanath.jpeg"},
    {"name":"Trimbakeshwar","location":"Nashik, MH","img":"trimbakeshwar.jpeg"},
    {"name":"Vaidyanath","location":"Deoghar, JH","img":"vaidyanath.jpeg"},
    {"name":"Nageshwar","location":"Dwarka, Gujarat","img":"nageshwar.jpeg"},
    {"name":"Rameshwaram","location":"Rameswaram, TN","img":"rameshwaram.jpeg"},
    {"name":"Grishneshwar","location":"Ellora, MH","img":"grishneshwar.jpeg"}
]

@app.route('/')
def home():
    return render_template('index.html', temples=temples)

if __name__ == '__main__':
    app.run(debug=True)
