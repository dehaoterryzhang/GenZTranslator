import streamlit as st
from translator import translate_EtoZ, translate_ZtoE

st.title("Gen Z Translator")

# Toggle: Select translation mode
translation_mode = st.radio(
    "Choose translation mode:",
    ("Formal English to Gen Z", "Gen Z to Formal English")
)

if translation_mode == "Formal English to Gen Z":
    user_input = st.text_input("Enter text to translate into Gen Z language:")
else:
    user_input = st.text_input("Enter Gen Z text to translate into formal English:")

temperature = st.slider(
    "Choose response creativity (Temperature):",
    min_value=0.0,
    max_value=1.5,
    value=0.8,  # Default temperature
    step=0.1
)

if st.button("Translate"):
    if user_input.strip():
        try:
            if translation_mode == "Formal English to Gen Z":
                slang_translation = translate_EtoZ(user_input, temperature)
            else:
                slang_translation = translate_ZtoE(user_input, temperature)
            st.success(f"Translation: {slang_translation}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to translate.")

