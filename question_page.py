import streamlit as st

def question_page():
    """Question page for the app"""
    st.title("demAi")

    # Question 1
    if st.session_state["question_number"] == 0:
        
        with st.form("Question 1"):
        
            q1_ans = st.text_area(st.session_state['generated_questions'][0]['Question'])
            submitted = st.form_submit_button("Submit Q1")
            if submitted:
                st.session_state["question_number"] += 1
                st.session_state["responses"].append(q1_ans)
                st.rerun()

        

    # Question 2
    elif st.session_state["question_number"] == 1: 
        with st.form("Question 2"):
        
            q2_ans = st.text_area(st.session_state['generated_questions'][1]['Question'])
            submitted = st.form_submit_button("Submit Q2")
            if submitted:
                st.session_state["question_number"] += 1
                st.session_state["responses"].append(q2_ans)
                st.rerun()

    # Question 3
    elif st.session_state["question_number"] == 2:
        
        with st.form("Question 3"):
            q3_ans = st.text_area(st.session_state['generated_questions'][2]['Question'])
            submitted = st.form_submit_button("Submit Q3")
            if submitted:
                st.session_state["question_number"] += 1
                st.session_state["responses"].append(q3_ans)
                st.rerun()
    # Responses
    else:
        st.write("Thank you for your responses!")
        # Show questions and answer pairs
        for i in range(3):
            st.write(f"Question {i+1}: {st.session_state['generated_questions'][i]['Question']}")
            st.write(f"Your Answer: {st.session_state['responses'][i]}")

        # Add an analyse button
        analyse_button = st.button("Analyse")
        if analyse_button:
            st.session_state["current_page"] = "analysis_page"
            st.rerun()
        
