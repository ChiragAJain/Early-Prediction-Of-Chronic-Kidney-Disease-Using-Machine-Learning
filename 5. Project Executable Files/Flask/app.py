from flask import Flask,render_template,request
from pickle import load
import pandas as pd

app =Flask(__name__)

with open('CKD.pkl','rb') as file:
    model=load(file,encoding='utf-8')
with open('Label_Encoder.pkl','rb') as file:
    label_enc = load(file)

Categorical = ['rbc','rc','pc','ba','bgr','htn','dm','cad','appet','pe','ane','pcc']
@app.route('/')
def home_page():
    return render_template('landing.html')
@app.route('/ckd_predict')
def start_page():
    return render_template('index.html')
@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        age=request.form['Age']
        bp=request.form['bp']
        sg=request.form['sg']
        bu=request.form['bu']
        sc=request.form['sc']
        sod=request.form['sod']
        pot=request.form['pot']
        hemo=request.form['hemo']
        wc=request.form['wc']
        rc=request.form['rc']
        al=request.form['al']
        su=request.form['su']
        rbc=request.form['rbc']
        pc=request.form['pc']
        pcc=request.form['pcc']
        ba=request.form['ba']
        bgr=request.form['bgr']
        dm=request.form['htn']
        cad=request.form['cad']
        appet=request.form['appet']
        htn=request.form['htn']
        pe=request.form['pe']
        ane=request.form['ane']
        column = [[age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,wc,rc,htn,dm,cad,appet,pe,ane]]
        data = pd.DataFrame(column,columns = ['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','wc','rc','htn','dm','cad','appet','pe','ane'])
        for i in Categorical:
            data[i]=label_enc.fit_transform(data[i])
        prediction = model.predict(data)[0]
        if prediction == [1]:
            return render_template('NoCKD.html')
        elif prediction ==[0]:
            return render_template('CKD.html')
        else:
            return f'An error occured'
    else:
        f'Request Method Error'
@app.route('/CKD')
def CKD():
    return render_template('CKD.html')

@app.route('/NoCKD')
def NoCKD():
    return render_template('NoCKD.html')

if __name__=='__main__':
    app.run(debug=True)