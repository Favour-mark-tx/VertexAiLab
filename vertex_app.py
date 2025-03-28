import streamlit as st
import os

import vertexai

from vertexai.generative_models import FunctionDeclaration, GenerationConfig, GenerativeModel, Tool

vertexai.init(project=os.environ.get("sectiona4project"), location="us-central1")

model = GenerativeModel(
    model_name="gemini-1.5-flash-002"
    # system_instruction=[]
)

st.title("Find your neighboring states")

users_state = st.text_input("Enter your state")


# Section A: Add in your Vertex AI API call below

if users_state:
    response = model.generate_content(
        "What are the neighbouring states to " + users_state + "?"
    )
    st.write("The neighboring states are:")
    st.write(response.text)



# End of Section A





# Section B:  Output the results to the user below



# End of Section B 