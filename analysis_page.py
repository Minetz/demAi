import streamlit as st
from data_mgmt import get_analysis_prompt, get_report_prompt
from model_interactions import get_gpt_response


def analysis_page():
    """Analysis page for the app"""
    st.title("demAi Analysis")
    # Given these questions we need to pair the questions with the examples and the traits and the answer into a single prompt.    
    questions = st.session_state['generated_questions']
    answers = st.session_state['responses']
    expand = True
    # Generate report summary if analysis has been performed!
    if st.session_state['report']:
        with st.container(border=True):
            st.write("Report Summary")
            report_prompt = get_report_prompt(questions, answers, st.session_state['analysis'])
            response = get_gpt_response(report_prompt)
            st.write(f"Overview report: \n{response}")
        expand = False
    # Show questions and answer pairs
    analysis = []
        
    with st.expander("See explanation", expanded=expand):
        for i in range(3):
            with st.container(border=True):
                st.write(f"Question {i+1}: {questions[i]['Question']}")
                st.write(f"Your Answer: {answers[i]}")
                # Write the prompt we are quantifying
                st.write(f"Trait: {questions[i]['example_a']['trait']}")
                # If we have not done the analysis yet
                if st.session_state['analysis'] == []:
                    # Build the prompt for the analysis
                    prompt = get_analysis_prompt(question=questions[i], answer=answers[i])
                    # Send the prompt to GPT35 for analysis
                    response = get_gpt_response(prompt)
                    analysis.append(response)
                else:
                    response = st.session_state['analysis'][i]

                st.write(f"\nAnalysis for Question {i+1}: \n{response}")
    
    if i == 2:
        # Save the analysis
        if st.session_state['analysis'] == []:
            st.session_state['analysis'] = analysis
        if st.session_state['report'] is False:
            # Add a button to generate the report
            generate_report_button = st.button("Generate Report")
            if generate_report_button:
                st.session_state['report'] = True
                st.rerun()

