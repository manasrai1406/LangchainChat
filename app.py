import streamlit as st 
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

OPENAI_API_KEY = st.secrets["key"]

llm = OpenAI(openai_api_key = OPENAI_API_KEY,temperature = 0.8)

st.subheader("Hello Welcome to career counselling bot")
name = st.text_input("Enter your name")

if name != '':
    st.write(f"Hello {name} Let's clarify your doubts")
    st.subheader("Enter Your Current Education Level")
    genre = st.radio(
    "Please select one:",
    ["High-School-junior", "College", "Intermediate"],index = None)
    st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if genre != None:
        TMAY = st.text_input("Describe the problem you are facing")
        if TMAY != '':
            Hobby = st.text_input("Enter your favourite Passtime Hobby")
            if Hobby != '':
                # prompt_template=PromptTemplate(input_variables=['Hobby'],template="As a career counsellor for a student and hobbies as {Hobby} generate some career option")
                # prompt_template.format(Hobby=Hobby)
                # chain=LLMChain(llm=llm,prompt=prompt_template)
                # feedback = chain.run(Hobby)
                # st.write(feedback)
                st.header("Answer following questions according to the scale given below :")
                # param1 = st.slider('Question 1 -> **How do you feel about working in team environments versus working independently?**', 0, 6, 1)
                # param2 = st.slider('Question 2 -> **When faced with a problem, do you tend to approach it systematically or do you prefer to explore various possibilities before deciding on a solution?**', 0, 6, 1)
                # param3 = st.slider('Question 3 -> **How important is it for you to have clear goals and objectives in your work?**', 0, 6, 1)
                # param4 = st.slider('Question 4 -> **Would you prefer a career that allows for constant learning and adaptation, or one that provides stability and routine?**',0,6,1)
                # param5 = st.slider('Question 5 -> **Can do you handle stressful situations or high-pressure environments?**',0,6,1)
                
                st.subheader("Question 1 : How do you feel about working in team environments versus working independently?")
                param1 = st.radio("Select your choice",
                ["1.1 Strongly Agree","1.2 Slightly Agree","1.3 Agree","1.4 Disagree","1.5 Slightly Diagree","1.6 Strongly Diasagree"],index = None)

                st.subheader("Question 2 : When faced with a problem, do you tend to approach it systematically or do you prefer to explore various possibilities before deciding on a solution?")
                param2 = st.radio("Select your choice",
                ["2.1 Strongly Agree","2.2 Slightly Agree","2.3 Agree","2.4 Disagree","2.5 Slightly Diagree","2.6 Strongly Diasagree"],index = None)

                st.subheader("Question 3 : How important is it for you to have clear goals and objectives in your work?")
                param3 = st.radio("Select your choice",
                ["3.1 Strongly Agree","3.2 Slightly Agree","3.3 Agree","3.4Disagree","3.5 Slightly Diagree","3.6 Strongly Diasagree"],index = None)

                st.subheader("Question 4 : How important is it for you to have clear goals and objectives in your work?")
                param4 = st.radio("Select your choice",
                ["4.1 Strongly Agree","4.2 Slightly Agree","4.3 Agree","4.4 Disagree","4.5 Slightly Diagree","4.6 Strongly Diasagree"],index = None)

                st.subheader("Question 5 : Can do you handle stressful situations or high-pressure environments?")
                param5 = st.radio("Select your choice",
                ["5.1 Strongly Agree","5.2 Slightly Agree","5.3 Agree","5.4 Disagree","5.5 Slightly Diagree","5.6 Strongly Diasagree"],index = None)


                

                if param1!=None and param2 != None and param3!= None and param4!=None and param5 != None:
                    answer_stmt = f"Assume that you are a career counsellor for {name} who is a {genre} student your task is to identify his personality type according to psychology and  he has {TMAY} as his description and hobbies as {Hobby} also on asking him How do you feel about working in team environments versus working independently he answers {param1} and for question When faced with a problem, do you tend to approach it systematically or do you prefer to explore various possibilities before deciding on a solution? he answers {param2} and for third question which is How important is it for you to have clear goals and objectives in your work? he answers as {param3} when asked about how important it is to have clear goals and objective for work he answered {param4} and for the last question which is How do you handle stressful situations or high-pressure environments? he replies as {param5} answer his peronality type in 10 words"

                    type_personality = llm.invoke(answer_stmt)
                    st.write(f"The personality type is as {type_personality}")

                    goals = f"Based on {type_personality} tell top 5 career options for {name} just give name of profession and text about him in not more tha 15 words and don't display word count try to keep description short as possible"   
                    final_goal = llm.invoke(goals)
                    st.write(final_goal)

                # prompt_template = PromptTemplate()
                # prompt_template.format()
                # chain=LLMChain(llm=llm,prompt=prompt_template)
                # feedback = chain.run()
                # # st.write(feedback)
                # type_personality = llm.invoke(answer_stmt)
                # st.write(f"The personality type is as {type_personality}")

                # goals = f"Based on {type_personality} tell top 5 career options for {name} just give name of profession and text about hem in not more tha 15 words try to keep description short as possible"   
                # final_goal = llm.invoke(goals)
                # st.write(final_goal)                          
    else:
        st.subheader("Please **Select** Education status to continue ⬆️ ")
    

    
