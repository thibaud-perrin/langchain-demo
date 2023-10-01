import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")

user_animal_type = st.sidebar.selectbox(
    "What is your pet?", ("Cat", "Dog", "Cow", "Hamster")
)

user_pet_color = st.sidebar.text_area(
    f"What color is your {user_animal_type.lower()}?", max_chars=10
)

if user_pet_color is not None:
    # response = lch.generate_pet_name(
    #     animal_type=user_animal_type, pet_color=user_pet_color
    # )
    # st.text(response["pet_names"])
    pass
