from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def demo():
    if request.method == 'POST':
        #print(request.form)
        SEext = int(request.form['se'])
        CNext = int(request.form['cn'])
        IOText = int(request.form['iot'])
        SEint = int(request.form['intse'])
        CNint = int(request.form['intcn'])
        IOTint = int(request.form['intiot'])

        SE = SEext+SEint
        CN = CNext+CNint
        IOT = IOText+IOTint
        #print(SE+CN+IOT)
        if SE<35 or CN<35 or IOT<35:
           marks =SE+CN+IOT
        if marks<=210:
            result = 'FAIL'
        elif 220<=marks<=300:
            result = 'Just Pass'
        else :
            reult = 'Result Not Released'
        return  render_template('index.html',result = result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)