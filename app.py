from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def demo():
     if request.method == 'POST':
          name = request.form['name']
          marks = request.form['marks']
          branch = request.form['branch']
          place = request.form['place']
          print(name,marks,branch,place)
     return render_template('index.html')

@app.route('/ram/<int:a>/<int:b>')
def pam(a,b):
     return f'multiple{a},{b} is: {a*b}'

@app.route('/sita/<string:a>/<string:b>',methods=['GET'])
def sit(a,b):
     return f'{a} is one of my friend {b}'
app.run(use_reloader=True,debug=True)


