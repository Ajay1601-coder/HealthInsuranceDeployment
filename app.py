import numpy as np
import pickle
from flask import Flask,request,render_template
#from sklearn.preprocessing import MinMaxScaler
app=Flask(__name__)

pickle_file =  pickle.load(open("insurance.pkl", 'rb'))

@app.route('/')   ## Home page
def Home_page():
    return render_template('health.html')


@app.route('/sub',methods =['POST'])
def predict():
     if request.method == 'POST':
       
       
        gen=request.form['gen']
        if(gen=='Male'):
            gen=1
        else:
            gen=0
        
        age = int(request.form["age"] ) 
        #age1=(age-20)/(85-20)
        
        
        dlicense=request.form['dl']
        if(dlicense=='Yes'):
           dlicense=1
                
        else:
            dlicense=0
        
        rc=int(request.form["rc"])
        #rc1=rc/52
        
        pi=request.form['pi']
        if(pi=='Yes'):
            pi=1
        else:
            pi=0
         
        
        vehicleage=request.form["vehicleage"]
        if (vehicleage=='1-2 Year'):
            vehicleage=0
        elif (vehicleage=='< 1 Year'):
            vehicleage=1
        else:
            vehicleage=2
            
        
        vd=request.form['vd']
        if(vd=='Yes'):
            vd=1
        else:
            vd=0
            
        
        ap=float(request.form["ap"])
        #ap1=(ap-2630.000)/(540165.000 - 2630.000)
        
        psc=int(request.form["psc"])
        #psc1=(psc-1)/162
        
        vin=int(request.form["vin"])
        #vin1=(vin -10)/(299-10)
        
     
        data =list([gen,age,dlicense,rc,pi,vehicleage,vd,ap,psc,vin])
        final_features = [np.array(data)]
        #pickle_file =  pickle.load(open("insurance.pkl", 'rb'))
        my_prediction = pickle_file.predict(final_features)
        
        #data=data.reshape(1,-1)
        my_prediction=my_prediction[0]
        if int(my_prediction)==1:
            prediction="Congratulations! You are eligible for Claiming Health Insurance"
        else:
            prediction="Oops! You cant claim Health Insurance"
        
        
        return render_template('result.html', prediction_text=prediction)

if __name__=='__main__':
         app.run(debug=True)

        
         
