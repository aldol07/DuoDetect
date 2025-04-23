import streamlit as st
import helper
import pickle
import re

model = pickle.load(open("notebooks/model.pkl", "rb"))
cv = pickle.load(open("notebooks/cv.pkl", "rb"))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

def is_valid_question(text):
    """Check if the input text is a valid question."""
    
    text = text.strip()
    
    if len(text) < 5:
        return False
    words = re.findall(r'\b\w+\b', text)
    if len(words) < 2:
        return False
    
    
    question_words = ['what', 'how', 'why', 'when', 'where', 'which', 'who', 'whom', 'whose', 'is', 'are', 'do', 'does', 'did', 'can', 'could', 'will', 'would', 'should', 'has', 'have']
    
    has_question_mark = '?' in text
    starts_with_question_word = any(text.lower().startswith(word) for word in question_words)
    contains_question_word = any(word.lower() in question_words for word in words)
    
    
    return has_question_mark or starts_with_question_word or contains_question_word

if st.button('Find'):
    
    if not q1 and not q2:
        st.error("Please fill correctly. Both questions are empty.")
    elif not q1:
        st.error("Please fill correctly. Question 1 is empty.")
    elif not q2:
        st.error("Please fill correctly. Question 2 is empty.")
    
    elif not is_valid_question(q1):
        st.error("Input 1 doesn't appear to be a valid question. Please enter a proper question.")
    elif not is_valid_question(q2):
        st.error("Input 2 doesn't appear to be a valid question. Please enter a proper question.")
    else:
        
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]

        if result:
            st.header('Duplicate')
        else:
            st.header('Not Duplicate')