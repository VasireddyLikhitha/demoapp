from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def demo():
    if request.method == 'POST':
        weight = int(request.form['weight'])
        height = float(request.form['height'])
        bmi_cal = weight/(height**2)
        bmi = round(bmi_cal,2)
        #print (bmi)
        if bmi<5:
            result='Under weight'
        elif 5<=bmi<=9:
            result='normal'
        elif 10<=bmi<=15:
            result='obase'
        else:
            result='overweight'
        output = {'bmi':bmi,'result':result}
        return render_template('result.html',data=output)
    return render_template('result.html')
app.run(use_reloader=True,debug=True)