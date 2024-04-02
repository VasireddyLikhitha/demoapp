from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

'''@app.route('/kala/<int:a>')
def kal(a):
    return redirect(url_for('demo',a=a))
@app.route('/<a>')
def demo(a):
    return f'{a} This is redirected page'''


@app.route('/ram/')
def rama():
    return redirect(url_for('demo1'))
@app.route('/redirected-page')
def demo1():
    return render_template('direct.html')
app.run(use_reloader=True,debug=True)

