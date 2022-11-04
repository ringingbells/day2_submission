import streamlit as st
# other libs
import numpy as np
import pandas as pd
import pickle

#Load model
with open('diabeties_model.pkl', "rb") as f:
	model = pickle.load(f)


@st.cache()
def predict(age, sex, bmi, bp, s1, s2):
	# Making predictions
	prediction = model.predict([[age, sex, bmi, bp, s1, s2]])
	return prediction

def main():
	# -- Set page config
	apptitle = 'Diabetes Model'
	st.set_page_config(page_title=apptitle, page_icon='random', 
		layout= 'wide', initial_sidebar_state="expanded")

	# give a title to your app
	st.title('Predict Diabetes Progression')
	html_temp = """ <div style ="background-color:AntiqueWhite;padding:15px"> 
       <h1 style ="color:black;text-align:center;">This model predicts diabetes progression</h1> 
       </div> <br/>"""

    #display the front end aspect
	st.markdown(html_temp, unsafe_allow_html = True)
	# let us make infrastructure to provide inputs
	# we will add the inputs to side bar
	st.sidebar.info('Provide input using the panel')
	st.info('Click Assess button below')

	age = st.sidebar.slider('Age', 0, 60, 100)
	st.write('input age', age)
	sex = st.sidebar.radio('Sex', [1, 2])
	st.write('input sex', sex)
	bmi = st.sidebar.slider('Body Mass Index', 10, 20, 60)
	st.write('bmi', bmi)
	bp = st.sidebar.slider('BP', 10, 150, 60)
	st.write('input bp', bp)
	s1 = st.sidebar.slider('TC', 30, 350, 150)
	st.write('input tc', s1)
	s2 = st.sidebar.slider('LDL', 20, 250, 100)
	st.write('input ldl', s2)

	result =""
	# assessment button
	if st.button("Predict"):
		assessment = predict(age, sex, bmi, bp, s1, s2)
		st.success('**Progression of Diabetes:** {}'.format(assessment))

	# if st.button("Reset"):
	# 	pyautogui.hotkey("ctrl","F5")

	# st.balloons()
	st.success("App is working!!") # other tags include st.error, st.warning, st.help etc.

if __name__ == '__main__':
	main()
