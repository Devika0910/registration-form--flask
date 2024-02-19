from flask import Flask,render_template,request
app= Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/file',methods=['POST'])
def ff():
    name=request.form['name']
    email=request.form['email']
    return render_template('file.html', name=name, email=email)


if __name__ == '__main__':
    app.run(debug=True)