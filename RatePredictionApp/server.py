from flask import Flask,request,render_template,url_for,redirect
from forms import PredictForm 
from Areanames import getareanames


import pickle


app = Flask(__name__)
app.config['SECRET_KEY'] = '318e2013cc0b3183eff7e57e112c888e'


@app.route('/',methods=['POST','GET'])
def homepage():
    return render_template('home.html')
@app.route('/chennai',methods=['POST','GET'])    
def chennai():
    form = PredictForm()
    name = getareanames()
    if form.validate_on_submit():
        return redirect(url_for('test'))
    return render_template('chennai.html', form =form,data = name,title='Home')
    
@app.route('/bangalore',methods=['POST','GET'])    
def bangalore():
    form = PredictForm()
    name = getareanames()
    if form.validate_on_submit():
        return redirect(url_for('test1'))
    return render_template('bangalore.html', form =form,data = name,title='Home')    

@app.route("/test" , methods=['GET', 'POST'])
def test1():
    form = PredictForm()
    name = getareanames()
    select = request.form.get('comp_select')
    AreaNo = name.Area_Names1[select]
    with open('./Resources/bangalorehouseprediction.pickle','rb') as f:
        model = pickle.load(f)
    predict =int(model.predict([[AreaNo,form.INTSQFT.data,form.BHK.data,form.BATHROOMS.data]]))
    data2= ("AREA",select," AREA NO",AreaNo,"Square feet",form.INTSQFT.data,"BHK",form.BHK.data,"BATHROOMS",form.BATHROOMS.data)
    return render_template('test.html',data = predict,data2 =data2)
    #return str(predict)


@app.route("/test" , methods=['GET', 'POST'])
def test():
    form = PredictForm()
    name = getareanames()
    select = request.form.get('comp_select')
    AreaNo = name.Area_Names[select]
    with open('./Resources/chennaihousepredictionpickle.pickle','rb') as f:
        model = pickle.load(f)
    predict =int(model.predict([[AreaNo,form.INTSQFT.data,form.BHK.data,form.BATHROOMS.data]]))
    data2= ("AREA",select," AREA NO",AreaNo,"Square feet",form.INTSQFT.data,"BHK",form.BHK.data,"BATHROOMS",form.BATHROOMS.data)
    return render_template('test.html',data = predict,data2 =data2)
    #return str(predict)

app.run(debug=True)


