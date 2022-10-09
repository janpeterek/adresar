from flask import Flask, request, render_template
from form import Form, BooleanField, StringField, validators

app = Flask(__name__)

class ZadaniJmena(Form):
    jmeno = StringField('Jmeno', [validators.Length(min=1, max=30)])
    prijmeni = StringField('Prijmeni', [validators.Length(min=1, max=30)])

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/name', methods=['GET', 'POST'])
def task():
    form = ZadaniJmena(request.form)
    if form.validate():
       return render_template()
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run()
