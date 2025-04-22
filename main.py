import streamlit as st
import helper
import pickle

model = pickle.load(open("notebooks/model.pkl", "rb"))
cv = pickle.load(open("notebooks/cv.pkl", "rb"))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    # Validation logic
    if not q1 and not q2:
        st.error("Please fill correctly. Both questions are empty.")
    elif not q1:
        st.error("Please fill correctly. Question 1 is empty.")
    elif not q2:
        st.error("Please fill correctly. Question 2 is empty.")
    else:
        # Continue with existing logic when both questions are provided
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]

        if result:
            st.header('Duplicate')
        else:
            st.header('Not Duplicate')