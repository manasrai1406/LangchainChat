import streamlit as st
import os
from secret_key import openapi_key
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set up OpenAI API key
os.environ['OPENAI_API_KEY'] = openapi_key

# Initialize the LLM with the OpenAI API
llm = OpenAI(openai_api_key= openapi_key, temperature=0.75)

# Initialize conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Define the main prompt template
main_prompt_template = """You are a career counsellor for an EdTech company. Use the conversation history to provide personalized advice to the student.

Conversation History:
{history}

Student: {user_input}
Counsellor:"""

def generate_prompt(conversation, user_input):
    history = "\n".join(conversation)
    return main_prompt_template.format(history=history, user_input=user_input)

# Streamlit user interface
st.title("Welcome to EasyEd Community")

name = st.text_input("Enter your name")
if name! = '':
    st.write(f"Hello {name}! Let's clarify your doubts.")
    st.subheader("Enter Your Current Education Level")
    edu_level = st.radio(
        "Please select one:",
        ["High-School-Junior", "College", "Intermediate"],
        index=None
    )
    st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if edu_level != None:
        problem_description = st.text_input("Describe the problem you are facing")
        if problem_description:
            hobby = st.text_input("Enter your favourite pastime hobby")
            if hobby:
                st.header("Answer the following questions according to the scale given below:")

                questions = [
                    "How do you feel about working in team environments versus working independently?",
                    "When faced with a problem, do you tend to approach it systematically or do you prefer to explore various possibilities before deciding on a solution?",
                    "How important is it for you to have clear goals and objectives in your work?",
                    "Would you prefer a career that allows for constant learning and adaptation, or one that provides stability and routine?",
                    "Can you handle stressful situations or high-pressure environments?"
                ]

                responses = []
                for i, question in enumerate(questions, 1):
                    st.subheader(f"Question {i}: {question}")
                    response = st.radio(
                        f"Select your choice for Question {i}",
                        [f"{i}.{j} {option}" for j, option in enumerate([
                            "Strongly Agree", "Slightly Agree", "Agree", "Disagree", "Slightly Disagree", "Strongly Disagree"
                        ], 1)],
                        index=None
                    )
                    responses.append(response)

                if all(responses):
                    # Generate prompt for personality analysis
                    answer_stmt = (
                        f"Assume you are a career counsellor for {name}, a {edu_level} student. "
                        f"The student's problem description is: {problem_description}. Their hobby is {hobby}. "
                        f"Here are their responses to the questions: "
                        f"1) {responses[0]}, 2) {responses[1]}, 3) {responses[2]}, 4) {responses[3]}, 5) {responses[4]}. "
                        f"Based on this information, determine and summarize their personality type."
                    )

                    # Run the personality analysis prompt
                    prompt = generate_prompt(st.session_state.conversation, answer_stmt)
                    chain = LLMChain(prompt_template=PromptTemplate(input_variables=["user_input"], template=prompt), llm=llm)
                    personality_type = chain.run(user_input=answer_stmt)

                    st.session_state.conversation.append(f"Student: {answer_stmt}")
                    st.session_state.conversation.append(f"Counsellor: {personality_type}")

                    # Display personality type
                    st.write(f"The personality type is: {personality_type}")

                    # Generate prompt for career advice based on personality type
                    goals = (
                        f"Based on the personality type '{personality_type}', suggest the top 5 career options for {name}. "
                        f"Provide the name of the profession and a short description (max 15 words) for each."
                    )

                    career_options = llm.invoke(goals)
                    st.subheader("Some great career options for you could be:")
                    st.write(career_options)

                    # Append career advice to the conversation history
                    st.session_state.conversation.append(f"Student: {goals}")
                    st.session_state.conversation.append(f"Counsellor: {career_options}")

            else:
                st.subheader("Please enter your favourite pastime hobby to continue.")
        else:
            st.subheader("Please describe the problem you are facing to continue.")
    else:
        st.subheader("Please select your current education level to continue.")

# Display conversation history
st.header("Conversation History")
for message in st.session_state.conversation:
    st.write(message)

# Button to clear the conversation history
if st.button("Clear Conversation"):
    st.session_state.conversation = []
    st.experimental_rerun()
