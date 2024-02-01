import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("wqi.pkl","rb")
classifier=pickle.load(pickle_in)
p1 = open("temp.pkl","rb")
c1=pickle.load(p1)
p2 = open("do.pkl","rb")
c2=pickle.load(p2)
p3 = open("ph.pkl","rb")
c3=pickle.load(p3)
p4 = open("con.pkl","rb")
c4=pickle.load(p4)
p5 = open("bod.pkl","rb")
c5=pickle.load(p5)
p6 = open("nit.pkl","rb")
c6 =pickle.load(p6)
p7 = open("fec.pkl","rb")
c7 =pickle.load(p7)
p8 = open("tot.pkl","rb")
c8 =pickle.load(p8)

with open('style.css') as f :
      st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def welcome():
    return "Welcome All"

def temp(year):
     
    prediction=c1.predict([[year]])
    print(prediction)
    return prediction

def dox(year):
     
    prediction=c2.predict([[year]])
    print(prediction)
    return prediction

def pH(year):
     
    prediction=c3.predict([[year]])
    print(prediction)
    return prediction

def cond(year):
     
    prediction=c4.predict([[year]])
    print(prediction)
    return prediction
  
def biod(year):
     
    prediction=c5.predict([[year]])
    print(prediction)
    return prediction

def nitr(year):
     
    prediction=c6.predict([[year]])
    print(prediction)
    return prediction
  
def fecoli(year):
     
    prediction=c7.predict([[year]])
    print(prediction)
    return prediction  

def total(year):
     
    prediction=c8.predict([[year]])
    print(prediction)
    return prediction 

def wqix(year):
     
    prediction=classifier.predict([[year]])
    print(prediction)
    return prediction 
def main():
    html_temp = """
    <div style="background-color:skyblue;padding:10px;border-radius:5px">
    <h2 style="color:white;text-align:center;font-family:Callibri;"><b>Indian River Water Quality Analysis</b></h2>
    
    </div>
    <style>
        .st-emotion-cache-kskxxl.e116k4er3 {
            border-color:white;
        }
        div.st-emotion-cache-zt5igj.e1nzilvr4 {
            color:rgb(37, 2, 78);
        }
        div.element-container.st-emotion-cache-13tdgzb.e1f1d6gn4 {
            height:70px;
        }

        div.st-emotion-cache-16idsys.e1nzilvr5 p{
            font-size: 14px;
            font-weight: bold;
        }

        div.st-emotion-cache-16idsys.e1nzilvr5 {
            width: 100%;
            text-align: center;
        }l

        div.stMarkdown {
            vertical-align: bottom;
        }

        div.st-emotion-cache-5rimss.e1nzilvr5 {
            align-items: center;
        }

        div.st-emotion-cache-5rimss.e1nzilvr5 p{
            font-size: 18px;
            font-weight: bold;
        }

        div.st-af.st-ah.st-ba.st-ar.st-as.st-ax.st-ay.st-az.st-b0.st-b1.st-b2.st-bb.st-b7 {
            height:40px;
            width:224px;
            border-color:white;
            text-align: center;
        }

        button.st-emotion-cache-7ym5gk.ef3psqc12 {
            width: 100%;
        }

        div.st-emotion-cache-1vbkxwb.e1nzilvr5 p{
            font-size: large;
        }

        div.st-emotion-cache-1vbkxwb.e1nzilvr5 p:hover{
            font-weight: bold;
        }

        button.step-down.st-emotion-cache-zbmw0q.e116k4er1:hover {
            background-color:darkslateblue ;
        }

        button.step-up.st-emotion-cache-zbmw0q.e116k4er1:hover {
            background-color:darkslateblue ;
        }

        button.st-emotion-cache-1umgz6k.ef3psqc12:hover {
            border-color: lightblue;
            background-color:skyblue;
            color:white;
        }
        </style>
    <br></br>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    year = st.number_input("Year",step=1,min_value=2023)
    #temp min - 24
    #temp = 30
    # do min - 5
    #do = 7.5
    #ph min - 6.8
    #ph = 8.5
    #con min - 435
    #con = 2800
    #bod min - 1.65
    #bod = 20
    #n min - 0.1
    #n = 2
    #fc min- 5000
    #fc = 3600000
    #tc min - 7800
    #tc = 8400000
    result=""
    if st.button("Predict"):
        tem = temp(year)
        do = dox(year)
        ph = pH(year)
        con = cond(year)
        bod= biod(year)
        nit = nitr(year)
        fec = fecoli(year)
        tot = total(year)
        c1,c2,c3 = st.columns(3)
        c1.write("Physical Parameters :")
        c2.text_area(label="Temperature", value="{:.2f}".format(tem[0]))
        c3.text_area(label="Conductivity", value="{:.2f}".format(con[0]))
        c1.write("Chemical Parameters :")
        c2.text_area(label="Dissolved Oxygen", value="{:.2f}".format(do[0]))
        c3.text_area(label="pH", value="{:.2f}".format(ph[0]))
        c1.write("Biological Parameters :")
        c2.text_area(label="Bio-chemical Oxygen Demand", value="{:.2f}".format(bod[0]))
        c3.text_area(label="Nitrate", value="{:.2f}".format(nit[0]))
        c2.text_area(label="Fecal Coliform", value="{:.2f}".format(fec[0]))
        c3.text_area(label="Total Coliform", value="{:.2f}".format(tot[0]))
        result = wqix(year)
        st.success('The Water Quality Index of the river is {:.2f}.'.format(result[0]))
        
        if result <= 25 :
          st.success('The quality of the water is excellent')  
          image = Image.open('Excellent.jpg')
          st.image(image, caption='Excellent')
        elif result >= 25 and result <= 50:
          st.success('The quality of the water is good')  
          image = Image.open('Good.jpg')
          st.image(image, caption='Good')
        elif result >= 50 and result <= 75:
          st.success('The quality of the water is poor')
          image = Image.open('Poor.jpg')
          st.image(image, caption='Poor')
        else:
          st.success('The quality of the water is very poor')
          image = Image.open('Very Poor.jpg')
          st.image(image, caption='Very Poor')

if __name__=='__main__':
    main()
    
